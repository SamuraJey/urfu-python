import pandas as pd


data = pd.read_csv('numpy and pandas/titanic_train.csv',
                   index_col='PassengerId')

miss_data = data[data['Name'].str.contains('Miss')]

miss_names = miss_data['Name'].str.extract(r'Miss\. ([A-Za-z]+)')
name_counts = miss_names[0].value_counts().reset_index()

sorted_df = name_counts.rename(columns={'index': 'Name', 0: 'Popularity'})
sorted_df.sort_values(by=['Popularity', 'Name'], ascending=[
                      False, True], inplace=True)

print(sorted_df)
