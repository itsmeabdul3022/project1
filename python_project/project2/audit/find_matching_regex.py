import re
import os

def find_and_count_matching_lines(filepath, regex_pattern):
    """
    Finds and counts all lines in a file that match a given regular expression.

    Args:
        filepath (str): The path to the file to be searched.
        regex_pattern (str): The regular expression pattern to match.

    Returns:
        tuple: A tuple containing a list of matching lines and the total count.
    """
    matching_lines = []
    line_count = 0
    try:
        with open(filepath, 'r') as file:
            for line in file:
                # The re.search() function looks for a match anywhere in the line.
                if re.search(regex_pattern, line):
                    matching_lines.append(line.strip())
                    line_count += 1
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    return matching_lines, line_count

def write_to_output_file(output_filepath, lines, count):
    """
    Writes the count and the list of lines to an output file.

    Args:
        output_filepath (str): The path to the output file.
        lines (list): A list of lines to be written.
        count (int): The total count of lines.
    """
    with open(output_filepath, 'w') as file:
        file.write(f"Total matching lines: {count}\n")
        if count > 0:
            file.write("\n".join(lines) + "\n")
    print(f"\nSuccessfully wrote {count} lines to '{output_filepath}'.")

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
        print(f"Found a total of {total_count} matching lines.")

        # Write to the output file
        if total_count > 0:
            write_to_output_file(output_path, found_lines, total_count)
        else:
            print("No matching lines found. The output file will not be created.")