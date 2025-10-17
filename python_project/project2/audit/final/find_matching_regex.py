import re
import os

def sort_key_by_dotted_number(line):
    """
    Custom sorting key to handle dotted numbers.
    It splits the number into parts and converts them to integers for correct sorting.
    """
    match = re.search(r'"([\d.]+)', line)
    if match:
        dotted_number = match.group(1)
        return [int(part) for part in dotted_number.split('.')]
    return []

def find_and_count_matching_lines(filepath, regex_pattern):
    """
    Finds and counts all unique lines in a file that match a given regular expression.

    Args:
        filepath (str): The path to the file to be searched.
        regex_pattern (str): The regular expression pattern to match.

    Returns:
        tuple: A tuple containing a sorted list of unique matching lines and the total count.
    """
    matching_lines_set = set() # Use a set to store unique lines
    try:
        with open(filepath, 'r') as file:
            for line in file:
                # The re.search() function looks for a match anywhere in the line.
                if re.search(regex_pattern, line):
                    matching_lines_set.add(line.strip()) # Add the line to the set
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return [], 0
    
    # Convert the set to a list, sort it, and get the count
    matching_lines = sorted(list(matching_lines_set), key=sort_key_by_dotted_number)
    line_count = len(matching_lines)
    return matching_lines, line_count

def write_to_output_file(output_filepath, lines, count):
    """
    Writes the count and the list of lines to an output file.

    Args:
        output_filepath (str): The path to the output file.
        lines (list): A list of lines to be written.
        count (int): The total count of unique lines.
    """
    with open(output_filepath, 'w') as file:
        file.write(f"Total unique matching lines: {count}\n")
        if count > 0:
            file.write("\n".join(lines) + "\n")
    print(f"\nSuccessfully wrote {count} unique lines to '{output_filepath}'.")

# Main script execution
if __name__ == "__main__":
    file_path = "CIS_IBM_AIX_7_v1.0.0_L1_CUSTOM_TEST3142025.audit"  # Replace with the path to your input file
    output_path = "CIS_IBM_AIX_7_v1.0.0_L1_CUSTOM_TEST3142025.audit.rules.out"  # The name of the new output file
    pattern = r'description\s*:\s*"\s*[\d.]+'

    # Check if the input file exists before proceeding
    if not os.path.exists(file_path):
        print(f"Error: The input file '{file_path}' does not exist.")
    else:
        found_lines, total_count = find_and_count_matching_lines(file_path, pattern)

        # Display the count
        print(f"Found a total of {total_count} unique matching lines.")

        # Write to the output file
        if total_count > 0:
            write_to_output_file(output_path, found_lines, total_count)
        else:
            print("No matching lines found. The output file will not be created.")
