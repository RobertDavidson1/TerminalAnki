import pandas as pd
from io_data import create_new_csv, load_csv, list_csv
from helpers import clear_terminal, countdown



def initial_prompt():
    
    while True:
        print("1. Load topic")
        print("2. Create new topic\n")

        choice: str = input("Enter 1 or 2 > ")

        if choice == '1':
            clear_terminal()
            csv_files: list[str] = list_csv()

            if csv_files:
                print("\nCurrent Topics:")
                for csv in csv_files:
                    print(csv)

            
                df = load_csv()
                if df is not None:
                    pass
                else:
                    countdown("Failed to load the specified file.")
            else:
                countdown("No topic files found - Please create a topic first")
                
        elif choice == '2':
            clear_terminal()
            if create_new_csv() == False:
                countdown("No file name entered")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    






initial_prompt()