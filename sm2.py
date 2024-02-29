import pandas as pd
import datetime



def review_card(row, quality):
    if quality < 3:
        repetitions = 0
        interval = 1
    else:
        repetitions = row['Repetitions'] + 1
        if repetitions == 1:
            interval = 1
        elif repetitions == 2:
            interval = 6
        else:
            interval = round(row['Interval'] * row['Ease Factor'])

    ease_factor = max(1.3, row['Ease Factor'] + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    next_review_date = pd.to_datetime('today') + pd.Timedelta(days=interval)
    
    return repetitions, interval, ease_factor, next_review_date

def ask_question(df):
    for index, row in df.iterrows():
        print(f"Question: {row['Question']}")
        input("Press any key to see the answer...")
        print(f"Answer: {row['Answer']}")
        quality = input("Rate the ease of recall from 0 (hardest) to 5 (easiest), or type 'quit flashcards' to exit: ")
        if quality.lower() == 'quit flashcards':
            return False  # Stop asking questions
        try:
            quality = int(quality)
            if quality < 0 or quality > 5:
                print("Invalid input. Please enter a number between 0 and 5.")
                continue
            update_data = review_card(row, quality)
            df.loc[index, ['Repetitions', 'Interval', 'Ease Factor', 'Next Review Date']] = update_data
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 5 or 'quit flashcards'.")
            continue
    return True


