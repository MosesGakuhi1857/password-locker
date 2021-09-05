# import pyperclip
from user import User
from credentials import Credentials


def create_user(myusername,loginpass):
    """
    Function to create a new user's account
    """
    new_user = User(myusername,loginpass)
    return new_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user()
    
def verify_user(login_username,password):
    """
    function that verifies user's credentials
    """
    checking_user = Credentials.check_user(login_username,password)
    return checking_user

def generate_newpassword():
    """
    function to generate password
    """
    gen_pass = Credentials.generate_newpassword()
    return gen_pass

def create_credentials(socialM,username,passcode):
    """
    Function to add a new social media's credentials
    """
    new_credentials = Credentials(socialM,username,passcode)
    return new_credentials

def save_credentials(credentials):
    """
    Function to save user's credentials
    """
    credentials.save_credentials()
    
    
def display_credentials(socialM):
    """
    Function that returns all the saved credentials
    """
    return Credentials.display_credentials(socialM)

def copy_credential (socialM):
    """
    Function to copy credentials
    """
    return Credentials.copy_credential(socialM)

def main():
    print(' ')
    print("Hello Welcome to Password Locker.")