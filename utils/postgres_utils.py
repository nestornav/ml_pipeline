import psycopg2

from pathlib import Path
from configparser import ConfigParser
from utils.constants import sql_dir, TABLES_FILE_NAME

def connect():
    """Get a connection to the PostgreSQL database
    """
    conn = None
    try:
        # read connection parameters
        params = config_postgres()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print('Error trying to create a new connection:', error)

def config_postgres(filename='database.ini', section='postgresql'):
    """Return all the db information to create a connection to the db.
    """
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def create_tables():
    conn = connect()
    cur = conn.cursor()
    try:
        print('Table creation is happening...')
        sql = open(Path(sql_dir, TABLES_FILE_NAME), "r").read()
        cur.execute(sql)
        conn.commit()
        print('Tables were created...')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()
        if conn is not None:
            conn.close()

def insert_values_to_table(query_table: str, values: tuple):
    """Insert a new row into a table with the given values.

      Arguments:
          query_table -- insert query to the desire table
          values -- the value to insert into the table"""
    conn = connect()
    cur = conn.cursor()
    try:
        query = query_table.format(VALUES=values)
        cur.execute(query)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        cur.close()
        if conn is not None:
            conn.close()
