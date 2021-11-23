import os
import sqlite3
from sqlite3 import Error

PATH = "sqlite/db/rpi.db"

def create_conn(path : str):
    conn = None

    try:
        conn = sqlite3.connect(path)
        return conn
    except Error as e:
        print(e)

    return conn

def get_events(conn):
    con = conn

    if con == None:
        print("Error: couldnt open database!")
        return False
    
    cur = con.cursor()
    con.row_factory = sqlite3
        
    sql_query = """SELECT * FROM events"""
    cur.execute(sql_query)

    r = cur.fetchall()
    
    return r

def main():
    path = PATH
    con = create_conn(path)
    return get_events(con)
    con.close()

if __name__ == "__main__":
    main()