import csv
# with open('E:/GitHub Projects/python-complete/00_misc/readandsplit.py', 'r') as file:
#     data = data = file.read().rstrip()

text_as_string = open(
    'E:/GitHub Projects/python-complete/00_misc/emailid.txt', 'r').read()
print(text_as_string)


splited_string = text_as_string.split(";")

print(splited_string)

trim_string = []
fname_list = []
print(type(trim_string))
print(type(splited_string))

for text in splited_string:
    trim_string.append(text.strip())

print(trim_string)

fields = ['emailid', 'fname']

filename = 'name_list.csv'

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)
    for item in trim_string:
        csvwriter.writerow([item])
