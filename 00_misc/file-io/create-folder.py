import os
from datetime import datetime

# This script will create a folder in DDMMYYY format

# Get today's date
today_date = datetime.now().date()
# print(today_date)

# Format the date as a string without any special characters
folder_name = today_date.strftime("%d%m%Y")
# print(folder_name)

# Specify the path where you want to create the folder
# folder_path = f'/d/python-complete/00_misc/file-io/{folder_name}'
folder_path = folder_name

# Create a new folder/directory
try:
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' created successfully.")
except OSError as e:
    print(f"Error: {e}")
