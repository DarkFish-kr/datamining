activity = [0.8, 0.3, 0.6]
activity[0]

import pandas as pd
activity = pd.Series(
    [0.8, 0.3, 0.6],
    index=['Morning', 'Afternoon', 'Evening']
)

activity['Morning']

sensor = [22.3, 6.5, 7.4]
sensor[1]
sensor = pd.Series({
'Temp': 22.3,
'DO': 6.5,
'pH': 7.4
})
sensor['DO']

import pandas as pd
list1 = [['08:00', 22.5, 33.1, 6.5],
['10:00', 23.2, 33.3, 6.2],
['12:00', 24.0, 33.5, 5.8],
['14:00', 25.1, 33.7, 5.5],
['16:00', 24.6, 33.6, 5.9],
['18:00', 23.8, 33.4, 6.1],
['20:00', 22.9, 33.2, 6.4],
['22:00', 22.3, 33.1, 6.6]]
col_names = ['Time', 'Temp', 'Salinity', 'DO']
df = pd.DataFrame(list1, columns=col_names)
df
df.to_csv('./water_data.csv', header=True, index=False, encoding='utf-8')
df2 = pd.read_csv('./water_data.csv', sep=',')
df2

df.columns

df.describe()

df.head(3)

df.tail()

list1 = list([['한빛', '남자', '20', '180'],
            ['한결', '남자', '21', '177'],
            ['한라', '여자', '20', '160']])
col_name = ['이름', '성별', '나이', '키']
pd.DataFrame(list1)

#코드 6-14
dict1 = {'이름':{0:'한빛', 1:'한결', 2:'한라'},
        '성별':{0:'남자', 1:'남자', 2:'여자'},
        '나이':{0:'20', 1:'21', 2:'20'},
        '키':{0:'180', 1:'177', 2:'160'}}
pd.DataFrame(dict1)

import numpy as np

arr1 = np.array([['한빛', '남자', '20', '180'],
            ['한결', '남자', '21', '177'],
            ['한라', '여자', '20', '160']])

col_names = ['이름', '성별', '나이', '키']

pd.DataFrame(arr1, columns=col_names)

#코드 6-22
df.sort_index(axis=0).head()

#코드 6-23
df.sort_values(by=['Temp', 'DO'], ascending=False).head()

#코드 6-24
df[['Temp', 'DO']].head()

#코드 6-25
df.iloc[1:4, 0:3]

#코드 6-26
df[df['DO'] <= 6]

#코드 6-27
df[df['DO'] < 6]

#코드 6-28
df[df['Temp'].isin([24.0, 23.8])]

#코드 6-29
df[(df['DO'] < 6) & (df['Temp'] > 24)]

#코드 6-30
df[(df['Temp'] >= 24) | (df['DO'] <= 5.8)]

#코드 6-31
df[df['Time'].str.contains('1')]

#코드 6-32
df.describe()

#코드 6-33
df.loc[4, 'DO'] = df.loc[4, 'DO'] + 0.5
df.loc[4]
df.loc[4, 'DO'] = df.loc[4, 'DO'] - 0.5
df.loc[4]

#코드 6-34
df.loc[1:3, 'DO'] = ['No data'] * 3
df

#원상복구
df.loc[1:3, 'DO'] = [6.2, 5.8, 5.5]
df.loc[1:3]

#코드 6-35
df.set_index('Time', inplace=True)
df.head(3)

#코드 6-36
df['DO_score'] = df['DO'] * 10
df.head(3)

#코드 6-37
df.drop('DO_score', axis=1, inplace=True)
df.head(3)

#코드 6-38
df.reset_index(inplace=True)

#코드 6-39
df['DO_Status'] = ['Normal', 'Normal', 'Low', 'Low', 'Low', 'Normal', 'Normal', 'Normal']
rep_cond = {'DO_Status': {'Normal': 1, 'Low': 0}}
df2 = df.replace(rep_cond)
df2.head(3)
df.head(3)

#코드 6-40
mean_by_status = df.groupby(by=['DO_Status'], as_index=False)['Temp'].mean()
mean_by_status.rename(columns={'Temp': '평균 Temp'}, inplace=True)
std_by_status = df.groupby(by=['DO_Status'], as_index=False)['Temp'].std()
std_by_status.rename(columns={'Temp': 'Temp의 표준편차'}, inplace=True)
new_df = pd.merge(mean_by_status, std_by_status)
new_df