import db_addevent
import db_getevents
import db_adduser
import db_getuser
from datetime import datetime
from user import User

NUM = 6

def test():
    for i in range(NUM):
        tmpdate = datetime.now()
        if i%2==0:
            db_addevent.main(tmpdate, 0)
        else:
            db_addevent.main(tmpdate, 1)

def test_query():
    return db_getevents.main()

def listevents():
    events = test_query()
    for event in events:
        print(event)

def fill_users():
    user1 = User("Pecneb", "ecneb2000@gmail.com", "Kakafej", 1)
    user2 = User("Pecneb1", "ecneb2001@gmail.com", "Kakafej1", 0)
    user3 = User("Pecneb2", "ecneb2002@gmail.com", "Kakafej2", 0)
    user4 = User("Pecneb3", "ecneb2003@gmail.com", "Kakafej3", 0)
    con = db_adduser.create_connection(db_adduser.PATH)
    db_adduser.main(user1.getName(), user1.getEmail(), user1.getEmail(), user1.getIsadmin())

def list_users():
    users = db_getuser.main()
    for user in users:
        print(user)
    
list_users()