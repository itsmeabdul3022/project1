import re
import os

def get_matching_lines(filepath):
    """
    Reads a file and returns a set of lines that match the specific pattern.
    The regex '^\s*description' handles leading whitespace.
    """
    matching_lines = set()
    # The  pattern now accounts for leading whitespace
    regex_pattern = r'^\s*description\s*:\s*"\s*[\d.]+'
    
    try:
        with open(filepath, 'r') as file:
            for line in file:
                # re.match() is a good choice as it only checks from the start of the line
                if re.match(regex_pattern, line):
                    matching_lines.add(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    return matching_lines

def write_output_file(output_filepath, lines, count):
    """
    Writes the count and the list of lines to an output file.
    """
    try:
        with open(output_filepath, 'w') as file:
            file.write(f"Total unique lines found in File A but not in File B: {count}\n")
            if count > 0:
                file.write("\n" + "\n".join(lines) + "\n")
        print(f"\nSuccessfully wrote {count} lines to '{output_filepath}'. ✅")
    except IOError as e:
        print(f"Error writing to output file '{output_filepath}': {e} ❌")

# --- Main Execution ---
if __name__ == "__main__":
    file_a_path = input("Enter the path of file a : ")  # 📌 Update with your superset file path
    file_b_path = input("Enter the path of file b: ")  # 📌 Update with your subset file path
    output_path = input("Enter output file name:" ) 

    if not os.path.exists(file_a_path):
        print(f"Error: Input file A '{file_a_path}' does not exist. ⚠️")
    elif not os.path.exists(file_b_path):
        print(f"Error: Input file B '{file_b_path}' does not exist. ⚠️")
    else:
        lines_a = get_matching_lines(file_a_path)
        lines_b = get_matching_lines(file_b_path)
        
        unique_missing_lines = sorted(list(lines_a - lines_b))
        total_unique_lines = len(unique_missing_lines)
        
        print(f"Found {total_unique_lines} unique lines matching the pattern. 🕵️‍♂️")

        if total_unique_lines > 0:
            write_output_file(output_path, unique_missing_lines, total_unique_lines)
        else:
            print("No unique lines were found. Output file not created. 🤷‍♂️")