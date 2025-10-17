import pandas as pd

# Step 1: Read the Excel file into a pandas DataFrame
# Replace 'your_excel_file.xlsx' with your file's name
try:
    df = pd.read_excel('your_excel_file.xlsx')
except FileNotFoundError:
    print("Error: The file was not found. Please check the file name and path.")
    exit()

# Step 2: Extract the first word from each cell in the specified column
# Replace 'YourColumnName' with the name of the column you want to analyze
try:
    df['first_word'] = df['YourColumnName'].astype(str).str.split().str[0]
except KeyError:
    print("Error: The specified column was not found. Please check the column name.")
    exit()

# Step 3: Count the occurrences of each first word
word_counts = df['first_word'].value_counts()

# Step 4: Filter to find duplicates (counts greater than 1)
duplicates = word_counts[word_counts > 1]

# Step 5: Print the results as a new DataFrame
if not duplicates.empty:
    print("Duplicate First Words and Their Counts:")
    print(duplicates.to_string())
else:
    print("No duplicate first words were found.")
