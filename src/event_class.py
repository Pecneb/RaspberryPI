from datetime import datetime
from pimail import email
import email_conf

class event(object):
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
        self._mail.sendmail_SSL()
    