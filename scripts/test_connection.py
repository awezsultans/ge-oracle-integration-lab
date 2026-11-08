"""Read-only Oracle ATP connectivity test."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ge_oracle_bridge.db import connect  # noqa: E402


def main() -> int:
    connection = None
    try:
        connection = connect()
        with connection.cursor() as cursor:
            cursor.execute("SELECT SYS_CONTEXT('USERENV', 'CURRENT_SCHEMA') FROM dual")
            schema = cursor.fetchone()[0]
        print(f"Connection successful. Current schema: {schema}")
        return 0
    except Exception as exc:
        print(f"Connection failed: {type(exc).__name__}: {exc}")
        return 1
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    raise SystemExit(main())
