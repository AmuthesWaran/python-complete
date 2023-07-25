import csv
# with open('E:/GitHub Projects/python-complete/00_misc/readandsplit.py', 'r') as file:
#     data = data = file.read().rstrip()

text_as_string = open(
    'E:/GitHub Projects/python-complete/00_misc/emailid.txt', 'r').read()


splited_string = text_as_string.split(";")


trim_string = []
fname_list = []

for text in splited_string:
    trim_string.append(text.strip())


fields = ['emailid', 'firstname', 'lastname']

filename = 'name_list.csv'

firstname = []
lastnamedirty = []
lastname = []
for emailid in trim_string:
    firstname = emailid.split('.')[0]
    lastnamedirty = emailid.split('@')[0].strip()

print(firstname)
print(lastnamedirty)

for lastnames in lastnamedirty:
    print(lastnames)
    lastname = lastnames.split('.')[1]


exportdata = zip(trim_string, firstname, lastname)

print(firstname)

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)
    for item in exportdata:
        csvwriter.writerows([item])
