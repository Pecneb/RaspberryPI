import db_operations
from user import User
# from event import Event

def add_test_users():
    admin = User("Pecneb", "ecneb2000@gmail.com", "testpass", 1)
    db_operations.add_user(admin.getName(), admin.getEmail(), admin.getPassword(), admin.getIsadmin())
    for i in range(1, 5):
        tmp_user = User(f"Pecneb{i}", f"ecneb{i}@gmail.com", f"testpass{i}", 0)
        db_operations.add_user(tmp_user.getName(), tmp_user.getEmail(), tmp_user.getPassword(), tmp_user.getIsadmin())

# def add_test_events():
#     for i in range(5):
#         tmp_event = Event()
#         db_operations.add_event(tmp_event._date, tmp_event.getAuthInBit())

def list_test_users():
    users = db_operations.get_data()
    for user in users:
        print(user)

# def list_test_events():
#     events = db_operations.get_events()
#     for event in events:
#         print(event)


def main():
    add_test_users()
    # add_test_events()
    list_test_users()
    #list_test_events()

if __name__ == "__main__":
    main()