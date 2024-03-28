import sys
import time

# Function to simulate a loading animation for general operations
def loading(duration):
    animation = "|/-\\"  # Characters used for the loading animation
    delay = 0.1  # Time delay between each animation frame
    elapsed_time = 0  # Variable to track elapsed time

    # Loop until elapsed_time reaches the specified duration
    while elapsed_time < duration:
        for char in animation:
            sys.stdout.write(f'\rLoading {char} ')  # Write loading animation to stdout
            sys.stdout.flush()  # Flush stdout to show the animation immediately
            time.sleep(delay)  # Delay before showing the next animation frame
            elapsed_time += delay  # Update elapsed_time based on the delay

    sys.stdout.write('\r')  # Move cursor to the beginning of the line
    # Display different messages based on the duration of the loading process
    if duration == 3:
        sys.stdout.write('Loading Complete!\n')
    elif duration == 5:
        sys.stdout.write('Account Creation Complete!\n')
    elif duration == 2:
        sys.stdout.write('Login Successful!\n')
        sys.stdout.write('Choose Functions!\n')
    elif duration == 6:
        sys.stdout.write('Person Initialization Complete!\n')
    sys.stdout.flush()  # Flush stdout to show the final message

# Function to simulate a loading animation for ATM operations
def loading_atm(duration):
    animation = "|/-\\"  # Characters used for the loading animation
    delay = 0.1  # Time delay between each animation frame
    elapsed_time = 0  # Variable to track elapsed time

    # Loop until elapsed_time reaches the specified duration
    while elapsed_time < duration:
        for char in animation:
            sys.stdout.write(f'\rLoading {char} ')  # Write loading animation to stdout
            sys.stdout.flush()  # Flush stdout to show the animation immediately
            time.sleep(delay)  # Delay before showing the next animation frame
            elapsed_time += delay  # Update elapsed_time based on the delay

    sys.stdout.write('\r')  # Move cursor to the beginning of the line
    # Display different messages based on the duration of the loading process
    if duration == 1:
        sys.stdout.write('Inquiring Balance Complete!\n')
    elif duration == 2:
        sys.stdout.write('Depositing Money Complete!\n')
    elif duration == 3:
        sys.stdout.write('Withdrawing Money Complete!\n')
    elif duration == 5:
        sys.stdout.write('Retrieving Recent Transaction Complete!\n')
    elif duration == 4:
        sys.stdout.write('Closing Program Complete!\n')
    elif duration == 6:
        sys.stdout.write('Closing Object Complete!\n')
    sys.stdout.flush()  # Flush stdout to show the final message
