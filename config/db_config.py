import os

POSTGRES_CONFIG = {
    "host": os.getenv("PG_HOST", "localhost"),
    "port": os.getenv("PG_PORT", 5432),
    "user": os.getenv("PG_USER", "postgres"),
    "password": os.getenv("PG_PASSWORD", "password"),
    "database": os.getenv("PG_DATABASE", "quality_metadata"),
}

SNOWFLAKE_CONFIG = {
    "user": os.getenv("SNOWFLAKE_USER", "user"),
    "password": os.getenv("SNOWFLAKE_PASSWORD", "password"),
    "account": os.getenv("SNOWFLAKE_ACCOUNT", "account"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
    "database": os.getenv("SNOWFLAKE_DATABASE", "MYDB"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA", "PUBLIC"),
}