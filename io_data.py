import csv
import os
import pandas as pd
import glob


def get_new_csv_file_name() -> tuple[str, str, str]:
    """
    Prompts the user to input a directory and a file name to create a new CSV file. 
    
    This function first asks for a directory name, defaulting to "flashcards" if none is provided.
    It ensures the specified directory exists, creating it if necessary. Then, it repeatedly prompts
    for a file name until a non-existing CSV file name is entered within the specified (or default) directory.
    
    If the directory cannot be created due to an OS error, it prints an error message and returns empty strings.
    If the specified CSV file already exists, it prompts again for a different file name. This process continues
    until a valid, non-existing file name is provided by the user.
    
    Parameters:
    None

    Returns:
    tuple[str, str, str]: A tuple containing three strings:
        - The first string is the new CSV file name with the ".csv" extension.
        - The second string is the directory name where the file will be located.
        - The third string is the full path to the new file.
    """

    # Prompt for directory name, use "flashcards" as default if input is empty
    
    directory_name = "flashcards"

    # Try to create the specified directory (if it doesn't exist), handle OS errors if any
    try:
        os.makedirs(directory_name, exist_ok=True)
    except OSError as e:
        print(f"An error occurred while creating the directory: {e}")
        return "", "", ""

    # Loop to prompt for a valid file name
    while True:
        file_name = input("Enter the name of topic (no spaces) > ")
        # Check if a file name was entered
        if file_name:
            # Construct the full path for the new file
            full_path = os.path.join(directory_name, file_name + ".csv") 
            # If the file does not already exist, break out of the loop
            if not os.path.exists(full_path): 
                break 
            else: 
                # Inform the user that the file already exists and prompt for a different name
                print(f"The file {file_name}.csv already exists in the directory {directory_name}.\n")
        else:

            return "", "", ""


    return file_name + ".csv", directory_name, full_path


def write_new_csv(file_name, directory_name, full_path) -> None:
    """
    Creates a new CSV file at the specified full path and writes initial rows to it.
    
    This function attempts to create a new CSV file with the provided name in the given directory.
    It then writes a predefined set of rows to the file. If an error occurs during file creation or writing,
    it prints an error message.
    
    Parameters:
    - file_name (str): The name of the CSV file to be created.
    - directory_name (str): The directory where the CSV file will be created.
    - full_path (str): The full path where the CSV file will be created and written to.
    
    Returns:
    None
    """

    # Predefined rows to be written to the CSV file
    rows: list[str] = ["front", "back"] 
    
    try:
        # Inform the user about the file creation process
        print(f"\nCreating {file_name} in {directory_name}...")
        
        # Open the file for writing. If it doesn't exist, it will be created.
        with open(full_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(rows)
            print(f"File {file_name} created successfully.\n")
            
    
    # Print an error message if an IOError occurs during the file operation
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")


def create_new_csv() -> None:
    """
    Facilitates the creation of a new CSV file by first prompting the user for file details and then writing to it.
    
    This function calls `get_new_csv_file_name` to interactively get the new CSV file's name, directory, and full path.
    If a valid file name is obtained (i.e., not an empty string), it proceeds to call `write_new_csv` to actually create
    the file and write initial content to it.
    
    Parameters:
    None
    
    Returns:
    None
    """

    # Get the new CSV file name, directory, and full path from the user
    file_name, directory_name, full_path = get_new_csv_file_name()
    print(file_name)
    # Ensure a valid file name was provided before proceeding
    if file_name != "":
        # Create the CSV file and write initial content to it
        write_new_csv(file_name, directory_name, full_path)
    else:
        return False


def list_csv() -> list[str]:
    """
    Lists all CSV file names in the specified folder without their directory paths.

    Returns:
    - list[str]: A list of CSV file names found in the specified folder.
    """

    directory_name = "flashcards"

    # Construct the search pattern to match all CSV files in the folder
    search_pattern = os.path.join(directory_name, '*.csv')
    
    # Use glob.glob to find all files matching the search pattern
    csv_files = glob.glob(search_pattern)
    
    # Extract just the file names from the full paths
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

    