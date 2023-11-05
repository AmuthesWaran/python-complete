import pandas as pd
from fuzzywuzzy import fuzz, process
import logging

logging.basicConfig(filename='./logs_filter_opt.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
logging.info('start')


firstname = pd.read_csv('./firstname.csv')
fullname = pd.read_csv('./fullname.csv')

firstname.fillna('', inplace=True)
fullname.fillna('', inplace=True)


def compute_fuzzy_match(source, target):
    return fuzz.ratio(source, target)


matching_results = []


for index1, fname in firstname.iterrows():

    source_record = fname['firstname']
    first1char = source_record[0:1]

    for index2, flname in fullname.iterrows():

        target_record = flname['fullname']

        if (target_record.startswith(first1char)):
            # Compute the fuzzy match score
            match_score = compute_fuzzy_match(source_record, target_record)

        # Add the match to the results DataFrame if it meets a certain threshold
            if match_score >= 60:  # Adjust the threshold as needed
                matching_results.append(
                    {'inputid1':  fname['id'], 'input': source_record, 'masterid':  flname['id'], 'master': target_record, 'FuzzyMatchScore': match_score})

matching_results_df = pd.DataFrame(matching_results)

# print(matching_results_df)

matching_results_df.to_csv('matching_results_filter_opt.csv', index=False)
logging.info('end')
