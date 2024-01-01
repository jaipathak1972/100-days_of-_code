import pandas as pd

# Read the NATO phonetic alphabet data from the CSV file
Data = pd.read_csv(r"Day26\NATO-alphabet-start\nato_phonetic_alphabet.csv")

# Get the user's name and convert it to uppercase
user_name = input("What's your name: ").upper()

# Create a dictionary to store the NATO codes
nato_dict = {row['letter']: row['code'] for index, row in Data.iterrows()}

# Use list comprehension to convert the name to NATO codes
nato_codes = [f"{letter}: {nato_dict[letter]}" if letter in nato_dict else f"No NATO code found for: {letter}" for letter in user_name]

# Print the NATO codes
for code in nato_codes:
    print(code)
