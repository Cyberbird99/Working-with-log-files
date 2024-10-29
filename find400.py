# Prompt for a file to analyze
log_filename = input("Name a file to analyze: ")

try:
    # Open the file using a context manager
    with open(log_filename, "r") as log_file:
        # Read the file line by line
        for line in log_file:
            # Check for the keyword "403"
            if "403" in line:
                print(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{log_filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

   
