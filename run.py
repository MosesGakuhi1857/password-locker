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



def main():
    print(' ')
    print("Hello Welcome to Password Locker.")
    
    
    
    
    while True:
        print( " ")
        print("."*40)
        print("Kindly use the short codes: \n cc=create a new account on password locker, \n log = to login, \n dlt= To delete the credentials, \n dc = to display the credentials list, \n ex = exit")
        
        short_code = input ("Choose a short code: ").lower().strip()
        
        if short_code == "ex":
            break
        
        elif short_code == "cc":
            print("."*35)
            print(" ")
            print("Create a new account:")
            login_username = input ("Input the username:").strip()
            password = input ("Input the password not less than 9 characters and must have an uppercase and lowercase characters with both letters and numbers: =>").strip()
            save_user(create_user(login_username,password))
            print (f"New user created for: {login_username} using password: {password} ")
        
        
        
        elif short_code == "log":
        
            print("."*30)
            print(" ")
            print("to login enter your account details:")
            login_username = (input ("Enter your username :"))
            password = str(input("Enter your password :"))
            user_exist = verify_user(login_username,password)
            if user_exist == login_username:
                print(" ")
                print(f"Welcome {login_username} .Please choose any option to  continue.")
                print(" ")
            
                while True:
                     print("_"*40)
                     print('to navigate to account use code:\n sm = to add a social media account, \n dc = to display accounts \n dlt = to delete \n ex- Exit')
                     short_code=input('Enter a choice: ').lower().strip()
                     print("_"*40)
                     if short_code =='ex':
                         print(' ')   
                         print(f'Thank you! {login_username}.')
                         break

                     elif short_code == 'dlt':

                         print("_"*40)
                         print(' ')
                         print('Successfully Deleted!')
                         break
                     elif short_code =='sm':
                         print(' ')
                         print('Enter your account name: ')
                         socialM = input('enter the the social media\'s name:  ').strip() 
                         username = input('enter your account\'s username:  ').strip()
                            
                            
                         while True:
                             print(' ')
                             print("_"*50)
                             print("please enter the choose for entering password for your account: \n pwd = enter existing password \n gp-generate a new password \n del- delete \n ex- Exit")
                             opt_choice = input('Enter an option: ').lower().strip()
                             print("-"*80)
                             if opt_choice == 'pwd':
                                 print(" ")
                                 passcode = input('enter your password: ').strip()
                                 break
                                
                             elif short_code == 'del':
                                 print("_"*80)
                                 print(' ')
                                 print('Successfully Deleted!')
                                 break
                                
                             elif opt_choice == 'gp':
                                 password = generate_newpassword()
                                 break
                             elif opt_choice == 'ex':
                                 break
                             else:
                                 print('Try Again!.')
                         save_credentials(create_credentials(socialM,username,passcode))
                         print(' ')
                         print(f'Account Created: Name:  {socialM}, userName:{username}, Password:{passcode}')
                         print(' ')
                     elif short_code == 'dc':
                         print(' ')
                         if display_credentials(socialM):
                             print('Here is a list of all accounts')
                             print(' ')
                             for account in display_credentials(socialM):
                                 print(f'social media name: {credentials.socialM} - username: {credentials.username} - Password: {credentials.passcode}')
                                 print(' ')
                             else:
                                 print(' ')
                                 print("you don't seem to have any account")
                                 print(' ')
                    
                         
                         else: 
                             print('TRY Again')
                        
                        
                
                else:
                    print(' ')
                    print('TRY Again or create another account.')

                 
         
        else:
                print("_"*40)
                print(' ')
                print("try Again")
                
                
                
                

if __name__ == '__main__':

    main()
    