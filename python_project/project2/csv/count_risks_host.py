import pandas as pd

def count_risks_for_host(filename):
    """
    Reads a CSV file, prompts for a host, and counts risk occurrences.

    Args:
        filename (str): The name of the CSV file.
    """
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(filename, na_filter=False)

        # Get the input for the host
        target_host = input("Enter the host name: ").strip().lower()

        # Check if the 'Host' column exists
        if 'Host' not in df.columns:
            print("Error: The 'Host' column was not found in the CSV file.")
            return
        
        # Check if the 'Risk' column exists
        if 'Risk' not in df.columns:
            print("Error: The 'Risk' column was not found in the CSV file.")
            return

        # Filter the DataFrame for the specified host
        host_data = df[df['Host'] == target_host]

        if host_data.empty:
            print(f"No data found for the host: {target_host}")
            return

        # Count the occurrences of each risk level
        risk_counts = host_data['Risk'].value_counts()
        
        # Define the specific risk levels you want to count
        risk_levels = ['High', 'Medium', 'Low', 'None']
        
        # Create a dictionary to store the final counts
        final_counts = {level: 0 for level in risk_levels}
        
        # Update the dictionary with the actual counts from the DataFrame
        for level in risk_counts.index:
            if level in final_counts:
                final_counts[level] = risk_counts[level]
            
        print("\n--- Risk Counts for Host:", target_host, "---")
        for level, count in final_counts.items():
            print(f"{level}: {count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_csv_file.csv' with the name of your file
    csv_file = 'CIS-Enterprise-Scan-Level-1_2--AIX_SEPT.csv'
    count_risks_for_host(csv_file)
 