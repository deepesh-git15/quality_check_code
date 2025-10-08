from metadata.metadata_manager import MetadataManager
from warehouse.snowflake_client import SnowflakeClient
from quality.checks import DataQualityCheck
from dashboard.superset_connector import print_superset_instructions

def main():
    meta_mgr = MetadataManager()
    sf_client = SnowflakeClient()
    dq = DataQualityCheck(sf_client)

    rules = meta_mgr.get_quality_rules()
    for table_name, check_type, threshold in rules:
        if check_type == 'row_count':
            result = dq.row_count_check(table_name, threshold)
        elif check_type == 'null_check':
            column = threshold  # Here, threshold is used as column name
            result = dq.null_check(table_name, column)
        else:
            result = None
        meta_mgr.log_check_result(table_name, check_type, result)
        print(f"Check {check_type} on {table_name}: {result}")

    meta_mgr.close()
    sf_client.close()
    print_superset_instructions()

if __name__ == "__main__":
    main()