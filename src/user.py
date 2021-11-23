from db_operations import add_user

class User(object):
    """
    This class represents a user in the database.
    """
    def __init__(self):
        self._name = "Anon"
        self._email = None
        self._password = None
        self._isadmin = 0

    def __init__(self, name, email, password, isadmin):
        self._name = name
        self._email = email
        self._password = password
        self._isadmin = isadmin

    # getter for name
    def getName(self):
        return self._name
    
    # setter for name
    def setName(self, name):
        self._name = name

    # getter for email
    def getEmail(self):
        return self._email

    # setter for email
    def setEmail(self, email):
        self._email = email

    # getter for password
    def getPassword(self):
        return self._password

    # setter for password
    def setPassword(self, password):
        self._password = password

    # getter for admin status
    def getIsadmin(self):
        return self._isadmin

    # setter for admin status
    def setIsadmin(self, isadmin):
        self._isadmin = isadmin