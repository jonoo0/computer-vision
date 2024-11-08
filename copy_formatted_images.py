import os
import shutil
import re

def copy_mask_files(source_dir, destination_dir):
    # Ensure destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Regular expression to match the naming format: "{id_number}_mask.png"
    pattern = re.compile(r'^\d+_mask\.png$')

    # Loop through files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the filename matches the pattern
        if pattern.match(filename):
            # Construct full file paths
            source_path = os.path.join(source_dir, filename)
            destination_path = os.path.join(destination_dir, filename)
            # Copy the file to the destination directory
            shutil.copy2(source_path, destination_path)
            print(f"Copied: {filename}")

# Usage
source_directory = 'path/to/source_directory'
destination_directory = 'path/to/destination_directory'
copy_mask_files(source_directory, destination_directory)
