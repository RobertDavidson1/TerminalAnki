import csv
import os

def get_new_csv_file_name() -> tuple[str, str, str]:
    # Prompt for directory name, use 'topics' as default
    directory_name = input('Enter Directory (press enter for default) > ')
    if directory_name == '':
        directory_name = 'topics'

    # Ensure directory exists
    try:
        os.makedirs(directory_name, exist_ok=True)
    except OSError as e:
        print(f"An error occurred while creating the directory: {e}")
        return "", "", ""

    # Loop until valid file name enter
    while True:
        file_name = input('Enter file name > ')
        if file_name: # If file name entered (not empty)
            full_path = os.path.join(directory_name, file_name + '.csv') 
            if not os.path.exists(full_path): # break if a csv with that file name does not exist
                break
            else: # else prompt the user
                print(f"The file {file_name}.csv already exists in the directory {directory_name}.\n")
        else: # if no file name enter, continue loop
            print('Please enter a valid file name\n')

    return file_name + '.csv', directory_name, full_path


def write_new_csv(file_name, directory_name, full_path) -> None:
    rows: list[str] = ['Front', 'Back'] # rows to addpend to csv
    
    try:
        print(f"\nCreating {file_name} in {directory_name}...")
        with open(full_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(rows)
            print(f"File {file_name} created successfully.")
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")


def create_new_csv() -> None:
    file_name, directory_name, full_path = get_new_csv_file_name()
    if file_name:  # Check if file_name is not empty
        write_new_csv(file_name, directory_name, full_path)



create_new_csv()