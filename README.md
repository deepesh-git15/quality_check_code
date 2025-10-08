# Quality Check Code

## Overview

A modular data quality framework using:
- **Python** for orchestration
- **PostgreSQL** for metadata config and results
- **Snowflake** as the main data warehouse
- **Superset** for dashboarding quality checks

## Structure

- `config/`: Database configs
- `metadata/`: Metadata management (Postgres)
- `warehouse/`: Snowflake interaction
- `quality/`: Quality check logic
- `dashboard/`: Superset integration/help
- `main.py`: Entrypoint

## Usage

1. Fill environment variables for DB connections.
2. Setup PostgreSQL table `quality_rules` with columns: `table_name`, `check_type`, `threshold`.
3. (Optional) Setup `check_results` table for results.
4. Run:
    ```bash
    pip install -r requirements.txt
    python main.py
    ```
5. Add `check_results` as a dataset in Superset for dashboarding.

## Extending

- Add more checks in `quality/checks.py`
- Expand metadata model as needed