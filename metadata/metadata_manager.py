import psycopg2
from config.db_config import POSTGRES_CONFIG

class MetadataManager:
    def __init__(self):
        self.conn = psycopg2.connect(**POSTGRES_CONFIG)

    def get_quality_rules(self):
        cur = self.conn.cursor()
        cur.execute("SELECT table_name, check_type, threshold FROM quality_rules;")
        rules = cur.fetchall()
        cur.close()
        return rules

    def log_check_result(self, table_name, check_type, result):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO check_results (table_name, check_type, result) VALUES (%s, %s, %s);",
            (table_name, check_type, result)
        )
        self.conn.commit()
        cur.close()

    def close(self):
        self.conn.close()