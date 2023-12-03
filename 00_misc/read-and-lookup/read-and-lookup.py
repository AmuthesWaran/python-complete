import pandas as pd
import sqlite3
import csv

input_file_path = 'input.txt'

with open(input_file_path, 'r') as file:
    lines = file.readlines()

cleaned_line = [line.strip() for line in lines]

print(cleaned_line)


conn = sqlite3.connect(':memory:')

cursor = conn.cursor()

df = pd.read_csv('look-up.csv')

df.to_sql('lookup', conn, index=False)

query = "SELECT EMPLOYEE_ID,FIRST_NAME,LAST_NAME FROM lookup WHERE EMPLOYEE_ID IN ({})".format(','.join(['?']*len(cleaned_line)))
result = cursor.execute(query, cleaned_line)

rows = result.fetchall()

cursor.close()
conn.close()

with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header
    csv_writer.writerow(['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME'])  # Replace with your column names
    
    # Write data rows
    for row in rows:
        csv_writer.writerow(row)