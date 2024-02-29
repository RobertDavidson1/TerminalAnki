import os
import time

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')


def countdown(initial_message : str,action : str,i=0):
    if i != 3:
        clear_terminal()  # Clear the terminal at the beginning of each call
        print(f"{initial_message}")
        print(f"{action.capitalize()} in {3 - i}...")
        time.sleep(1)  # Wait for 1 second
        
        countdown(initial_message, action, i+1)

    clear_terminal()
        


