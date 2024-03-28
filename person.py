from atm import ATM  # Importing the ATM class frobalancem the atm module
from load import loading, loading_atm  # Importing the loading functions from the load module
import sys

# Define the Person class
class Person:
    atm = ATM()
    max_login_attempts = 3  # Maximum number of login attempts allowed
    login_attempts = 0  # Initialize login attempts counter
    
    # Constructor to initialize a Person object with optional parameters
    def __init__(self, userName=None, password=None, balance=0.00,current_user = 0,user_info={}):
        # Create an instance of the ATM class
        self.userName = userName
        self.password = password
        self.__balance = balance # Private variable with double underscores
        self.current_user = current_user
        self.user_info = user_info
        self.attempt = 1
        self.paths = ["user_data5.txt","user_data5.txt","user_data5.txt","user_data5.txt,user_data5.txt","user_data5.txt"]

    # Getter method for retrieving the balance
    def get_balance(self):
        return self.__balance

    # Setter method for updating the balance
    def set_balance(self, new_balance):
        self.__balance = new_balance

    # Method to login to the account
    def login_account(self):
        while self.login_attempts < self.max_login_attempts:
            input_username = input("Enter Username:")
            input_password = input("Enter Password:")
            
            if input_username == self.userName and input_password == self.password:
                loading(2)  # Display loading animation for 2 seconds
                self.account_Functions()  # Call account functions after successful login
                break
            else:
                self.login_attempts += 1
                remaining_attempts = self.max_login_attempts - self.login_attempts
                print("Invalid username or password.", remaining_attempts, "attempts remaining.")
        
        else:
            print("Max login attempts reached. Exiting program.")
            sys.exit()  # Exit the program after reaching the maximum login attempts

    # Method to withdraw money from the account
    def withdraw(self):
        try:
            w_amount = int(input("Enter how much money you want to withdraw: "))
            if w_amount <= 0:
                print("Invalid amount. Please enter a positive integer.")
                self.account_Functions()
            elif w_amount > self.get_balance():
                print("You don't have enough balance to withdraw that amount.")
                self.account_Functions()
            else:
                new_balance = self.get_balance() - w_amount
                self.set_balance(new_balance)
                self.atm.add_transaction("Withdraw", w_amount)
                loading_atm(3)  # Display loading animation for ATM operations for 3 seconds
                print("You withdrew", w_amount, "pesos!")
                print("Current Balance:", self.get_balance(), "pesos")
                self.save_user_data()
                self.account_Functions()
        except ValueError:
            print("Invalid input. Please enter a valid integer amount.")
            self.account_Functions()

    # Method to check the balance
    def check_Balance(self):
        loading_atm(1)  # Display loading animation for ATM operations for 1 second
        print("Your Current Balance is", self.get_balance(), "pesos")
        self.save_user_data()
        self.account_Functions()

    # Method to deposit money into the account
    def deposit(self):
        while True:
            try:
                d_amount = int(input("Enter how much money you want to deposit: "))
                if d_amount <= 0:
                    raise ValueError("Invalid amount. Please enter a positive integer.")
                break
            except ValueError as e:
                print("Error:", e)
        
        new_balance = self.get_balance() + d_amount
        self.set_balance(new_balance)
        self.atm.add_transaction("Deposit", d_amount)
        loading_atm(2)  # Display loading animation for ATM operations for 2 seconds
        print("You deposited", d_amount, "pesos!")
        print("Current Balance:", self.get_balance(), "pesos")
        self.save_user_data()
        self.account_Functions()
        
    def back_data(self):
        
        if self.current_user == 1:
            with open("user_data1.txt",'r') as file:
                for line in file:
                    key,values = line.strip().split(":")
                    self.user_info[key] = values
            file.close()
          
        elif self.current_user == 2:
            with open("user_data2.txt",'r') as file:
                for line in file:
                    key,values = line.strip().split(":")
                    self.user_info[key] = values
            file.close()  
        
        elif self.current_user == 3:
            with open("user_data3.txt",'r') as file:
                for line in file:
                    key,values = line.strip().split(":")
                    self.user_info[key] = values
            file.close()  
        
        elif self.current_user == 4:
            with open("user_data4.txt",'r') as file:
                for line in file:
                    key,values = line.strip().split(":")
                    self.user_info[key] = values
            file.close()  
          
        elif self.current_user == 5:
            with open("user_data5.txt",'r') as file:
                for line in file:
                    key,values = line.strip().split(":")
                    self.user_info[key] = values
            file.close()  
          
    # Method to display the welcome message and options
    def welcome_Intro(self):
        self.atm.current_user = self.current_user
        print("""
        **********************************************
        *                                            *
        *         Welcome to ATM Simulation!         *
        *                                            *
        *  Please select an option:                  *
        *  1. Create account                         *
        *  2. Login                                  *
        *  3. Exit                                   *
        *                                            *
        **********************************************
        """)
        while True:
            if self.attempt == 1:
               load = input("Do you want to login your previous account?(y/n)")
               self.attempt = 0
               if load == 'y':
                  if self.check_file_content() == False:
                    self.back_data()
                    self.userName = self.user_info['Username']
                    self.password = self.user_info['Password']
                    self.balance = self.set_balance((float(self.user_info['Current Balance'])))
                  else:
                      print("There is no previous account!")
            else:
                break
        while True:   
          option = input("Enter option: ")    
          if option == "1":
              if self.userName is None:
                  self.userName = input("Enter Username:")
                  self.password = input("Enter Password:")
                  loading(5)  # Display loading animation for 5 seconds
                  self.welcome_Intro()  # Restart the welcome intro
              else:
                  print("You already created an Account!")
                  new_accounts = input("Do you want to create new account?: (y/n)")
                  if new_accounts == "y":
                      self.new_account()
                      self.userName = input("Enter Username:")
                      self.password = input("Enter Password:")
                      loading(5)  # Display loading animation for 5 seconds
                      print(self.userName)
                      self.welcome_Intro()
                  else:
                    print("Log In now!")
                    self.welcome_Intro
          elif option == "2":
              if self.userName is None:
                   print("Create Account First!")
                   self.welcome_Intro()
              else:
                  self.login_account()
                
          elif option == "3":
              print("Exiting...") 
              self.save_user_data()
              loading_atm(4)  # Display loading animation for ATM operations for 4 seconds
              sys.exit() #Exit program
          else:
             print("Invalid option.")   
                    
    def new_account(self):
        if self.current_user == 1:
          with open(self.paths[0],'w') as file:
              file.write(f"Username:{""}\n")
              file.write(f"Password:{""}\n")
              file.write(f"Current Balance: {0.00}\n")
              
        elif self.current_user == 2:
          with open(self.paths[1],'w') as file:
              file.write(f"Username:{""}\n")
              file.write(f"Password:{""}\n")
              file.write(f"Current Balance: {0.00}\n")
        
        elif self.current_user == 3:
          with open(self.paths[2],'w') as file:
              file.write(f"Username:{""}\n")
              file.write(f"Password:{""}\n")
              file.write(f"Current Balance: {0.00}\n")
              
        elif self.current_user == 4:
          with open(self.paths[3],'w') as file:
              file.write(f"Username:{""}\n")
              file.write(f"Password:{""}\n")
              file.write(f"Current Balance: {0.00}\n")
              
        elif self.current_user == 5:
          with open(self.paths[4],'w') as file:
              file.write(f"Username:{""}\n")
              file.write(f"Password:{""}\n")
              file.write(f"Current Balance: {0.00}\n")
        
    # Method to display account functions menu
    def account_Functions(self):
        print("""
        **********************************************
        *                                            *
        *  Options:                                  *
        *  1. Check Balance                          *
        *  2. Deposit                                *
        *  3. Withdraw                               *
        *  4. View Transaction History               *
        *  5. Exit                                   *
        *                                            *
        **********************************************
        """)
        while True:
            choice = input("Please enter your choice (1-5): ")

            if choice == '1':
                self.check_Balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.atm.view_transaction_history()
                self.account_Functions()
            elif choice == '5':
                print("Exiting...")
                self.welcome_Intro()
            else:
                print("Invalid choice. Please try again.")
                
                
                
    def save_user_data(self):
        if self.current_user == 1:
          with open("user_data1.txt", "w") as file:
              file.write(f"Username:{self.userName}\n")
              file.write(f"Password:{self.password}\n")
              file.write(f"Current Balance:{self.get_balance()}\n")
              
        elif self.current_user == 2:
          with open("user_data2.txt", "w") as file:
              file.write(f"Username:{self.userName}\n")
              file.write(f"Password:{self.password}\n")
              file.write(f"Current Balance: {self.get_balance()}\n")
              
        elif self.current_user == 3:
          with open("user_data3.txt", "w") as file:
              file.write(f"Username:{self.userName}\n")
              file.write(f"Password:{self.password}\n")
              file.write(f"Current Balance: {self.get_balance()}\n")
        
        elif self.current_user == 4:
          with open("user_data4.txt", "w") as file:
              file.write(f"Username:{self.userName}\n")
              file.write(f"Password:{self.password}\n")
              file.write(f"Current Balance: {self.get_balance()}\n")
              
        elif self.current_user == 5:
          with open("user_data5.txt", "w") as file:
              file.write(f"Username:{self.userName}\n")
              file.write(f"Password:{self.password}\n")
              file.write(f"Current Balance: {self.get_balance()}\n")
              
    def check_file_content(self):
      try:
        
        if self.current_user == 1:
          with open(self.paths[0], 'r') as file:
            file_content = file.read()
            # Check if the file content is empty
            if not file_content.strip():
                return True
            else:
                return False
            
        elif self.current_user == 2:
          with open(self.paths[1], 'r') as file:
            file_content = file.read()
            # Check if the file content is empty
            if not file_content.strip():
                return True
            else:
                return False
        elif self.current_user == 3:
          with open(self.paths[2], 'r') as file:
            file_content = file.read()
            # Check if the file content is empty
            if not file_content.strip():
                return True
            else:
                return False
        
        elif self.current_user == 4:
          with open(self.paths[3], 'r') as file:
            file_content = file.read()
            # Check if the file content is empty
            if not file_content.strip():
                return True
            else:
                return False
        
        elif self.current_user == 5:
          with open(self.paths[4], 'r') as file:
            file_content = file.read()
            # Check if the file content is empty
            if not file_content.strip():
                return True
            else:
                return False
            
      except FileNotFoundError:
        return "The specified file does not exist."


