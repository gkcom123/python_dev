import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('salaries_by_college_major.csv')
# print(df.head())
# print(df.shape)
print(df.columns)
# print(df.isna)
clean_df = df.dropna()
median_sal_max_index= clean_df['Starting Median Salary'].idxmax()
med_max = clean_df['Undergraduate Major'].loc[43]
med_max_2 = clean_df.loc[43]
print(med_max_2)
med_sal_4 = clean_df['Starting Median Salary'].idxmin()
print(clean_df.loc[med_sal_4])
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
print(clean_df.head())
low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())