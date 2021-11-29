from src.db_operations import add_user
import sys
import argparse

def main():
    '''Register admin account via command line.'''
    parser = argparse.ArgumentParser(description="Register Admin account to send notification emails from it.")
    parser.add_argument("--username", "-U", help="Optional agrument. Default is Administrator", default="Administrator")
    parser.add_argument("--email", "-E", required=True, help="This email will be used to send notification emails from.")
    parser.add_argument("--password", "-P", required=True, help="Password of the email account. The program have to access the account to send emails.")
    args = parser.parse_args()

    username = args.username
    email = args.email
    password = args.password

    add_user(username, email, password, 1)

if __name__ == "__main__":
    main()