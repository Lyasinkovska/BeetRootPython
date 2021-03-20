import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('my_tb.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn
    # finally:
    #     if conn:
    #         conn.close()


def create_cursor(connection):
    return connection.cursor()


def create_table(cursor, table_name: str):
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {table_name}(id INTEGER NOT NULL PRIMARY KEY, fisrtname TEXT ,lastname TEXT)')


if __name__ == '__main__':
    connection = create_connection()
    cursor = create_cursor(connection)
    create_table(cursor, 'my_table')
    connection.commit()
