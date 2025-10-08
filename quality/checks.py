class DataQualityCheck:
    def __init__(self, sf_client):
        self.sf = sf_client

    def null_check(self, table, column):
        query = f"SELECT COUNT(*) FROM {table} WHERE {column} IS NULL"
        result = self.sf.run_query(query)
        return result[0][0]

    def row_count_check(self, table, threshold):
        query = f"SELECT COUNT(*) FROM {table}"
        result = self.sf.run_query(query)
        return result[0][0] >= threshold