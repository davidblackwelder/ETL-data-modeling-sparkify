import psycopg2
import os
from dotenv import load_dotenv
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    # Load .env variables
    load_dotenv()

    # Store .env variables for default database
    # Keeps database credentials hidden
    HOST = os.getenv('HOST')
    DEFAULT_DB_NAME = os.getenv('DEFAULT_DBNAME')
    DEFAULT_USER = os.getenv('DEFAULT_USER')
    DEFAULT_PASSWORD = os.getenv('DEFAULT_PASSWORD')

    # Creates connection string
    default_conn_string = f'host={HOST} dbname={
        DEFAULT_DB_NAME} user={DEFAULT_USER} password={DEFAULT_PASSWORD}'

    # connect to default database
    conn = psycopg2.connect(default_conn_string)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute(
        "CREATE DATABASE sparkifydb WITH ENCODING 'utf8'")

    # close connection to default database
    conn.close()

    # Store .env variables for sparkify database
    # Keeps database credentials hidden
    DB_NAME = os.getenv('DBNAME')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')

    # Creates connection string
    conn_string = f'host={HOST} dbname={
        DB_NAME} user={USER} password={PASSWORD}'

    # connect to sparkify database
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database.

    - Establishes connection with the sparkify database and gets
    cursor to it.

    - Drops all the tables.

    - Creates all tables needed.

    - Finally, closes the connection.
    """
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
