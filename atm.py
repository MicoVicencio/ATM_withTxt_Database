import datetime
from load import loading_atm

# Define the ATM class
class ATM:
    # Constructor to initialize an ATM object with optional transactions parameter
    def __init__(self, transactions=None,current_user = 0,user_info = {},balance = 0):
        self.user_info = user_info
        if transactions is None:
           transactions = {}  # If transactions are not provided, initialize as an empty dictionary
        self.transactions = transactions  # Store transactions in the ATM object
        self.current_user = current_user
        self.balance = balance # Initialize the balance to zero
        
    def back_data(self):
        if self.current_user == 1:
          with open("user_data1.txt",'r') as file:
              for line in file:
                  key,values = line.strip().split(":")
                  self.user_info[key] = values
          file.close()
          self.balance = (float(self.user_info['Current Balance']))
        
        elif self.current_user == 2:
          with open("user_data2.txt",'r') as file:
              for line in file:
                  key,values = line.strip().split(":")
                  self.user_info[key] = values
          file.close()
          self.balance = (float(self.user_info['Current Balance']))
          
        elif self.current_user == 3:
          with open("user_data3.txt",'r') as file:
              for line in file:
                  key,values = line.strip().split(":")
                  self.user_info[key] = values
          file.close()
          self.balance = (float(self.user_info['Current Balance']))
          
        elif self.current_user == 4:
          with open("user_data4.txt",'r') as file:
              for line in file:
                  key,values = line.strip().split(":")
                  self.user_info[key] = values
          file.close()
          self.balance = (float(self.user_info['Current Balance']))
          
        elif self.current_user == 5:
          with open("user_data5.txt",'r') as file:
              for line in file:
                  key,values = line.strip().split(":")
                  self.user_info[key] = values
          file.close()
          self.balance = (float(self.user_info['Current Balance']))
          
    # Method to add a transaction to the ATM
    def add_transaction(self, transaction_type, amount):
        self.back_data()
        now = datetime.datetime.now()  # Get the current date and time
        transaction_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format the current date and time
        # Store the transaction details in the transactions dictionary
        self.transactions[transaction_time] = {'type': transaction_type, 'amount': amount}
        # Update the balance based on the transaction type
        if transaction_type == 'Deposit':
            self.balance += amount  # Add the amount to the balance for deposit transactions
        elif transaction_type == 'Withdraw':
            self.balance -= amount  # Subtract the amount from the balance for withdrawal transactions

        # Update the balance for the current transaction
        self.transactions[transaction_time]['balance'] = self.balance

    # Method to view the transaction history
    def view_transaction_history(self):
        if not self.transactions:  # Check if there are no transactions
            loading_atm(5)  # Display loading animation for ATM operations for 5 seconds
            print("No transactions yet.")
        else:
            loading_atm(5)  # Display loading animation for ATM operations for 5 seconds
            print("Transaction History:")
            # Iterate over each transaction in the transactions dictionary
            for transaction_time, details in self.transactions.items():
                if 'balance' in details:  # Check if balance information is available for the transaction
                    # Print transaction details with balance information
                    print(transaction_time + ": " + details['type'] + " " + str(details['amount']) + " pesos - Current Balance: " + str(details['balance']) + " pesos")
                else:
                    # Print transaction details without balance information
                    print(transaction_time + ": " + details['type'] + " " + str(details['amount']) + " pesos")
