class Greeting:
    '''Used for handling greeting the user'''
    def __init__(self):
        self.new_user = False
        self._input_recieved = False
        self.login_token = False
        self.register_token = False

    def welcome_msg(self):
        '''Greets the user and prompts to ask if they are a new or existing user'''

        while not self._input_recieved:
            user_type = input("Welcome to PyLogin!\nIf you are a new user type: 'Register'\
                \nIf you are an existing user type: 'Login'\n\n...")
            print("")
            if user_type.lower() == 'register':
                self.new_user = True
                self._input_recieved = True
                self.register_token = True
            elif user_type.lower() == 'login':
                self._input_recieved = True
                self.login_token = True
            else:
                print("I'm sorry, that was an invalid input. Please try again.\n")

    def welcome_new_user(self):

        print("Welcome! Please enter a new username that does not begin with a number or special character and is not an empty string.\
            Then enter a password that is at least 8 characters long and contains one upper and lower case letter and one digit:\n")

    def welcome_back(self):

        print("Welcome back! Please provide your username and password:\n")

class RegisterUser:
    '''For non-registered users'''

    def __init__(self):
        self.valid_username = False
        self.unique_user = False
        self._username = ""
        self._password = ""
        self.valid_password = False

    def enter_username(self):

        print("*"*10+"REGISTER USERNAME"+"*"*10+"\n")
        self._username = input("USERNAME: ")
        print("")

    def enter_password(self):

        print("*"*10+"REGISTER PASSWORD"+"*"*10+"\n")
        self._password = input("PASSWORD: ")
        print("")
    
    def username_valid(self):
        '''returns false if username starts with a number or special character'''
        from string import digits, punctuation

        if self._username == "":
            print("Username cannot be empty!")
        elif self._username[0] in digits or self._username[0] in punctuation:
            print("Username cannot begin with a number or a special character!\n")
        else:
            self.valid_username = True

    def username_unique(self):
        '''Checks if the entered username already exists'''

        file_path = "D:\\Documents\\Python\\LoginSystem\\user_pass.txt"

        my_file = open(file_path)
        my_str = my_file.read()
        my_file.close()
        my_str = my_str.split()

        if self._username not in my_str:
            self.unique_user = True
        else:
            print("Username already exists. Please choose another.\n")

    def password_valid(self):
        '''Returns true if the entered password is at least 8 characters long 
        and contains at least one upper and lowercase letter and at least one digit'''

        from string import ascii_lowercase, ascii_uppercase, digits

        lower_count = upper_count = digit_count = 0

        if len(self._password) > 7:
            for char in self._password:
                lower_count += ascii_lowercase.count(char)
                upper_count += ascii_uppercase.count(char)
                digit_count += digits.count(char)
            if lower_count > 0 and upper_count > 0 and digit_count > 0:
                self.valid_password = True
            else:
                print("Password must contain at least one upper and lowercase letter and at least one digit.\n")
        else:
            print("Password must be at least 8 characters long.\n")

    def log_new_user(self):
        '''Appends the valid username and password to user_pass.txt'''

        file_path = "D:\\Documents\\Python\\LoginSystem\\user_pass.txt"

        my_file = open(file_path,'a')
        my_file.write(self._username+"\n")
        my_file.write(self._password+"\n\n")

class LoginUser:
    '''For registered users'''

    def  __init__(self):
        self._username = ""
        self._password = ""
        self.login_success = False
    
    def enter_username(self):

        print("*"*10+"LOGIN USERNAME"+"*"*10+"\n")
        self._username = input("USERNAME: ")
        print("")

    def enter_password(self):

        print("*"*10+"LOGIN PASSWORD"+"*"*10+"\n")
        self._password = input("PASSWORD: ")
        print("")

    def check_user_pass(self):
        '''Checks if the provided username and password are in the database'''

        file_path = "D:\\Documents\\Python\\LoginSystem\\user_pass.txt"

        my_file = open(file_path)
        my_str = my_file.read()
        my_file.close()

        user_pass_regex = self._username+"\n"+self._password+"\n\n"

        if user_pass_regex in my_str:
            self.login_success = True
        else:
            print("The provided username and password are invalid or do not exist.")




if __name__ == "__main__":
    
    greeter = Greeting() # Create an instance of the Greeting class
    greeter.welcome_msg() # Check if the user is new or existing

    if greeter.register_token:
        # Welcome the new user
        greeter.welcome_new_user()

        # Create an instance of the RegisterUser class
        new_user = RegisterUser()

        # While the new username is invalid or already taken prompt the user to create a new username
        while not new_user.valid_username or not new_user.unique_user:
            new_user.enter_username()
            new_user.username_valid() # Check to see if the entered username is valid
            new_user.username_unique() # Check to see if the entered username is in the database already

        # While the new password is invalid prompt the user to create a new password
        while not new_user.valid_password:
            new_user.enter_password()
            new_user.password_valid()

        new_user.log_new_user() # Add the now valid username and password to database "user_pass.txt"
        print("NEW USER REGISTERED!\n")

    if greeter.login_token:
        # Welcome the existing user
        greeter.welcome_back()

        # If the user already exists, create an instance of the LoginUser class
        exist_user = LoginUser()

        # While the login details do not match any in the database, repeat the login process
        while not exist_user.login_success:
            exist_user.enter_username()
            exist_user.enter_password()
            exist_user.check_user_pass()
        
        print("LOGIN SUCCESS!\n")
