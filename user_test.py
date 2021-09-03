import unittest #importing the unittest module
from user import User #importing the User class

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
        self.assertEqual(len(User.user_list),1)
        
if __name__ == '__main__':
    unittest.main()