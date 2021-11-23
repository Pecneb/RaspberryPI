import os
import sqlite3
from sqlite3 import Error

PATH = "sqlite/db/rpi.db"

def createdb(db_file):
    '''
    Create SQLite database
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite version %s" , sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            print("SQLite database successfully created!")

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

def create_table(conn, create_table_sql):
    '''
    Create table from create_table_sql statement.
    '''

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    

def main():
    '''
    Create database and create tables.
    '''

    # define database path
    path = PATH
    
    # create database
    createdb(path)

    # define sql scripts
    sql_create_events_table = """ CREATE TABLE IF NOT EXISTS events (
                                    id integer PRIMARY KEY ASC AUTOINCREMENT,
                                    date text NOT NULL,
                                    authenticated integer NOT NULL
                                ); """      
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                    id integer PRIMARY KEY ASC AUTOINCREMENT,
                                    name text NOT NULL,
                                    password text NOT NULL,
                                    email text NOT NULL,
                                    isadmin integer NOT NULL
                                ); """

    # create database connection
    conn = create_connection(path)
    
    # create tables
    if conn is not None:
        # events table
        create_table(conn, sql_create_events_table)
        print("Events table successfully created!")

        # users table
        create_table(conn, sql_create_users_table)
        print("Users table successfully created!")
    else:
        print("Error! Cannot connect to database.")

    conn.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()