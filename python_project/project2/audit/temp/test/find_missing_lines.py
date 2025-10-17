import re
import json

def process_files(file_a_path, file_b_path):
    """ print the dictionary key and values based on the search criteria"""
    # Regex patterns
    pattern_b = re.compile(r'description\s*:\s*"([\d.]+)\s*(.*?)"')
    # Dictionary to store 'some_otherdata' and its corresponding dotted number from file_b
    file_b_data = {}
    try:
        with open(file_b_path, 'r') as f_b:
            for line in f_b:
                match = pattern_b.search(line)
                if match:
                    dotted_number = match.group(1).strip()
                    other_data = match.group(2).strip().lower()
                    file_b_data[other_data] = dotted_number
        print("Contents of file_b_data dictionary (JSON format):")
        print(json.dumps(file_b_data, indent=2))            
    except FileNotFoundError:
        print(f"Error: The file '{file_b_path}' was not found.")
    try:
        with open(file_a_path, 'r') as f_a, \
             open(matching_output_test1, 'w') as matching_out, \
             open(unique_output_test1, 'w') as unique_out:
            
            for line in f_a:
                match = pattern_a.search(line)
                if match:
                    other_data = match.group(1).strip().lower()

                    # Check for a match
                    if other_data in file_b_data:
                        new_dotted_number = file_b_data[other_data]
                        new_line = f'description : "{new_dotted_number} {match.group(1).strip()}"\1 n'
                        matching_out.write(new_line)
                    else:
                        # Write to the unique file if no match is found
                        unique_out.write(line)
    except FileNotFoundError:
        print(f"Error: The file '{file_a_path}' was not found.")           
process_files('test1.txt', 'test2.txt')

    
