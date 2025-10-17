import re
import json
def find_match_files(file_a,file_b):
    pattern_a = re.compile(r'^description\s*:\s*"([\d.]+)\s*(.*?)"')
    file_a_data: {}
    try:
        with open(file_a_path, r) as f_b:
            for line in f_b:
                match = pattern_a.search(line)
                if match:
                    dotted_number_a = match.group(1).strip()
                    other_data = match.group(2).strip()
                    file_a_data[other_data] = dotted_number_a
        print("Contents of file_b_data dictionary (JSON format):")
        print(json.dumps(file_a_data, indent=2))            
    except FileNotFoundError:
        print(f"Error: The file '{file_a_path}' was not found.")