# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:47:37 2016

@author: n393637
"""
import numpy as np, pandas as pd
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
'B' : ['one', 'one', 'two', 'three',
'two', 'two', 'one', 'three'],
'C' : np.random.randn(8),
'D' : np.random.randn(8)})


#==============================================================================
# df
# Out[52]: 
#      A      B         C         D
# 0  foo    one  0.005469  1.090924
# 1  bar    one -1.062572  0.319766
# 2  foo    two -2.035521  0.050693
# 3  bar  three  0.521742 -2.709764
# 4  foo    two  0.972318  1.004795
# 5  bar    two  0.631277 -1.149338
# 6  foo    one -1.571251  0.289953
# 7  foo  three  1.268612 -0.854561
# 
#==============================================================================
def get_letter_type(letter):
    if letter.lower() in 'aeiou':
        return 'vowel'
    else:
        return 'consonant'

grouped = df.groupby(get_letter_type, axis=1)

grouped.groups

#Out[51]: {'consonant': ['B', 'C', 'D'], 'vowel': ['A']}


lst = [1, 2, 3, 1, 2, 3]
s = pd.Series([1, 2, 3, 10, 20, 30], lst)
s
#==============================================================================
# Out[67]: 
# 1     1
# 2     2
# 3     3
# 1    10
# 2    20
# 3    30
# dtype: int64
#==============================================================================
# grouped = s.groupby(level=0)
# grouped.sum()
# Out[68]: 
# 1    11
# 2    22
# 3    33
# dtype: int64
#==============================================================================

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
           ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
s = pd.Series(np.random.randn(8), index=index)
#==============================================================================
# Out[77]: 
# first  second
# bar    one       0.389129
#        two      -0.494269
# baz    one       0.483215
#        two      -0.590473
# foo    one      -0.965358
#        two      -0.823181
# qux    one      -0.589662
#        two       0.919487
# dtype: float64
#==============================================================================
s.groupby(level=1).sum()
#==============================================================================
# second
# one   -0.682676
# two   -0.988436
# dtype: float64
#==============================================================================
#use label ref
s.groupby(level='first').sum()
#==============================================================================
# Out[81]: 
# first
# bar   -0.105140
# baz   -0.107259
# foo   -1.788539
# qux    0.329826
# dtype: float64 
#==============================================================================


f=grouped['consonant']

df = pd.DataFrame({"a":[1,1,3], "b":[4,5.5,6], "c":[7,8,9], "name":["hello","hello","foo"]})
#==============================================================================
# Out[102]: 
#    a    b  c   name
# 0  1  4.0  7  hello
# 1  1  5.5  8  hello
# 2  3  6.0  9    foo
#==============================================================================
df.groupby(["a", "name"]).median()

df.groupby(["a", "name"]).median().index.get_level_values(1)
df.groupby(["a", "name"]).median().index.get_level_values('name')

#==============================================================================
## Create an example dataframe
# data = {'Platoon': ['A','A','A','A','A','A','B','B','B','B','B','C','C','C','C','C'],
#        'Casualties': [1,4,5,7,5,5,6,1,4,5,6,7,4,6,4,6]}
# df = pd.DataFrame(data)
# 
# df.groupby('Platoon')['Casualties'].count()
# df.groupby('Platoon')['Casualties'].apply(lambda x:x.rolling(center=False,window=2).mean())
#==============================================================================
df

grouped = df.groupby('A')
grouped_C = grouped['C']
grouped_C.count()

for k,v  in grouped.groups.items():
    print(k, v)
    
for name, group in grouped:
    print(name )   #string
    print(group ) #dataframe

grouped.get_group('bar')

#sums values for each column
grouped.aggregate(np.sum)
grouped['C'].sum()
grouped.describe()
grouped['C'].agg([np.sum, np.mean, np.std])

index = pd.date_range('10/1/1999', periods=1100)
ts = pd.Series(np.random.normal(0.5, 2, 1100), index)
ts = ts.rolling(window=100,min_periods=100).mean().dropna()



