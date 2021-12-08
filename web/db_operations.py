import os
import sqlite3
from sqlite3 import Error

PATH = os.path.join("..","sqlite", "db", "rpi.db")

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

def sql_query(sql_script):
    conn = create_connection(PATH)
    try:
        cur = conn.cursor()
        cur.execute(sql_script)
        data = cur.fetchall()
        conn.close()
        print("Successful SQL Query execution!")
        return data
    except Error as e:
        print(e)


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
    sql_script = """SELECT * FROM events"""
    return sql_query(sql_script)

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

def get_user():
    sql_script = """SELECT * FROM users"""
    return sql_query(sql_script)

def emails2event():
    data = get_user()
    emails = []
    for user in data:
        emails.append(user[3])
    return emails

def admin2event():
    data = get_user()
    adminCreds = [None, None]
    for user in data:
        if user[4] == 1:
            # extract admin email from db
            adminCreds[0] = user[3]
            # extract admin password from db
            adminCreds[1] = user[2]
            break
    if (adminCreds[0] is None) or (adminCreds[1] is None):
        print("Error: No admin found in the system.")
        return None
    return adminCreds
