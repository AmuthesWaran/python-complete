import pandas as pd
from fuzzywuzzy import fuzz, process
import logging

logging.basicConfig(filename='./logs-simple.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
logging.info('start')

firstname = pd.read_csv('./firstname.csv')
fullname = pd.read_csv('./fullname.csv')


firstname.fillna('', inplace=True)
fullname.fillna('', inplace=True)
firstname_list = firstname['firstname'].tolist()
fullname_list = fullname['fullname'].tolist()


def get_matches(input, master, limit=10):
    results = process.extract(input, master, limit=limit)
    # print(type(results))
    return results


for fname in firstname_list:
    res = get_matches(fname, fullname_list)
    for re in res:
        # print(re[1]>80)
        if (re[1] > 80):
            print(re[0], re[1])
    # if (res[1] > 80):
    # print(res)
