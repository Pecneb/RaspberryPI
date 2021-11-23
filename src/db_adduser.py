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

def create_user(con, name, email, password, isadmin):
    try:
        c = con.cursor()
        
        script = """INSERT INTO users (name, password, email, isadmin)
                    VALUES(?,?,?,?)"""
        c.execute(script, (name,password,email,isadmin))
        con.commit()
        
        con.close()

        return True
    except Error as e:
        print(e)
    
    return False

def main(name, email, password, isadmin):
    con = create_connection(PATH)
    create_user(con, name, email, password, isadmin)