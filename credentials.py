import random
import string
import pyperclip

class Credentials:
    """
    class that generates new instances of credentials instances
    """
    
    credentials_list = []
    user_credentials_list = []
    
    @classmethod
    def check_user(cls,login_username,password):
        """
        method that checks if the name and password matches
        """
        current_user = ''
        for user in User.user_list:
            if(user.login_username == login_username and user.password == password):
                current_user = user.login_username
        return current_user
    
    
    def __init__(self,socialM,username,passcode):
        
        self.socialM = socialM
        self.username = username
        self.passcode = passcode
        
    def save_credentials(self):
        
        """
        save_credentials method saves credentials objects into credentials_list
        """
        
        Credentials.credentials_list.append(self)
        
    def generate_newpassword(size=9,char=string.ascii_uppercase + string.ascii_lowercase + string.hexdigits):
        """
        function to generate new password
        """
        gen_pass = ''.join(random.choice(char)for _ in range(size))
        return gen_pass
    
    @classmethod
    def display_credentials(cls,socialM):
        """
        method that returns the account list
        """
        
        user_credentials_list= []
        for credentials in cls.credentials_list:
            
            user_credentials_list.append(credentials)
        return user_credentials_list
    
    def delete_credentials(self):
        
        """
        delete credentials method deletes saved credentials
        """
        
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_by_socialM(cls,socialM):
        """
        Method that takes in a social media's and returns an account that matches the socialmedia name
        """
        for Credentials in cls.credentials_list:
            if Credentials.socialM == socialM:
                return Credentials
            
    @classmethod
    def copy_credential(cls,socialM):
        """
        class method that copies credential's info after the account's social media's name is entered
        """
        
        find_credentials = Credentials.find_by_socialM(socialM)
        return pyperclip.copy(find_credentials.passcode)