import pandas as pd

# Step 1: Read the CSV file into a pandas DataFrame
# Replace 'your_csv_file.csv' with your file's name and 'YourColumnName' with your column header
try:
    df = pd.read_csv('Test_L2.csv')
    column_name = 'Description'
except FileNotFoundError:
    print("Error: The file was not found. Please check the file name and path.")
    exit()
except KeyError:
    print("Error: The specified column was not found. Please check the column name.")
    exit()

# Step 2: Use a regular expression to extract the text between the first double quotes
# The pattern r'"(.*?)"' finds any characters (.*) between a pair of double quotes (")
# The parentheses () create a 'capturing group' so only the content inside is returned.
df['extracted_text'] = df[column_name].astype(str).str.extract(r'"(.*?)"')

# Step 3: Print the original column and the new column with the extracted text
print(df[['extracted_text']].to_string())

# You can also save the new data to a CSV file if needed:
# df.to_csv('output2.csv', index=False)

# Step 4: Count the occurrences of each extracted line
# This will count all unique values, including those with a count of 1.
line_counts = df['extracted_text'].value_counts()

# Step 5: Print the results
print("Line counts (includes both duplicates and unique lines):")
print(line_counts.to_string())