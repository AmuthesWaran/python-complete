import pandas as pd
from fuzzywuzzy import fuzz, process
import logging

logging.basicConfig(filename='./logs0.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.info('start')

firstname = pd.read_csv('./firstname.csv')
fullname = pd.read_csv('./fullname.csv')


firstname.fillna('', inplace=True)
fullname.fillna('', inplace=True)

# print(type(fullname))

# Converting the df fullname column to list
list_fullname = fullname.fullname.values.tolist()

# Converting the df firstname column to list
list_firstname = firstname.firstname.values.tolist()

# Function to compute fuzzy match score


def compute_fuzzy_match(source, target):
    return fuzz.ratio(source, target)


# Initialize an empty DataFrame to store the matching results
matching_results = []


for flname in list_fullname:
    first2letters = flname[0:5]
    print(first2letters)
    # print(list(filter(lambda x: x.startswith(first2letters), flname)))
    for fname in list_firstname:
        if (fname.startswith(first2letters)):
            match_score = compute_fuzzy_match(flname, fname)
            # print(match_score)
            if match_score >= 0:  # Adjust the threshold as needed
                matching_results.append(
                    {'File1_Record': fname, 'File2_Record': flname, 'FuzzyMatchScore': match_score})

matching_results_df = pd.DataFrame(matching_results)

# print(matching_results_df)

matching_results_df.to_csv('matching_results2.csv', index=False)

logging.info('end')
