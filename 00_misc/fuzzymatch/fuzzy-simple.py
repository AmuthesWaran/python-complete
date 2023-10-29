import pandas as pd
from fuzzywuzzy import fuzz, process
import logging

logging.basicConfig(filename='./logs-simple.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
logging.info('start')

firstname = pd.read_csv('./firstname.csv')
fullname = pd.read_csv('./fullname.csv')


firstname.fillna('', inplace=True)
fullname.fillna('', inplace=True)
firstname_list = firstname['firstname'].tolist()
fullname_list = fullname['fullname'].tolist()
idfirstname_list = firstname['id'].tolist()
idfullname_list = fullname['id'].tolist()

# Initialize an empty DataFrame to store the matching results
matching_results = []


def get_matches(input, master, limit=10):
    results = process.extract(input, master, limit=limit)
    print(results)
    return results


for fname in firstname_list:
    res = get_matches(fname, fullname_list)
    for re in res:
        # print(re[1]>80)
        print(re)
        if (re[1] > 80):
            print(fname, re[0], re[1])
            print()
            matching_results.append(
                {'input': fname, 'master': re[0], 'FuzzyMatchScore': re[1]})


matching_results_df = pd.DataFrame(matching_results)

matching_results_df.to_csv('matching_results_simple.csv', index=False)

logging.info('end')
