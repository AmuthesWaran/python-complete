import pandas as pd
from fuzzywuzzy import fuzz, process
import logging


logging.basicConfig(filename='./logs.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
logging.info('start')

firstname = pd.read_csv('./firstname.csv')
fullname = pd.read_csv('./fullname.csv')


firstname.fillna('', inplace=True)
fullname.fillna('', inplace=True)

# print(firstname)
# print(fullname)


# Function to compute fuzzy match score
def compute_fuzzy_match(source, target):
    return fuzz.ratio(source, target)


# Initialize an empty DataFrame to store the matching results
matching_results = []


# Iterate through records in file1_df
for index1, row1 in firstname.iterrows():
    # Adjust this based on your file structure
    source_record = row1['firstname']
    # logging.info(row1['firstname'])
    # Iterate through records in file2_df
    for index2, row2 in fullname.iterrows():
        # Adjust this based on your file structure
        target_record = row2['fullname']
        # print(target_record)

        # Compute the fuzzy match score
        match_score = compute_fuzzy_match(source_record, target_record)

        # Add the match to the results DataFrame if it meets a certain threshold
        if match_score >= 0:  # Adjust the threshold as needed
            matching_results.append(
                {'File1_Record': source_record, 'File2_Record': target_record, 'FuzzyMatchScore': match_score})

matching_results_df = pd.DataFrame(matching_results)

# print(matching_results_df)

matching_results_df.to_csv('matching_results.csv', index=False)
logging.info('end')
