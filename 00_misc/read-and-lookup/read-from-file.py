# This python script will read all the lines of input.txt and store as a list 

input_file_path = 'input.txt'

with open(input_file_path, 'r') as file:
    lines = file.readlines()

cleaned_line = [line.strip() for line in lines]

print(cleaned_line)