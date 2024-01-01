import pandas as pd
import numpy as np
import joblib,fuzzywuzzy
from fuzzywuzzy import fuzz,process
from joblib import Parallel, delayed
import logging

logging.basicConfig(filename='./logs0.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.info('start')

firstname = pd.read_csv('../firstname.csv')
fullname = pd.read_csv('../fullname.csv')


firstname.fillna('', inplace=True)
fullname.fillna('', inplace=True)

print(type(firstname))
print(type(fullname))

## Define the fuzzy metric (uncomment any one of the metric)
metric = fuzz.ratio
#metric = fuzz.partial_ratio
#metric = fuzz.token_sort_ratio
#metric = fuzz.token_set_ratio

# Define Threshold for Metric
thresh = 60

ca = np.array(firstname[["firstname"]])
cb = np.array(fullname[["fullname"]])

#Parallel Code
def parallel_fuzzy_match(idxa,idxb):
    return [ca[idxa][0],cb[idxb][0],metric(ca[idxa][0],cb[idxb][0])]  
results = Parallel(n_jobs=-1,verbose=1)(delayed(parallel_fuzzy_match)(idx1, idx2) for idx1 in range(len(ca)) for idx2 in range(len(cb)) \
                   if(metric(ca[idx1][0],cb[idx2][0]) > thresh))

#Sequential Code
#from tqdm import tqdm
#results = [(ca[idx1][0],cb[idx2][0],metric(ca[idx1][0],cb[idx2][0])) for idx1 in tqdm(range(len(ca))) for idx2 in range(len(cb)) if metric(ca[idx1][0],cb[idx2][0]) > thresh]

results = pd.DataFrame(results,columns = ["firstname","fullname","Score"])

results.to_csv('output.csv', index=False)

logging.info('end')