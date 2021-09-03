class User:
    """
    class that generates new instances of user information
    """
    
    def __init__(self,login_username,password):
        
        self.login_username=login_username
        self.password=password
    
   
    user_list = [] #Empty user list
    
    def save_user(self):
        
        """
        save_user method saves user credentials objects into user_list
        """
        
        User.user_list.append(self)