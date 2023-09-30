import csv

filecontent_as_string = open(
    './00_misc/emailid.txt', 'r').read()

splited_string = filecontent_as_string.split(";")

# Initializing empty lists
trim_string = []
firstname = []
lastname = []
fields = ['emailid', 'firstname', 'lastname']
filename = 'extracted_output.csv'


for text in splited_string:
    trim_string.append(text.strip())

for i in range(0, len(trim_string)):
    firstname.append(trim_string[i].split('.')[0])
    lastname.append(trim_string[i].split('@')[0].strip().split('.')[1])

exportdata = zip(trim_string, firstname, lastname)

with open(f'./00_misc/{filename}', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)
    for item in exportdata:
        csvwriter.writerows([item])
