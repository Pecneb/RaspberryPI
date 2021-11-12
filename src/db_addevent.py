import os
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    '''
    Create a database connection.
    Return connection object or none.
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def sql_add_event(conn, datetime, authenticated):
    date2db = datetime.strftime("%Y-%m-%d %H:%M:%S")
    authenticated2db = authenticated
    event = (date2db, authenticated2db)
    sql_addevent = f""" INSERT INTO events (date, authenticated)
                        VALUES (?,?) """
    try:
        c = conn.cursor()
        c.execute(sql_addevent, event)
    except Error as e:
        print(e)

def main(datetime, authenticated):
    path = "sqlite/db/rpi.db"
    conn = create_connection(path)
    sql_add_event(conn, datetime, authenticated)
    conn.commit()
    conn.close()