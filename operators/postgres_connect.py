"""
Connects to the Postgres database
"""

import os

import psycopg2

class ConnectPostgres:
    def __init__(self):
        self.host = os.getenv("POSTGRES_HOST")
        self.port = os.getenv("POSTGRES_PORT")
        self.dbname = os.getenv("POSTGRES_DB")
        self.pg_user = os.getenv("POSTGRES_USER")
        self.pg_password = os.getenv("POSTGRES_PASSWORD")

    def postgres_connector(self):
        conn = psycopg2.connect(
            f"host='{self.host}' port='{self.port}' dbname='{self.dbname}' user='{self.pg_user}' password='{self.pg_password}'"
        )
        return conn


if __name__ == "__main__":
    conn = ConnectPostgres()
    conn.postgres_connector()
