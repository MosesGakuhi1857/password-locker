import random
import string

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