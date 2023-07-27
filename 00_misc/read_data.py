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
for i in range(0, len(trim_string)):
    firstname = trim_string[i].split('.')[0]
    lastnamedirty = trim_string[i].split('@')[0].strip()

print(firstname)
print(lastnamedirty)


for i in range(0, len(lastnamedirty)):
    # print(lastnamedirty[1])
    lastname = lastnamedirty[i].split('.')[0]


exportdata = zip(trim_string, firstname, lastname)

print(firstname)

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)
    for item in exportdata:
        csvwriter.writerows([item])
