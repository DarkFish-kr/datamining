import networkx as nx
import pandas as pd
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from wordcloud import wordcloud
from konlpy.tag import Okt
from collections import Counter
import numpy as np

# DiGraph는 방향성을 볼 때 사용한다.
G = nx.DiGraph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])

nx.draw(G, with_labels=True)

# 노드 추가 및 제거하기
g1 =nx.Graph()
g1.add_node('David')
g1.add_node('John')
g1.add_node('Mary')
g1.add_node('Julia')
g1.add_node('Juda')
g1.add_nodes_from(['Judy', 'Karen'])
g1.remove_node('Julia')

#선 추가 및 제거하기
g1.add_edge('David', 'John')
g1.add_edge('David', 'Mary')
g1.add_edge('David', 'Karen')
g1.add_edges_from([('John', 'Mary'), ('John', 'Judy')])
g1.remove_edge('John', 'Mary')

d = dict(g1.degree)
nx.draw(g1, nodelist=d.keys(), node_size=[v*1800 for v in d.values()], with_labels=True, font_weight='bold')

g1.nodes

g2 = nx.DiGraph()
g2.add_edges_from([(1,2), (1,3), (1,4), (3,4)])
nx.draw(g2, with_labels=True, font_weight='bold')
print(g2.in_degree)
print(g2.out_degree)

g3 = nx.DiGraph()
g3.add_weighted_edges_from([(1,2,10), (2,3,20)])
g3.add_edge(1, 3, weight=30)
pos = nx.spring_layout(g3)

nx.draw(g3, pos, with_labels=True)
labels = nx.get_edge_attributes(g3, 'weight')
nx.draw_networkx_edge_labels(g3, pos, edge_labels=labels)

df = pd.DataFrame({'from': ['A', 'B', 'C', 'A', 'E', 'D'], 'to': ['D', 'A', 'E', 'C', 'A', 'E'], 'weight': [1,2,3,4,5,6]})

g4 = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.DiGraph())
nx.draw(g4, with_labels=True)

df1 = pd.read_csv('/Users/jun/Library/Mobile Documents/com~apple~CloudDocs/Github/datamining/Data folder/OBS_ASOS_MNH_20260414234817.csv', encoding='cp949')
df1.head(3)

df2 = df1.ffill()
df2.info()

df2.rename(columns={'최저기온(°C)':'min_temp'},inplace=True)
df2.rename(columns={'평균기온(°C)':'avg_temp'},inplace=True)
df2.rename(columns={'최고기온(°C)':'max_temp'},inplace=True)
df2.head(3)


plt.title('여수의 월별 기온 변화')
plt.plot(range(1,len(df2)+1), df2['max_temp'], label='최고기온', c='r')
plt.plot(range(1,len(df2)+1), df2['avg_temp'], label='평균기온', c='y')
plt.plot(range(1,len(df2)+1), df2['min_temp'], label='최저기온', c='b')

plt.xlabel('일')
plt.ylabel('기온')
plt.legend()
plt.show()

df2['일시']=pd.to_datetime(df2['일시'], format='%Y-%m')
df2['일시']

df3 = df2.set_index('일시')
df1.head(3)

df_Mar = df3[pd.DatetimeIndex(df3.index).month ==3]

plt.title('여수시 연도별 3월 기온 변화')
plt.plot(df_Mar.index, df_Mar['max_temp'], label='최고기온', c='r')
plt.plot(df_Mar.index, df_Mar['avg_temp'], label='평균기온', c='y')
plt.plot(df_Mar.index, df_Mar['min_temp'], label='최저기온', c='b')

plt.xlabel('년도')
plt.ylabel('기온')
plt.legend()
plt.rcParams['figure.figsize'] = (10,6)

plt.show()
plt.savefig('yeosu_march_annual_temp.png')