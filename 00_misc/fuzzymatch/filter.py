import pandas as pd

firstname = pd.read_csv('./firstname.csv')
fullname = pd.read_csv('./fullname.csv')


firstname.fillna('', inplace=True)
fullname.fillna('', inplace=True)


for index1, row1 in firstname.iterrows():
    # Adjust this based on your file structure
    # get column names that start with a specific string, s
    # df.columns[df.columns.str.startswith(s)]
    firstname['filter'] = list(
        map(lambda x: x.startswith('a'), firstname['firstname']))

    print(firstname)
    # Iterate through records in file2_df
    for index2, row2 in fullname.iterrows():
        # Adjust this based on your file structure
        target_record = row2['fullname']
# inprogress
