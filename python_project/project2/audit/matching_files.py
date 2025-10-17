import re

def process_files(file_a_path, file_b_path, matching_output_path, unique_output_path):
    """
    Compares lines from two files, replaces a value based on a match, and writes
    the matching lines to one file and the unique lines to another.

    Args:
        file_a_path (str): The path to the first input file (file_a).
        file_b_path (str): The path to the second input file (file_b).
        matching_output_path (str): The path for the output file with matching lines.
        unique_output_path (str): The path for the output file with unique lines.
    """

    # Regex patterns
    pattern_a = re.compile(r'description\s*:\s*"[\d.]+\s*(.*?)"')
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
    except FileNotFoundError:
        print(f"Error: The file '{file_b_path}' was not found.")
        return

    # Process file_a and write to both output files
    try:
        with open(file_a_path, 'r') as f_a, \
             open(matching_output_path, 'w') as matching_out, \
             open(unique_output_path, 'w') as unique_out:
            
            for line in f_a:
                match = pattern_a.search(line)
                if match:
                    other_data = match.group(1).strip().lower()

                    # Check for a match
                    if other_data in file_b_data:
                        new_dotted_number = file_b_data[other_data]
                        new_line = f'description : "{new_dotted_number} {match.group(1).strip()}"\n'
                        matching_out.write(new_line)
                    else:
                        # Write to the unique file if no match is found
                        unique_out.write(line)
    except FileNotFoundError:
        print(f"Error: The file '{file_a_path}' was not found.")
process_files('CIS_IBM_AIX_7_v1.0.0_L1_CUSTOM_TEST3142025.audit', 'cis_rules.txt', 'CIS_IBM_AIX_7_v1.0.0_L1_CUSTOM_TEST3142025.audit.matching.out', 'CIS_IBM_AIX_7_v1.0.0_L1_CUSTOM_TEST3142025.audit.unique.out')