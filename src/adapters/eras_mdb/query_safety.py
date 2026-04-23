from __future__ import annotations

from .models import QueryValidationResult

_ALLOWED_START_TOKENS = {"SELECT", "WITH"}
_FORBIDDEN_TOKENS = {
    "ALTER",
    "ATTACH",
    "COMMIT",
    "CREATE",
    "DELETE",
    "DETACH",
    "DROP",
    "EXEC",
    "EXECUTE",
    "GRANT",
    "INSERT",
    "INTO",
    "MERGE",
    "PRAGMA",
    "REINDEX",
    "REPLACE",
    "REVOKE",
    "ROLLBACK",
    "SAVEPOINT",
    "TRUNCATE",
    "UPDATE",
    "VACUUM",
}
_FORBIDDEN_COMBINATIONS = {
    ("SELECT", "INTO"),
}


def _strip_comments_and_literals(sql: str) -> str:
    cleaned: list[str] = []
    length = len(sql)
    idx = 0
    state = "normal"

    while idx < length:
        char = sql[idx]
        nxt = sql[idx + 1] if idx + 1 < length else ""

        if state == "normal":
            if char == "-" and nxt == "-":
                state = "line_comment"
                idx += 2
                continue
            if char == "/" and nxt == "*":
                state = "block_comment"
                idx += 2
                continue
            if char == "'":
                state = "single_quote"
                idx += 1
                cleaned.append(" ")
                continue
            if char == '"':
                state = "double_quote"
                idx += 1
                cleaned.append(" ")
                continue
            if char == "[":
                state = "bracket_identifier"
                idx += 1
                cleaned.append(" ")
                continue
            cleaned.append(char)
            idx += 1
            continue

        if state == "line_comment":
            if char == "\n":
                state = "normal"
                cleaned.append("\n")
            idx += 1
            continue

        if state == "block_comment":
            if char == "*" and nxt == "/":
                state = "normal"
                idx += 2
                continue
            idx += 1
            continue

        if state == "single_quote":
            if char == "'" and nxt == "'":
                idx += 2
                continue
            if char == "'":
                state = "normal"
            idx += 1
            continue

        if state == "double_quote":
            if char == '"' and nxt == '"':
                idx += 2
                continue
            if char == '"':
                state = "normal"
            idx += 1
            continue

        if state == "bracket_identifier":
            if char == "]":
                state = "normal"
            idx += 1
            continue

    return "".join(cleaned)


def _tokenize_sql(sql: str) -> list[str]:
    normalized = _strip_comments_and_literals(sql)
    separators = ",()=+-*/%<>!|&^~.;:\n\r\t"
    translated = normalized
    for separator in separators:
        translated = translated.replace(separator, " ")
    tokens = [token.upper() for token in translated.split() if token.strip()]
    return tokens


def validate_read_only_query(sql: str) -> QueryValidationResult:
    if not sql or not sql.strip():
        return QueryValidationResult(False, "Query is empty.")

    tokens = _tokenize_sql(sql)
    if not tokens:
        return QueryValidationResult(
            False, "Query contains only comments, literals, or whitespace."
        )

    if tokens[0] not in _ALLOWED_START_TOKENS:
        return QueryValidationResult(
            False,
            "Only SELECT or WITH queries are allowed in read-only mode.",
        )

    statements = [part.strip() for part in _strip_comments_and_literals(sql).split(";") if part.strip()]
    if len(statements) > 1:
        return QueryValidationResult(
            False, "Multiple SQL statements are not allowed in read-only mode."
        )

    forbidden_found = sorted(token for token in set(tokens) if token in _FORBIDDEN_TOKENS)
    if forbidden_found:
        return QueryValidationResult(
            False,
            f"Forbidden keyword(s) detected: {', '.join(forbidden_found)}.",
        )

    for first, second in _FORBIDDEN_COMBINATIONS:
        for idx in range(len(tokens) - 1):
            if tokens[idx] == first and tokens[idx + 1] == second:
                return QueryValidationResult(
                    False,
                    f"Forbidden statement pattern detected: {first} {second}.",
                )

    return QueryValidationResult(True, "Query accepted as read-only.")


def assert_read_only_query(sql: str) -> None:
    validation = validate_read_only_query(sql)
    if not validation.is_valid:
        raise ValueError(validation.reason)
