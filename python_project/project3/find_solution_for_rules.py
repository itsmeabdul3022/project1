import pandas as pd
import re
import os

def extract_solution(description):
    """
    Extracts the solution and command lines from a given description string.
    """
    if pd.isna(description) or not isinstance(description, str):
        return None

    # Regex to find 'Solution:' section and capture all lines until the next section header
    # or the end of the string. The 're.DOTALL' flag allows '.' to match newlines.
    match = re.search(r'Solution:\s*(.*?)(?:\n\n|\Z)', description, re.IGNORECASE | re.DOTALL)
    if match:
        solution_section = match.group(1).strip()
        # Split the section into individual lines
        solution_lines = [line.strip() for line in solution_section.split('\n') if line.strip()]
        return solution_lines
    return None

def process_rules(file_a_path, file_b_path, output_path):
    """
    Reads rules from file_a, searches for them in file_b, and saves the solutions to a new file.
    """
    try:
        df_a = pd.read_excel(file_a_path)
        df_b = pd.read_excel(file_b_path)
    except FileNotFoundError as e:
        print(f"Error: One of the input files was not found. Please check the file paths. {e}")
        return
    except Exception as e:
        print(f"An error occurred while reading the Excel files: {e}")
        return

    output_data = []

    # Iterate through each rule in the first file
    for index, row in df_a.iterrows():
        rule = str(row['Rule']).strip()
        print(f"Searching for rule: {rule}")

        # Find the row in file_b where the description contains the rule
        matching_rows = df_b[df_b['Description'].str.contains(r'\b' + re.escape(rule) + r'\b', case=False, na=False)]

        if not matching_rows.empty:
            description = matching_rows.iloc[0]['Description']
            solution_lines = extract_solution(description)

            if solution_lines:
                for line in solution_lines:
                    output_data.append({'Rule': rule, 'Solution': line})
            else:
                output_data.append({'Rule': rule, 'Solution': 'No "Solution:" section found.'})
        else:
            output_data.append({'Rule': rule, 'Solution': 'Rule not found in file_b.'})

    # Create a new DataFrame and save it to an Excel file
    output_df = pd.DataFrame(output_data)
    try:
        output_df.to_excel(output_path, index=False)
        print(f"\nSuccessfully created the output file at: {output_path}")
    except Exception as e:
        print(f"An error occurred while writing the output file: {e}")

if __name__ == "__main__":
    file_a = 'CIS_RULES.xlsx'
    file_b = 'CIS-Enterprise-Scan-Level-1_2--AIX.xlsx'
    output_file = 'CIS_RULES_solutions_output.xlsx'
    
    # Ensure your files are in the same directory as this script, or provide their full paths.
    process_rules(file_a, file_b, output_file)