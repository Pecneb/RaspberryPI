import smtplib, ssl
import sys

'''
Module for sending emails. __init__ takes sender email, 
the subject of the email (title), the message,
then the receiver email / emails in an array.

The standart port for SSL is 465.
The standart email service is smtp.gmail.com.
'''
class email(object):

    # init email
    def __init__(self, from_email, title, message, to_emails=[]) -> None:
        self._from_email = from_email
        self._title = title
        self._message = message
        self._to_emails = to_emails
        self._password = "initpass"
        self._port = 0
        self._service = "smtp.gmail.com"

    # get sender email
    def getSender(self) -> str:
        return self._from_email

    # set sender email
    def setSender(self, sender : str):
        try:
            self._from_email = str(sender)
        except ValueError:
            # Handle tyope exeption
            print("Bad email type!")

    # get receivers
    def getReceivers(self):
        return self._to_emails

    # set receiver / receivers
    def setRecievers(self, recievers=[]):
        try:
            self._to_emails = [str(reciever) for reciever in recievers]
        except ValueError:
            # Handle type exeption
            print("Bad email type!")

    def getTitle(self):
        return self._title

    def setTitle(self, title):
        if len(title) == 0 or len(title) <= 100:
            self._title = title
        else:
            print("Title must be <= 100 chars!")

    def getMessage(self):
        return self._message

    def setMessage(self, message):
        self._message = message

    def sendmail(self):
        # sends mail with SSL
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self._service, self._port, context) as server:
            server.login(self._from_email, self._password)
            finalMessage = f'''\
            Subject: {self._title}

            {self._message}
            '''
            server.sendmail(self._from_email, self._to_emails, finalMessage)