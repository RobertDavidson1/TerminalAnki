import csv
import os
import pandas as pd
import glob


def get_new_csv_file_name() -> tuple[str, str, str]:

    directory_name = "flashcards"
    
    try:
        os.makedirs(directory_name, exist_ok=True)
    except OSError as e:
        print(f"An error occurred while creating the directory: {e}")
        return "", "", ""
  
    while True:
        file_name = input("Enter the name of topic (no spaces) > ")       
        if file_name:
            full_path = os.path.join(directory_name, file_name + ".csv") 
            if not os.path.exists(full_path): 
                break 
            else: 
                print(f"The file {file_name}.csv already exists in the directory {directory_name}.\n")
        else:
            return "", "", ""


    return file_name + ".csv", directory_name, full_path


def write_new_csv(file_name, directory_name, full_path) -> None:
    rows: list[str] = ["front", "back"] 
    try:
        print(f"\nCreating {file_name} in {directory_name}...")
        with open(full_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(rows)
            print(f"File {file_name} created successfully.\n")
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")


def create_new_csv() -> None:
    file_name, directory_name, full_path = get_new_csv_file_name()
    print(file_name)
    if file_name != "":
        write_new_csv(file_name, directory_name, full_path)
    else:
        return False


def list_csv() -> list[str]:
    directory_name = "flashcards"
    search_pattern = os.path.join(directory_name, '*.csv')
    csv_files = glob.glob(search_pattern)
    file_names = [os.path.basename(file) for file in csv_files]
    
    return file_names


def load_csv() -> pd.DataFrame | None:
    
    directory_name =  "flashcards"
    while True:
        file_name: str = input("\nEnter file name (press enter to exit) > ")

        if not file_name:
            return None
        
        full_path: str = os.path.join(directory_name, file_name) 
        if os.path.exists(full_path): 
            print(f"{file_name} loaded succesfully\n")
            return pd.read_csv(full_path)
        else: 
            print(f"The file {file_name}.csv was not found in the directory {directory_name}.\n")
            user_continue = input("Try again? [Y/n] > ")

            if user_continue.lower() != 'y':
                return None

    