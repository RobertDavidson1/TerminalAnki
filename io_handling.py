import csv
import os
import pandas as pd
import glob
from helpers import countdown, clear_terminal
import sys


def prompt_file_name():
    directory = "flashcards"
    file_name = input("\nEnter file name (press enter to exit) > ").strip()


    if file_name:
        return directory, file_name
    else:
        return directory, False

def initialise_csv():
    directory, file_name = prompt_file_name()

    if not file_name:
        return "No file name provided."

    full_path = os.path.join(directory, file_name + ".csv") 

    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        return f"An error occurred while creating the directory: {e}"

    if not os.path.exists(full_path): 
        rows = ["front", "back"]
        print(f"\nCreating {file_name} in {directory}...")

        try:
            with open(full_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(rows)
                return f"File {file_name} created successfully.\n"
        except IOError as e:
            return f"An error occurred while writing the file: {e}"

    else:
        return f"File {file_name}.csv already exists."

def list_csv():
    directory = "flashcards"
    search_pattern = os.path.join(directory, '*.csv')
    csv_files = glob.glob(search_pattern)
    file_names = [os.path.basename(file) for file in csv_files]


    if len(file_names) >= 1:
        clear_terminal()
        print("\n--Files found --")
        for file in file_names:
            print(file)

        print()

        return True
    
    return False


def load_csv():

    if list_csv() != True:
        return f"No files in 'flashcards' directory, please create one first", None

    directory, file_name = prompt_file_name()

    if not file_name:
        return "No file name provided.", None
    



    full_path = os.path.join(directory, file_name + ".csv") 

    if os.path.exists(full_path): 
        return f"{file_name}.csv loaded successfully.\n", pd.read_csv(full_path)
    else:
        return f"File {file_name}.csv does not exist.", None


def rename_or_delete_csv():

    if list_csv() != True:
        return f"No files in 'flashcards' directory, please create one first"

    directory, file_name = prompt_file_name()

    if not file_name:
        return "No file name provided."

    full_path = os.path.join(directory, file_name + ".csv") 

    if not os.path.exists(full_path): 
        return f"File {file_name}.csv doesn't exist."

    print("1. Rename")
    print("2. Delete")
    choice = input("Enter 1 or 2 >").strip()

    if choice == '1':
        new_file_name = input("Enter the new file name: ").strip()
        new_full_path = os.path.join(directory, new_file_name + ".csv")

        if os.path.exists(new_full_path):
            return f"Cannot rename: File {new_file_name}.csv already exists."

        try:
            os.rename(full_path, new_full_path)
            return f"File renamed to {new_file_name}.csv successfully."
        except OSError as e:
            return f"Error renaming file: {e}"
    elif choice == '2':
        try:
            os.remove(full_path)
            return f"File {file_name}.csv deleted successfully."
        except OSError as e:
            return f"Error deleting file: {e}"
    else:
        return "Invalid choice. Please enter 1 or 2."



def main_csv_handling():
    
    while True:
        print("1. Load a CSV")
        print("2. Create a CSV")
        print("3. Rename or Delete a CSV")
        
        choice = input("\nEnter 1, 2 or 3 > ")

        if choice == "1":
            message, df = load_csv()
            countdown(message, "Returning")
            if df is not None:
                return df
        elif choice == "2":
            countdown(initialise_csv(), "Returning")
        elif choice == "3":
            clear_terminal()
            countdown(rename_or_delete_csv(), "Returning")
        
        else:
            countdown("Invalid input", "Exiting")
            sys.exit()

