import sqlite3
from sqlite3 import Error

PATH = "sqlite/db/rpi.db"

def create_connection(path):
    con = None
    
    try:
        con = sqlite3.connect(path)
        return con
    except Error as e:
        print(e)
    
    return False

def get_data(con):
    if con == False:
        return False

    try:
        query = """SELECT * FROM users"""
        cur = con.cursor()
        
        cur.execute(query)
        data = cur.fetchall()
        
        con.close()
        
        return data
    except Error as e:
        print(e)

def main():
    con = create_connection(PATH)
    return get_data(con)