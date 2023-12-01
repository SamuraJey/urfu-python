import pandas as pd


def solution(data):
    strings_with_names = data[data['Name'].str.contains('Miss')]
    names = strings_with_names['Name'].str.extract(r'Miss\. ([A-Za-z]+)')

    name_counts = names[0].value_counts()
    answ = pd.DataFrame([name_counts]).T

    answ.insert(0, '', answ.index)
    answ.reset_index(drop=True, inplace=True)

    answ.columns = ['Name', 'Popularity']
    answ = answ.sort_values(by=['Popularity', 'Name'], ascending=[False, True])
    return answ


data = pd.read_csv('numpy and pandas/titanic_train.csv',
                   index_col='PassengerId')

print(solution(data))
