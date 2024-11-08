import os
import re

def rename_files(directory):
    # Regular expression to match the naming format "{id_number}_sat.jpg"
    pattern = re.compile(r'^(\d+)_sat\.jpg$')

    # Loop through files in the specified directory
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            # Extract the id_number
            id_number = match.group(1)
            # Create the new filename
            new_filename = f"{id_number}_mask.jpg"
            # Construct full file paths
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

# Usage
directory_path = 'path/to/directory'
rename_files(directory_path)
