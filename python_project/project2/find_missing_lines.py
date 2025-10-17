import os

def find_missing_lines(file_a, file_b):
    """
    Compares two files and finds lines in file_a that are not in file_b.

    Args:
        file_a (str): The path to the superset file.
        file_b (str): The path to the subset file.

    Returns:
        list: A list of lines found in file_a but missing in file_b.
              Returns an empty list if file_a or file_b don't exist.
    """
    if not os.path.exists(file_a) or not os.path.exists(file_b):
        print("One or both files do not exist.")
        return []

    with open(file_a, 'r') as f_a:
        lines_a = set(f_a.readlines())

    with open(file_b, 'r') as f_b:
        lines_b = set(f_b.readlines())

    missing_lines = sorted(list(lines_a - lines_b))
    return missing_lines

def update_file_with_missing_lines(file_b, missing_lines):
    """
    Updates file_b by adding missing lines at the top with a comment section.

    Args:
        file_b (str): The path to the file to be updated.
        missing_lines (list): A list of lines to be added.
    """
    if not missing_lines:
        print("No missing lines to add.")
        return

    # Read the original content of file B
    with open(file_b, 'r') as f_b:
        original_content = f_b.readlines()

    # Prepare the new content
    new_content = ["\"\"\" Excludes\"\"\"\n"] + missing_lines + original_content

    # Write the new content back to file B
    with open(file_b, 'w') as f_b:
        f_b.writelines(new_content)

    print(f"File '{file_b}' has been updated successfully with the missing lines.")

def main():
    """
    Main function to execute the file comparison and update process.
    """
    file_a = "CIS_IBM_AIX_7_v1.0.0_L2.audit"  # Replace with the path to your first file
    file_b = "CIS_IBM_AIX_7_v1.0.0_L2_CUSTOM_TEST3072025.audit"  # Replace with the path to your second file

    missing = find_missing_lines(file_a, file_b)
    if missing:
        update_file_with_missing_lines(file_b, missing)
    else:
        print("No missing lines were found.")

if __name__ == "__main__":
    main()