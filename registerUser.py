from src.db_operations import add_user
import sys

def main():
    '''Register user account via command line.'''
    parser = argparse.ArgumentParser(description="Register Admin account to send notification emails from it.")
    parser.add_argument("--username", "-U", help="Optional agrument. Default is Administrator", default="Administrator")
    parser.add_argument("--email", "-E", required=True, help="This email will be used to send notification emails from.")
    args = parser.parse_args()

    username = args.username
    email = args.email

    add_user(username, email, "placeholder", 0)

if __name__ == "__main__":
    main()