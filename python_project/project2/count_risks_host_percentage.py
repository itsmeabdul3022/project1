import pandas as pd

def count_risks_and_compliance(filename):
    """
    Reads a CSV file, prompts for a host, counts risks, and calculates compliance percentage.

    Args:
        filename (str): The name of the CSV file.
    """
    try:
        # Read the CSV file, keeping the default NA values as strings
        df = pd.read_csv(filename, keep_default_na=False)
        
        # Convert the 'Host' column to lowercase for consistent searching
        df['Host'] = df['Host'].astype(str).str.lower()
        
        # Get the input for the host and also convert it to lowercase
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
        
        # Define the specific risk levels
        passed_levels = ['None']
        failed_levels = ['High', 'Medium', 'Low']
        
        # Calculate passed and failed counts
        passed_count = 0
        failed_count = 0
        
        for level, count in risk_counts.items():
            if level in passed_levels:
                passed_count += count
            elif level in failed_levels:
                failed_count += count

        total_records = passed_count + failed_count
        
        # Calculate compliance percentage
        if total_records > 0:
            compliance_percentage = (passed_count / total_records) * 100
        else:
            compliance_percentage = 0.0

        print("\n--- Compliance Report for Host:", target_host, "---")
        print(f"Total Records: {total_records}")
        print(f"Passed: {passed_count}")
        print(f"Failed: {failed_count}")
        print(f"Compliance Percentage: {compliance_percentage:.2f}%")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_csv_file.csv' with the name of your file
    csv_file = 'Test_L2.csv' 
    count_risks_and_compliance(csv_file)