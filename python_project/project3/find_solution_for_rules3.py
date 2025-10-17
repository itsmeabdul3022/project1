import pandas as pd
import re
import os


def extract_solution_and_command(description):
    """
    Extracts the first line after 'Solution:' as the description
    and all subsequent lines as commands.
    """
    if pd.isna(description) or not isinstance(description, str):
        return None, None
    
    # New regex: captures everything after 'Solution:' until the next known section header
    match = re.search(r'Solution:\s*(.*?)(?=\n\s*See Also:|\n\s*Reference:|\n\s*Policy Value:|\n\s*Actual Value:|\Z)', description, re.IGNORECASE | re.DOTALL)
    
    if match:
        solution_section = match.group(1).strip()
        lines = [line.strip() for line in solution_section.split('\n') if line.strip()]

        if not lines:
            return "No description found.", "No command found."

        # The first line is the description
        solution_description = lines[0]

        # The rest of the lines are the commands
        solution_command = "\n".join(lines[1:])
        
        # If there are no other lines, the command is empty
        if not solution_command:
            solution_command = "No command found."
            
        return solution_description, solution_command
    
    return None, None

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
    except KeyError as e:
        print(f"Error: A required column was not found. Please check the column names in your Excel files. {e}")
        return
    except Exception as e:
        print(f"An error occurred while reading the Excel files: {e}")
        return

    output_data = []

    for index, row in df_a.iterrows():
        try:
            rule = str(row['Rule']).strip()
        except KeyError:
            print("Error: 'Rule' column not found in file_a. Please check the column name.")
            return

        print(f"Searching for rule: {rule}")

        try:
            matching_rows = df_b[df_b['Description'].str.contains(r'\b' + re.escape(rule) + r'\b', case=False, na=False)]
        except KeyError:
            print("Error: 'Description' column not found in file_b. Please check the column name.")
            return

        if not matching_rows.empty:
            description = matching_rows.iloc[0]['Description']
            solution_description, solution_command = extract_solution_and_command(description)

            if solution_description or solution_command:
                output_data.append({
                    'Rule': rule,
                    'Solution_Description': solution_description if solution_description else 'No description found.',
                    'Solution_Command': solution_command if solution_command else 'No command found.'
                })
            else:
                output_data.append({
                    'Rule': rule,
                    'Solution_Description': 'No solution section found.',
                    'Solution_Command': ''
                })
        else:
            output_data.append({
                'Rule': rule,
                'Solution_Description': 'Rule not found in file_b.',
                'Solution_Command': ''
            })

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
    output_file = 'CIS_RULES_solutions_output4.xlsx'
    
    process_rules(file_a, file_b, output_file)