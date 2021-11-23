from datetime import datetime
from pimail import email
import email_conf
import db_addevent

class Event(object):
    def __init__(self) -> None:
        self._date = datetime.now()
        self._mail = email(email_conf.admin_email, title='placeholder', message='placeholder' ,password=email_conf.password,
        to_emails=email_conf.user_email)
        self._auth = False

    def auth_success(self, succ: bool):
        '''
        sets the _auth attribute True, if user ath succeeds,  
        False otherwise
        '''
        if succ:
            self._auth  = True

    def getAuth(self):
        return self._auth
    
    def getAuthInBit(self):
        if self._auth:
            return 1
        return 0

    def create_notification(self):
        if self._auth:
            title = 'User authentication success!'
            datestr = self._date.strftime("%d/%m/%Y %H:%M:%S")
            msg = f'''
            {datestr}

            Authenticated user arrived home.
            '''
        else:
            title = 'Intudaer Alert!'
            datestr = self._date.strftime("%d/%m/%Y %H:%M:%S")
            msg = f'''
            {datestr}

            Authentication failed! Intruder alert!
            '''
        self._mail.setTitle(title)
        self._mail.setMessage(msg)

    def send_notification(self):
        self._mail.sendmail_securely()
        db_addevent.main(self._date, self.getAuthInBit())

    
    
