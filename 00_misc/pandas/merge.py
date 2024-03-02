import pandas as pd

emp_df = pd.read_csv("E:\\python-complete\\00_misc\\pandas\\employees.csv")
dept_df = pd.read_csv("E:\\python-complete\\00_misc\\pandas\\departments.csv")

print(emp_df.head())
print(dept_df.head())

merged = pd.merge(left=emp_df, right=dept_df, left_on='DEPARTMENT_ID', right_on='DEPARTMENT_ID', how='left')

print(merged.head())
merged.drop('DEPARTMENT_ID', axis=1)
merged.to_csv('department_merged.csv', index=False)