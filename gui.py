import tkinter as tk
from tkinter import Label,Button,messagebox,Entry,Listbox
from datetime import datetime

class GUI:
    def __init__(self,
                 username="",
                 password="",
                 balance=0.00,
                 current_user=1,
                 user_info={},
                 message ="",
                 status = None,
                 transactions = None
                 ):
        self.transactions = transactions
        self.transactions = {}
        self.status = status
        self.userName = username
        self.password = password
        self.balance = balance  # Private variable with double underscores
        self.current_user = current_user
        self.user_info = user_info
        self.attempt = 1
        self.message = message
        # Paths for storing user data
        self.paths = ["user_data1.txt", "user_data2.txt", "user_data3.txt", "user_data4.txt", "user_data5.txt"]
        
        self.root = tk.Tk()
        self.root.geometry("285x340")
        self.root.title("Object Instantiation")
        self.root.config(bg="#222831")
        self.label_title = Label(self.root, text="ATM Object Interface", font=("Arial", 20),foreground="#EEEEEE",bg="#222831")
        self.label_description = Label(self.root, text="Choose a Person to Login", font=("Arial", 10,"bold"),foreground="#EEEEEE",bg="#222831")

        self.button_person1 = Button(self.root, text="Person 1",foreground="#EEEEEE",bg="#222831",command=lambda: self.update_current_user(1))
        self.button_person2 = Button(self.root, text="Person 2",foreground="#EEEEEE",bg="#222831",command=lambda: self.update_current_user(2))
        self.button_person3 = Button(self.root, text="Person 3",foreground="#EEEEEE",bg="#222831",command=lambda: self.update_current_user(3))
        self.button_person4 = Button(self.root, text="Person 4",foreground="#EEEEEE",bg="#222831",command=lambda: self.update_current_user(4))
        self.button_person5 = Button(self.root, text="Person 5",foreground="#EEEEEE",bg="#222831",command=lambda: self.update_current_user(5))


        self.label_title.grid(row=0, column=0, padx=10, pady=10)
        self.label_description.grid(row=1, column=0, padx=10, pady=10)
        self.button_person1.grid(row=2, column=0, padx=10, pady=10)
        self.button_person2.grid(row=3, column=0, padx=10, pady=10)
        self.button_person3.grid(row=4, column=0, padx=10, pady=10)
        self.button_person4.grid(row=5, column=0, padx=10, pady=10)
        self.button_person5.grid(row=6, column=0, padx=10, pady=10)
    
    def login_form(self):
        global login_form
        login_form = tk.Toplevel(self.root)
        login_form.title("Login Interface")
        login_form.geometry("250x180")
        login_form.config(bg="#222831")
        log_title = Label(login_form,text="Login your Account!",foreground="#EEEEEE",bg="#222831")
        user_label = Label(login_form,text="Username:",foreground="#EEEEEE",bg="#222831")
        pass_label = Label(login_form,text="Password:",foreground="#EEEEEE",bg="#222831")
        self.l_user_entry = Entry(login_form,bg="#A1AEB1")
        self.l_pass_entry = Entry(login_form,show="*",bg="#A1AEB1")
        log_button = Button(login_form,text="Login",foreground="#EEEEEE",bg="#222831",command=lambda: self.credentials_verify('1'))
        
        log_title.grid(row=0,column=1,padx=10,pady=10)
        user_label.grid(row=1,column=0,padx=0,pady=10)
        pass_label.grid(row=2,column=0,padx=0,pady=10)
        self.l_user_entry.grid(row=1,column=1,padx=0,pady=10)
        self.l_pass_entry.grid(row=2,column=1,padx=0,pady=10)
        log_button.grid(row=3,column=1,padx=10,pady=5)
        
    def credentials_verify(self,value):
        if value == '1':
          user_input = self.l_user_entry.get()
          pass_input = self.l_pass_entry.get()
          if self.userName == user_input and self.password == pass_input:
              self.msg_box('2')
              login_form.destroy()
              self.atm_ui()
          else:
              self.msg_box('3')
              login_form.destroy()
              self.login_form()
              
        if value == '2':
          user_input = self.c_user_entry.get()
          pass_input = self.c_pass_entry.get()
          self.userName = user_input
          self.password = pass_input
          self.save_user_data()
          messagebox.showinfo("Account","Account Creation Complete! Proceeding to Login Form")
          create_form.destroy()
          self.login_form()
          
    def save_user_data(self):
        # Save user data based on current_user value
        if self.current_user >= 1 and self.current_user <= 5:
            with open(f"user_data{self.current_user}.txt", "w") as file:
                file.write(f"Username:{self.userName}\n")
                file.write(f"Password:{self.password}\n")
                file.write(f"Current Balance:{self.balance}\n")        
      
    def create_acc(self):
        global create_form
        create_form = tk.Toplevel(self.root)
        create_form.title("Account Creation")
        create_form.config(bg="#222831")
        create_form.geometry("260x180")
        log_title = Label(create_form,text="Create your Account!",foreground="#EEEEEE",bg="#222831")
        user_label = Label(create_form,text="Username:",foreground="#EEEEEE",bg="#222831")
        pass_label = Label(create_form,text="Password:",foreground="#EEEEEE",bg="#222831")
        self.c_user_entry = Entry(create_form,bg="#A1AEB1")
        self.c_pass_entry = Entry(create_form,show="*",bg="#A1AEB1")
        create_button = Button(create_form,text="Create Account",foreground="#EEEEEE",bg="#222831",command=lambda: self.credentials_verify('2'))
        
        log_title.grid(row=0,column=1,padx=10,pady=10)
        user_label.grid(row=1,column=0,padx=0,pady=10)
        pass_label.grid(row=2,column=0,padx=0,pady=10)
        self.c_user_entry.grid(row=1,column=1,padx=0,pady=10)
        self.c_pass_entry.grid(row=2,column=1,padx=0,pady=10)
        create_button.grid(row=3,column=1,padx=10,pady=5)
        
    def atm_ui(self):
        global atm_functions
        atm_functions = tk.Toplevel(self.root)
        atm_functions.title("ATM Functions")
        atm_functions.config(bg="#222831")
        atm_functions.geometry("275x160")   
        title = Label(atm_functions,text="Choose Functionalities",foreground="#EEEEEE",bg="#222831",font=("Arial",10))
        deposit_button = Button(atm_functions,text = "Deposit Money",foreground="#EEEEEE",bg="#222831",command=self.deposit)
        withdraw_button = Button(atm_functions,text="Withdraw Money",foreground="#EEEEEE",bg="#222831",command=self.withdraw)
        balance_button = Button(atm_functions,text="Check Balance",foreground="#EEEEEE",bg="#222831",command=self.check_balance)
        transactions_button = Button(atm_functions,text="View Transactons",foreground="#EEEEEE",bg="#222831",command=self.view_transaction_history)
        
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        deposit_button.grid(row=1,column=0,padx=20,pady=10)
        withdraw_button.grid(row=1,column=1,padx=20,pady=10)
        balance_button.grid(row=2,column=0,padx=10,pady=10)
        transactions_button.grid(row=2,column=1,padx=10,pady=10)
        
    def deposit(self):
        atm_functions.destroy()
        global depo
        depo = tk.Toplevel(self.root)
        depo.title("Deposit")
        depo.config(bg="#222831")
        dep_label = Label(depo,text="Money to Deposit:",bg="#222831",foreground="#EEEEEE")
        self.dep_entry = Entry(depo)
        dep_button = Button(depo,text="Confirm",command=self.deposit_process,bg="#222831",foreground="#EEEEEE")
        dep_label.grid(row = 0,column=0,padx=10,pady=10)
        self.dep_entry.grid(row=0,column=1,padx=10,pady=10)
        dep_button.grid(row=1,column=1,padx=10,pady=10)
    def deposit_process(self):
        d_money = self.dep_entry.get()
        value = float(d_money)
        msg = f"Do you want to deposit {value} pesos?"
        confirmation = messagebox.askyesno("Deposit Confirmation",msg)
        if confirmation:
            try:
              if value <= 0:
                  messagebox.showinfo("Notice","Please enter valid amount!")
                  depo.destroy()
                  self.atm_ui()
            except ValueError:
                  messagebox.showwarning("Notice","Please enter numbers")
                  depo.destroy()
                  self.atm_ui()
                  
            self.balance += value
            self.add_transaction("Deposit",value)  
            self.save_user_data()    
            update = f"You successfully deposit {value} pesos!"
            messagebox.showinfo("Notice",update)      
            depo.destroy()      
            
            self.atm_ui()
        else:
            msg = f"Depositing {value} pesos is cancelled!"
            messagebox.showinfo("Notice",msg)
            depo.destroy()
            self.atm_ui()
            
    def check_balance(self):
        atm_functions.destroy()
        current_money = self.balance
        msg = f"Your current Balance is {current_money} pesos."
        messagebox.showinfo("Notice",msg)
        self.atm_ui()
        
            
        
        
    def withdraw(self):
        atm_functions.destroy()
        global withdraw
        withdraw = tk.Toplevel(self.root)
        withdraw.title("Withdraw")
        withdraw.config(bg="#222831")
        withdraw_label = Label(withdraw,text="Money to withdraw:",bg="#222831",foreground="#EEEEEE")
        self.withdraw_entry = Entry(withdraw)
        withdraw_button = Button(withdraw,text="Confirm",command=self.withdraw_process,bg="#222831",foreground="#EEEEEE")
        withdraw_label.grid(row = 0,column=0,padx=10,pady=10)
        self.withdraw_entry.grid(row=0,column=1,padx=10,pady=10)
        withdraw_button.grid(row=1,column=1,padx=10,pady=10) 
        
        
    def withdraw_process(self):  
        w_money = self.withdraw_entry.get()
        value = float(w_money)
        msg = f"Are you sure you want to withdraw {value} pesos?" 
        confirm = messagebox.askyesno("Withdrawal Confirmation",msg) 
        if confirm:
            if value <= 0:
              messagebox.showinfo("Notice","Invalid Amount! Try again.")
              withdraw.destroy()
              self.atm_ui()
            
            elif value > self.balance:
              update = f"You Don't have {value} pesos on your current balance! Try again."
              messagebox.showinfo("Notice",update)    
              withdraw.destroy()
              self.atm_ui()
              
            else:  
              self.balance -= value
              self.add_transaction("Withdraw",value)
              update = f"You successfully withdraw {value} pesos!"
              messagebox.showinfo("Notice",update)
              self.save_user_data()
              withdraw.destroy()
              self.atm_ui()
        else:
            update = f"Withdrawing {value} cancelled!"
            messagebox.showinfo("Notice",update)
            withdraw.destroy()
            self.atm_ui()
            
        
            
        
    def run(self):
        self.root.mainloop()
        
    def update_current_user(self,value):
        self.current_user = value
        self.msg_box('1')
        
    def msg_box(self,value):
        if value == '1':
          message = "Do you want to recover the old account?"
          promp = messagebox.askyesno("Recovering old Account?",message)
          if promp:
              messagebox.showinfo("Recovering Data!","Please Wait...")
              self.check_file_content()
              if self.status == True:
                 messagebox.showinfo("No data Found!","Make a Account First!")
                 self.create_acc()
              else:
                self.back_data()
                self.userName = self.user_info['Username']
                self.password = self.user_info['Password']
                self.balance = float(self.user_info['Current Balance'])  
                messagebox.showinfo("Data Recovered!","Going to Login Form.")
                self.login_form()    
          else:
              messagebox.showinfo("Entering Account Creation Form.","Click OK.")
              self.new_account()
              self.create_acc()
        if value == '2':
            messagebox.showinfo("Login","Loging in.. Please Wait") 
        if value == '3':
            messagebox.showinfo("Login","Username and Password Incorrect. Please try again")    
               
    def back_data(self):
        # Load user data based on current_user value
        if self.current_user >= 1 and self.current_user <= 5:
            with open(f"user_data{self.current_user}.txt", 'r') as file:
                for line in file:
                    key, values = line.strip().split(":")
                    self.user_info[key] = values
                file.close()  
                
    def new_account(self):
        # Create a new account based on the current_user value
        if self.current_user >= 1 and self.current_user <= 5:
            with open(self.paths[self.current_user - 1], 'w') as file:
                file.write(f"Username:{self.userName}\n")
                file.write(f"Password:{self.password}\n")
                file.write(f"Current Balance: {0.00}\n")
                
    def check_file_content(self):
        try:
            # Check if the specified file exists and if it's empty
            if self.current_user >= 1 and self.current_user <= 5:
                with open(self.paths[self.current_user - 1], 'r') as file:
                    file_content = file.read()
                    # Check if the file content is empty
                    lines = file_content.strip().split('\n')
                    # Check if the file has at least three lines (Username, Password, and Balance)
                    if len(lines) < 3:
                      self.status = True
                
                    username_line = lines[0].strip()
                    password_line = lines[1].strip()
                    # Check if both Username and Password lines are blank
                    if username_line == 'Username:' and password_line == 'Password:':
                       self.status = True
                    else:
                      self.status = False
                    
        except FileNotFoundError:
            return "The specified file does not exist."
        
    def add_transaction(self, transaction_type, amount):
        self.back_data()
        now = datetime.now()  # Get the current date and time
        transaction_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format the current date and time
        # Store the transaction details in the transactions dictionary
        self.transactions[transaction_time] = {'type': transaction_type, 'amount': amount}
        # Update the balance for the current transaction
        self.transactions[transaction_time]['balance'] = self.balance
        
        

    # Method to view the transaction history
    def view_transaction_history(self):
        global trans
        trans = tk.Toplevel(self.root)
        trans.geometry("480x210")
        trans.config(bg="#222831")
        trans.title("Transaction History")
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time = Label(trans,text="Current Time :"+current_time,bg="#222831",foreground="#EEEEEE")
        trans_list = Listbox(trans,height=10,width=75,bg="#222831",foreground="#EEEEEE")
        if not self.transactions:  # Check if there are no transactions
            print("No transactions yet.")
        else:
            print("Transaction History:")
            # Iterate over each transaction in the transactions dictionary
            for transaction_time, details in self.transactions.items():
                if 'balance' in details:  # Check if balance information is available for the transaction
                    # Print transaction details with balance information
                    msg = f"{transaction_time}: {details['type']} {details['amount']} pesos - Current Balance: {details['balance']} pesos"
                    trans_list.insert(tk.END,msg)
                else:
                    # Print transaction details without balance information
                    print(transaction_time + ": " + details['type'] + " " + str(details['amount']) + " pesos")
        trans_list.grid(row=0,column=0,padx=10,pady=10)
        time.grid(row=1,column=0,padx=10,pady=0)
s = GUI()
s.run()
