"""
Superset can connect to both Snowflake and PostgreSQL directly for dashboarding.
This module can help register datasets or push results if needed.
For most cases, you manage connections and datasets in Superset UI.
"""

def print_superset_instructions():
    print("To add dashboards, connect Superset to Snowflake and/or PostgreSQL via its UI.")
    print("Add the 'check_results' table from PostgreSQL as a dataset for reporting quality checks.")