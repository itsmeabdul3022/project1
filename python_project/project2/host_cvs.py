import pandas as pd

# Step 1: Read the CSV file into a pandas DataFrame
# Replace 'your_csv_file.csv' with your file's name
try:
    df = pd.read_csv('Test_L2.csv')
except FileNotFoundError:
    print("Error: The file was not found. Please check the file name and path.")
    exit()

# Step 2: Extract the first word and remove the starting double quote
# Replace 'YourColumnName' with the name of the column you want to analyze
try:
    df['first_word'] = df['Host'].astype(str).str.split().str[0].str.lstrip('"')
except KeyError:
    print("Error: The specified column was not found. Please check the column name.")
    exit()

# Step 3: Count the occurrences of each first word
word_counts = df['first_word'].value_counts()

# Step 4: Print all unique first words
unique_words = word_counts.index
print("All Unique First Words:")
print(unique_words)

print("\n" + "="*40 + "\n")

# Step 5: Filter and print only the duplicate words with their counts
duplicates = word_counts[word_counts > 1]

if not duplicates.empty:
    print("Duplicate First Words and Their Counts:")
    print(duplicates.to_string())
else:
    print("No duplicate first words were found.")
