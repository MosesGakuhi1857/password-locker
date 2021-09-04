import unittest #importing the unittest module
from user import User #importing the User class
from credentials import Credentials #importing the credentials class

class TestUser(unittest.TestCase):
    
    """
    Test class that defines test cases for the user behaviours
    
    Args:
        unittest.TestCase : TestCase class that helps in creating test cases
    """
    
    def setUp(self):
        
        """
        set up method to run before each test cases.
        """
        
        self.new_user = User ("MoseKings","baroda") #create user object
        
    def test_init(self):
        
        """
        test init test case to test if the object is intialiazed properly
        """
        
        self.assertEqual(self.new_user.login_username,"MoseKings")
        self.assertEqual(self.new_user.password,"baroda")
        
        
    def test_save_user(self):
        """
        test_save_user test case to test if the contact object is saved into the password locker
        """
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),2)
        
    def test_delete_user(self):
        
        """
        test_delete_user to test if we can remove a user credentials from user_list
        """
        self.new_user.save_user() 
        test_user = User("Mosekings","baroda")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

class testCredentials(unittest.TestCase):
    
    """
    Test class that defines test cases for the credential class behaviours.
    
    Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    """
    
    def test_check_user(self):
        
        """
        Function to test whether the login in function check_user works properly
        """
        self.new_user = User ("Mosekings","baroda")
        self.new_user.save_user()
        user2 = User('maloly',"muxah")
        user2.save_user()
        
        for user in User.user_list:
            if user.login_username == user2.login_username and user.password == user2.password:
                current_user= user.login_username
        return current_user
        
        self.assertEqual(current_user,Credentials.check_user(user2.login_username,user2.password))
        
    def setUp(self):
        """
        Set up method to run before test cases
        """
        self.new_credentials = Credentials("twitter","Musakings","baroda")
        
        
        self.assertEqual(self.new_credentials.socialM,"twitter")
        self.assertEqual(self.new_credentials.username,"Musakings")
        self.assertEqual(self.new_credentials.passcode,"baroda")
        
    def test_save_credentials(self):
        """
        
        """    
           
        self.new_credentials.save_credentials()
        instagram = Credentials("instagram","kings","musa") 
        instagram.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credentials.credentials_list = []
        User.user_list = []
        
    def test_display_credentials(self):
        """
        method that returns a list of all credentials saved
        """
        instagram = Credentials("instagram","kings","musa") 
        instagram.save_credentials()
        facebook = Credentials ("facebook","maloly","kings")
        facebook.save_credentials()
        self.assertEqual(len(Credentials.display_credentials(instagram.socialM)),2)
        
    def test_find_by_socialM(self):
        """
        test to check if the find_by_social media method returns the correct credentials
        """
        
        self.new_credentials.save_credentials()
        instagram = Credentials("instagram","kings","musa") 
        instagram.save_credentials()
        credentials_exist= Credentials.find_by_socialM("instagram")
        self.assertEqual(credentials_exist,instagram)
        
        
        
        
if __name__ == '__main__':
    unittest.main()
    