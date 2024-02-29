import pandas as pd
from io_handling import csv_file_menu
from sm2 import ask_question





if __name__ == "__main__":
    df = csv_file_menu()
    df['Next Review Date'] = pd.to_datetime(df['Next Review Date'])  # Ensure correct datetime format
    try:
        if ask_question(df):
            print("All cards reviewed for today!")
        print("Saving progress...")
        df.to_csv('flashcards.csv', index=False)
        print("Progress saved. Exiting flashcards.")
    except KeyboardInterrupt:
        print("\nSession interrupted. Saving progress...")
        df.to_csv('flashcards.csv', index=False)
        print("Progress saved. Goodbye!")