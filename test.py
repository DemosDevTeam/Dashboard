import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import json

users = pd.read_csv('data/csv/users.csv')
users = (users[['age', 'children', 'education', 'gender',
                'income', 'marital', 'occupation', 'race']]).dropna()

videos = pd.read_csv('data/csv/videos.csv', index_col=0, encoding='latin1')
#print(videos)
videos = pd.DataFrame.from_dict(videos.iloc[:, 1:])
# print(videos.shape)
# print(videos.head())
#print(videos.iloc[:, 1:])

for i in videos:
    print(i)

    node = videos[i][0]
    dateIdx = node.find('date')

    dictString = videos[i][0][dateIdx:]
    dictString = "{\'" + dictString
    dictString = dictString.replace('\'', '\"')
    dictString = dictString.replace('0,', '\"0\",')
    dictString = dictString.replace('0}', '\"0\"}')


    print(dictString)
    newDict = json.loads(dictString)

    print(type(newDict))
    print(newDict)
    print(pd.DataFrame.from_dict(newDict), '\n')    

rows = videos.iloc[:, 1:]
#print(rows)

dataframe = pd.DataFrame(videos.items())

df1 = dataframe.from_dict(dataframe)
#print(df1)
# print(dataframe.iloc[:, 1])
#print(df1)
issueDict = df1.iloc[:, 1]
#print(issueDict, '\n')
#print(issueDict.items())

df2 = dataframe.from_items(dataframe.items(),
                           orient='index',
                           columns=['Issue', 'Reaction'])

#print(df2)                    


# uniqueUsers = pd.DataFrame(users.groupby('age').count())

# # print(users.head())
# # print(users.columns()
# print(uniqueUsers.head())
# labels = uniqueUsers.index.tolist()
# values = uniqueUsers.iloc[:, 0].tolist()

# print(labels)
# print(values)