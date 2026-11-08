# GE Oracle Integration Lab

Python-to-Oracle Autonomous Transaction Processing (ATP) bridge and corporate integration practice lab.

## Target architecture

ERPNext / source systems → SFTP → Oracle Integration Cloud (OIC) → ATP staging and PL/SQL → Oracle Fusion Cloud AP through supported FBDI/UCM/ESS orchestration.

- **Python bridge:** local development utilities and controlled ATP connectivity.
- **ATP:** staging, validation, duplicate detection, batch control, audit, and error tracking.
- **OIC:** file movement, mapping, orchestration, Fusion upload/import jobs, monitoring, and reprocessing.
- **Oracle Fusion:** system of record. Never write directly to Fusion SaaS database tables.

## Local setup

Python 3.11+ is recommended. Create a virtual environment and install dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, then set local connection values. Keep the ATP wallet in a separate local folder and set `ORACLE_CONFIG_DIR` to that folder.

Run the read-only connectivity test:

```powershell
python scripts/test_connection.py
```

## Environment variables

- `ORACLE_USER`
- `ORACLE_PASSWORD`
- `ORACLE_DSN` (example alias: `atpdbgen3_high`)
- `ORACLE_CONFIG_DIR` (local wallet directory)
- `ORACLE_WALLET_PASSWORD` (only if required by wallet configuration)

## Security

This repository is public. Never commit `.env`, passwords, wallet files (`cwallet.sso`, `ewallet.p12`), `tnsnames.ora`, `sqlnet.ora`, private keys, certificates, production data, or real customer/supplier records. Use synthetic test data only.

## Existing ATP objects

The following objects have been reported as already present in the user's ATP schema. This repository setup does not connect to or modify the database:

- `GE_AP_INVOICE_STG`
- `GE_AP_INVOICE_LINES_STG`
- `GE_AP_INVOICE_ERRORS`
- `GE_AP_INVOICE_AUDIT`
- `GE_AP_BATCH_CONTROL`
- `GE_AP_INVOICE_PKG`

## Current status

Initial Python project scaffold. Database validation and batch processing are not yet confirmed by this repository. Any database procedure that changes data must be reviewed and explicitly approved before execution.
