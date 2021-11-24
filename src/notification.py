from event import Event
from pimail import Email
from db_operations import admin2event, emails2event, add_event

def make_notif(notif : Event, auth_succ : bool):
    notif.auth_success(auth_succ)
    title, msg = notif.create_notification()
    adminCreds = admin2event()
    users = emails2event()
    if adminCreds is None:
        return None
    adminEmail = adminCreds[0]
    adminPass = adminCreds[1]
    email = Email(adminEmail, title, msg, password=adminPass, to_emails=users)
    email.sendmail_securely()
    add_event(notif._date, notif.getAuthInBit())
    return True