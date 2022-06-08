from src.db_operations import add_user
import argparse
from werkzeug.security import generate_password_hash

def main():
    '''Register user account via command line.'''
    parser = argparse.ArgumentParser(description="Register Admin account to send notification emails from it.")
    parser.add_argument("--username", "-U", required=True, help="Username to log in with.")
    parser.add_argument("--email", "-E", required=True, help="This email will be used to send notification emails from.")
    parser.add_argument("--password", "-P", required=True, help="Password to log in with.")
    args = parser.parse_args()

    username = args.username
    email = args.email
    password = generate_password_hash(args.password)

    add_user(username, email, password, 0)

if __name__ == "__main__":
    main()
