import pimail
import event
import email_conf

def main():
    event1 = event.event()
    event1.auth_success(True)
    event1.notif()
    event2 = event.event()
    event2.auth_success(False)
    event2.notif()

if __name__ == "__main__":
    main()