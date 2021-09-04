import random
import string

class Credentials:
    """
    class that generates new instances of credentials instances
    """
    
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