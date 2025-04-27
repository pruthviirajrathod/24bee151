import os
import shutil

# Define source file path and target folder
source_file = 'old_folder/sample.txt'  # Example: file to copy
new_subdir = 'new_folder'              # Folder to create
destination_file = os.path.join(new_subdir, 'sample.txt')

# Step 1: Create the new subdirectory if it doesn't exist
if not os.path.exists(new_subdir):
    os.make

