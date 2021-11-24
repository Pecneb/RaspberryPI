from datetime import datetime

class Event(object):
    def __init__(self):
        self._date = datetime.now()
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
            return title, msg

        title = 'Intudaer Alert!'
        datestr = self._date.strftime("%d/%m/%Y %H:%M:%S")
        msg = f'''
        {datestr}
         
        Authentication failed! Intruder alert!
        '''
        return title, msg

    
    
