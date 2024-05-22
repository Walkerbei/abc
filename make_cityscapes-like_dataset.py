import shutil
import os
import re
####labelIds copy to 
def batch_rename_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Define the pattern to match filenames
    pattern = re.compile(r'^(\d+_){3}\d+\.png$')

    # Iterate through each file
    for file_name in files:
        # Check if the filename matches the pattern
        if pattern.match(file_name):
            # Extract the prefix from the filename
            prefix = file_name.split('.')[0]

            # Construct the new filename
            new_file_name = f"{prefix}_color.png"

            # Construct the full paths for the old and new files
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)

def batch_rename_files2(source_folder):
    # List all files in the source folder
    files = os.listdir(source_folder)

    # Iterate through each file
    for file_name in files:
        # Check if the filename ends with '.png'
        if file_name.endswith('.png'):
            # Construct the new filename
            new_file_name = file_name.replace('_leftImg8bit.png', '.png')

            # Construct the full paths for the source and destination files
            source_file_path = os.path.join(source_folder, file_name)
            destination_file_path = os.path.join(source_folder, new_file_name)

            # Rename the file
            os.rename(source_file_path, destination_file_path)
            print(f"Renamed: {file_name} to {new_file_name}")

# Example usage
source_folder = "/Users/jc/Downloads/aihub_dataset_1840_add_class/Dataset2/imgFine/leftImg8bit/images_with_originalname/train/seoul"
batch_rename_files2(source_folder)


