# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 08:17:15 2016

@author: n393637
"""
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
s1= pd.Series([2,3,45,55])

s1.index

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
s2=Series(sdata)

s2['Ohio']

s2.name='ASeries'
s2.index.name='state'

s2.index = ['obgo', 'leve', 'eeff', 'fyan']

n=np.arange(10)
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)

frame['b']=23

frame.rename(columns={'b':'c'}, inplace=True)

#drop columns
frame.drop(['pop','year'], axis =1)

frame.dr
del frame['b']

pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

f2=DataFrame(pop)

f2.T

frame.set_index(['year'],inplace=True)

frame.columns
frame.index

f2=frame

#index methods????????

l=[1900,1901,1902]

f2.reindex(index=['a',2000,'b',2001,'c',2002])

f2[f2.index.duplicated()]

f2.ix[2002]

#==============================================================================
# 
#==============================================================================
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame
np.abs(frame)

f = lambda x: x.max() - x.min()
f1= lambda x: sum(x)
f2= lambda x: np.mean(x)
f3= lambda x: [np.std(x), np.mean(x)]

frame.apply(f)
frame.apply(f, axis=1)

frame.apply(f1)

frame.apply(f3,axis=1)

frame.apply(f2)

frame['avg']=frame.apply(f3,axis=1)

def f(x):
    return Series([x.min(), x.max()], index=['min','max'])
    
frame.apply(f)

format = lambda x: '%.2f' % x

frame.applymap(format)

frame.sort_index(by=['b'])
frame.sort_index()

frame.index.is_unique

df = DataFrame([[1.4, np.nan], [7.1, -4.5],[np.nan, np.nan], [0.75, -1.3]],index=['a', 'b', 'c', 'd'],columns=['one', 'two'])

df.sum(axis=0)

#return index for row with max 
df.idxmax()

obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
obj.unique()

frame.reset_index(inplace=True)

frame.set_index(['b','d'],inplace=True)

df.reset_index(inplace=True)

df[df.index.isin(['a'])]


data = DataFrame({'Qu1': [1, 3, 4, 3, 4],'Qu2': [2, 3, 1, 2, 3],
                  'Qu3': [1, 5, 2, 4, 4]})
                  
#note use of apply function
result = data.apply(pd.value_counts).fillna(0)


data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                   [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
#==============================================================================
# data
# Out[127]: 
# a  1   -0.984756
#    2    0.606217
#    3   -0.497659
# b  1    1.065649
#    2    0.655888
#    3    3.229694
# c  1    1.037043
#    2   -1.369270
# d  2   -1.107656
#    3   -0.038055
# dtype: float64
#==============================================================================
                   
data.ix['a'] 

data['b']    
#access sub level
data[:,2]

#==============================================================================
# data[:,2]
# Out[131]: 
# a    0.606217
# b    0.655888
# c   -1.369270
# d   -1.107656
# dtype: float64
# 
#==============================================================================

data.unstack()

#==============================================================================
# Out[133]: 
#           1         2         3
# a -0.984756  0.606217 -0.497659
# b  1.065649  0.655888  3.229694
# c  1.037043 -1.369270       NaN
# d       NaN -1.107656 -0.038055
#==============================================================================
              

frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                    columns=[['Ohio', 'Ohio', 'Colorado'],['Green', 'Red', 'Green']])

#==============================================================================
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
                 
#==============================================================================
# frame
# Out[151]: 
# state      Ohio     Colorado
# color     Green Red    Green
# key1 key2                   
# a    1        0   1        2
#      2        3   4        5
# b    1        6   7        8
#      2        9  10       11
# 
# 
#==============================================================================

#==============================================================================
#partial column indexing to select groups of columns
frame.Ohio
# 
# Out[144]: 
#      Green  Red
# a 1      0    1
#   2      3    4
# b 1      6    7
#   2      9   10
#==============================================================================

frame.ix['a'].sum()

frame.sum(level='key2')

frame.sum(level='color', axis=1)

#stack and unstack

data = DataFrame(np.arange(6).reshape((2, 3)),index=pd.Index(['Ohio', 'Colorado'], name='state'),
                 columns=pd.Index(['one', 'two', 'three'], name='number'))


#==============================================================================
# data
# Out[215]: 
# number    one  two  three
# state                    
# Ohio        0    1      2
# Colorado    3    4      5
#==============================================================================

#dataframe into series(if not multi index columns)
s1=data.stack()

s1.data.unstack()

s2=s1.unstack('number')


df = pd.DataFrame(
    [['A', 'X', 3], ['A', 'X', 5], ['A', 'Y', 7], ['A', 'Y', 1],
     ['B', 'X', 3], ['B', 'X', 1], ['B', 'X', 3], ['B', 'Y', 1],
     ['C', 'X', 7], ['C', 'Y', 4], ['C', 'Y', 1], ['C', 'Y', 6]],
    columns=['c1', 'c2', 'v1'])
print(df)

def callback(x):
    x['seq'] = range(1, x.shape[0] + 1)
    return x
df = df.groupby(['c1', 'c2']).apply(callback)
print(df)

