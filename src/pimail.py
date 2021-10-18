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
    def __init__(self, from_email, title, message, port=None,
                 service=None , password=None, to_emails=[]) -> None:
        """
        __init__ takes a source email address, the message title,
        the message itself, port and service is only optional, and the recipients mail addresses
        """
        self._from_email = from_email
        self._title = title
        self._message = message
        self._to_emails = to_emails
        if password != None:
            self._password = password
        else:
            self._password = "initpass"
        if port != None:
            self._port = port
        else:
            self._port = 587
        if service != None: 
            self._service = service
        else:
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

    def getPort(self):
        return self._port

    def setPort(self, port):
        self._port = port

    def getService(self):
        return self._service

    def setService(self):
        self._service

    def sendmail_SSL(self):
        """
        Send mail securely via SSL.
        """
        context = ssl.create_default_context()
        try:
            server = smtplib.SMTP(self._service, self._port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(self._from_email, self._password)
            finalMessage = f'''\
            Subject: {self._title}

            {self._message}
            '''
            server.sendmail(self._from_email, self._to_emails, finalMessage)
        except Exception as e:
            print(e)
        finally:
            server.quit()

    def sendmail(self):
        """
        Send mail in plain text.
        """
        with smtplib.SMTP(self._service, self._port) as server:
            finalMessage = f'''\
            Subject: {self._title}

            {self._message}
            '''
            server.sendmail(self._from_email, self._to_emails, finalMessage)
