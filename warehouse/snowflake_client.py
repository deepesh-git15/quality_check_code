import snowflake.connector
from config.db_config import SNOWFLAKE_CONFIG

class SnowflakeClient:
    def __init__(self):
        self.ctx = snowflake.connector.connect(
            **SNOWFLAKE_CONFIG
        )

    def run_query(self, query):
        cur = self.ctx.cursor()
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result

    def close(self):
        self.ctx.close()