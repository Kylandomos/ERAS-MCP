# ERAS Scripts Notes

## MDB Discovery / Schema Script

Script: `scripts/eras/eras_mdb_discovery.py`

### Runtime Dependencies (Windows)

- Python 3.14 (user install validated at `C:\Python314\python.exe`)
- `pyodbc==5.3.0`
- 64-bit `Microsoft Access Driver (*.mdb, *.accdb)`

### Typical Run

```powershell
python scripts/eras/eras_mdb_discovery.py --copy-reports-to-docs
```

### Current Status Note

- Discovery/copy/hash pipeline is working on the verified root `C:\AppSogelink\ERAS_Connect_2026`.
- Schema extraction is partial: some databases still return ODBC decode warnings (`utf-16-le ... illegal UTF-16 surrogate`).
