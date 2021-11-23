import os
import sqlite3
from sqlite3 import Error

PATH = "sqlite/db/rpi.db"

def create_connection(db_file):
    '''
    Create a database connection.
    Return connection object or none.
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("DB connection created!")
        return conn
    except Error as e:
        print(e)

    return conn

def add_event(datetime, authenticated):
    conn = create_connection(PATH)

    # format datetime for db
    date2db = datetime.strftime("%Y-%m-%d %H:%M:%S")
    authenticated2db = authenticated
    event = (date2db, authenticated2db)
    sql_addevent = f""" INSERT INTO events (date, authenticated)
                        VALUES (?,?) """
    
    # try get to cursor
    try:
        c = conn.cursor()
        c.execute(sql_addevent, event)
        conn.commit()
        conn.close()
        print("Event successfully added to database!")
        return True
    except Error as e:
        print(e)
    return False

def get_events():
    conn = create_connection(PATH)

    try:
        cur = conn.cursor()
        sql_query = """SELECT * FROM events"""
        cur.execute(sql_query)
        r = cur.fetchall()
        conn.close()
        return r
    except Error as e:
        print(e)

def add_user(name, email, password, isadmin):
    conn = create_connection(PATH)
    
    try:
        c = conn.cursor()
        script = """INSERT INTO users (name, password, email, isadmin)
                    VALUES(?,?,?,?)"""
        c.execute(script, (name,password,email,isadmin))
        conn.commit()
        conn.close()
        print("User successfully added to database!")
        return True
    except Error as e:
        print(e)
    return False

def get_data():
    conn = create_connection(PATH)

    try:
        query = """SELECT * FROM users"""
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        conn.close()
        return data
    except Error as e:
        print(e)