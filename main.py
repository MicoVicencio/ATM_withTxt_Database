
# Import necessary modules
from person import Person  # Importing the Person class from the person module
from load import loading,loading_atm  # Importing the loading function from the load module
from atm import ATM

atm = ATM()
# Simulate a loading animation with a duration of 3 seconds
loading(1)

def choices():
     print("Choose an option:")
     print("1. Log in as User 1")
     print("2. Log in as User 2")
     print("3. Log in as User 3")
     print("4. Log in as User 4")
     print("5. Log in as User 5")
     print("0. Exit")
     
def choose_person():
    while True:
        choices()
        choice = input("Enter which object do you want:")
        if choice == "1":
            person1 = Person()
            person1.current_user = 1
            loading(1)
            person1.welcome_Intro()
            
        elif choice == "2":
            person2 = Person()
            person2.current_user = 2
            loading(1)
            person2.welcome_Intro()
            
        elif choice == "3":
            person3 = Person()
            person3.current_user = 3
            loading(6)
            person3.welcome_Intro()
            
        elif choice == "4":
            person4 = Person()
            person4.current_user = 4
            loading(6)
            person4.welcome_Intro()
            
        elif choice == "5":
            person5 = Person()
            person5.current_user = 5
            loading(6)
            person5.welcome_Intro()
        elif choice == "0":
            print("Exiting.......")
            loading_atm(4)
            break
            
        else:
            print("Invalid Choice! Try again!")
            
choose_person()
            
