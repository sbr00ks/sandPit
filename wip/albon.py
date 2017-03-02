# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 09:31:28 2017

@author: n393637
"""
# In[]

import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import re

# In[]

#==============================================================================
# apply function to DF by Group
#==============================================================================
data = {'col1': ['A','A','A','A','A','A','B','B','B','B','B','C','C','C','C','C'],
'col2': [1,4,5,7,5,5,6,1,4,5,6,7,4,6,4,6]}

df01=DataFrame(data)
df01.groupby('col1')['col2'].mean()

#==============================================================================
# create new column
#==============================================================================
#new column needs to match length of index
df['newCol']=['in1','in2','in3','in4','in5']
df['newerCol']=list(df.name)


# In[]
#==============================================================================
# apply operations to groups
#==============================================================================
data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons',
'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
'postTestScore': [5, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

df02 = pd.DataFrame(data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])

gb=df02['preTestScore'].groupby(df02['company'])
gb.describe()

df02['preTestScore'].groupby([df02['regiment'], df02['company']]).mean()

df02.groupby(['company','regiment']).mean()

#observation counts
df02.groupby(['company','regiment']).size().unstack()

#==============================================================================
# apply operations over df
# apply()  - apply function along any axis
#==============================================================================
data = {'name': ['sando', 'davyh', 'presto', 'carli', 'widnes'],
'year': [2012, 2012, 2013, 2014, 2014],
'reports': [4, 24, 31, 2, 3],
'coverage': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, index = ['Coc', 'Pim', 'San', 'Mar', 'Tum'])

df.name.str.upper()

cap=lambda x : x.upper()

df.name.apply(cap)

#map() applies an operation over each element of a series
df.name.map(cap)

df.drop('name', axis=1,inplace=True)

#apply function over a dataframe
df.applymap(np.sqrt)

div2= lambda x : x/2

df.applymap(div2)
#function that multiplies all non strings by 100

def timHun(x):
    if type(x) is str:
        return x
    else:
        return x* 100

df.applymap(timHun)

#==============================================================================
# binning
#==============================================================================
bins = [0, 25, 50, 75, 100]
group_names = ['Low', 'Okay', 'Good', 'Great']

s1=pd.cut(df02['postTestScore'],bins,labels=group_names)

#==============================================================================
# breaking string into columns
#==============================================================================

# Create a dataframe with a single column of strings
data = {'raw': ['Arizona 1 2014-12-23 3242.0',
'Iowa 1 2010-02-23 3453.7',
'Oregon 0 2014-06-20 2123.0',
'Maryland 0 2014-03-14 1123.6',
'Florida 1 2013-01-15 2134.0',
'Georgia 0 2012-07-14 2345.6']}
df = pd.DataFrame(data, columns = ['raw'])

df['raw'].str.contains('....-..-..', regex=True)

df['fale'] = df['raw'].str.extract('(\d)', expand=True)
df['fale']
df['date'] = df['raw'].str.extract('(....-..-..)', expand=True)
df['score'] = df['raw'].str.extract('(\d\d\d\d\.\d)', expand=True)
df['state'] = df['raw'].str.extract('([A-Z]\w{0,})', expand=True)

#==============================================================================
# convert categorical into dummy
#==============================================================================

#check can use this for sludge stuff

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
'cat': ['male', 'female', 'male', 'female', 'female']}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'cat'])

df_cat = pd.get_dummies(df['cat'])

df_new = pd.concat([df, df_cat], axis=1)



#==============================================================================
# convert numerical categorical variable wit patsy
#==============================================================================
raw_data = {'areaCode': [1, 2, 3, 2, 1]}
df = pd.DataFrame(raw_data, columns = ['areaCode'])

# Convert the areacode variable into three binary variables
patsy.dmatrix('C(areaCode)-1', df, return_type='dataframe')

#==============================================================================
# convert string categorical to numeric
#==============================================================================
raw_data = {'patient': [1, 1, 1, 2, 2],
'obs': [1, 2, 3, 1, 2],
'treatment': [0, 1, 0, 1, 0],
'score': ['strong', 'weak', 'normal', 'weak', 'strong']}
df = pd.DataFrame(raw_data, columns = ['patient', 'obs', 'treatment', 'score'])

def score_to_numeric(x):
    if x=='strong':
        return 3
    if x=='normal':
        return 2
    if x=='weak':
        return 1
    
df['bla']=df.score.apply(score_to_numeric)

#==============================================================================
#convert variable to time 
#==============================================================================

# Create a dataset with the index being a set of names
raw_data = {'date': ['2014-06-01T01:21:38.004053', '2014-06-02T01:21:38.004053', '2014-06-03T01:21:38.004053'],
'score': [25, 94, 57]}
df = pd.DataFrame(raw_data, columns = ['date', 'score'])


df["date"] = pd.to_datetime(df["date"])


# In[]
#==============================================================================
# count values in df
#==============================================================================
year = pd.Series([1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884,
1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894])
guardCorps = pd.Series([0,2,2,1,0,0,1,1,0,3,0,2,1,0,0,1,0,1,0,1])
corps1 = pd.Series([0,0,0,2,0,3,0,2,0,0,0,1,1,1,0,2,0,3,1,0])
corps2 = pd.Series([0,0,0,2,0,2,0,0,1,1,0,0,2,1,1,0,0,2,0,0])
corps3 = pd.Series([0,0,0,1,1,1,2,0,2,0,0,0,1,0,1,2,1,0,0,0])
corps4 = pd.Series([0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0])
corps5 = pd.Series([0,0,0,0,2,1,0,0,1,0,0,1,0,1,1,1,1,1,1,0])
corps6 = pd.Series([0,0,1,0,2,0,0,1,2,0,1,1,3,1,1,1,0,3,0,0])
corps7 = pd.Series([1,0,1,0,0,0,1,0,1,1,0,0,2,0,0,2,1,0,2,0])
corps8 = pd.Series([1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1])
corps9 = pd.Series([0,0,0,0,0,2,1,1,1,0,2,1,1,0,1,2,0,1,0,0])
corps10 = pd.Series([0,0,1,1,0,1,0,2,0,2,0,0,0,0,2,1,3,0,1,1])
corps11 = pd.Series([0,0,0,0,2,4,0,1,3,0,1,1,1,1,2,1,3,1,3,1])
corps14 = pd.Series([ 1,1,2,1,1,3,0,4,0,1,0,3,2,1,0,2,1,1,0,0])
corps15 = pd.Series([0,1,0,0,0,0,0,1,0,1,1,0,0,0,2,2,0,0,0,0])

variables = dict(guardCorps = guardCorps, corps1 = corps1,
corps2 = corps2, corps3 = corps3, corps4 = corps4,
corps5 = corps5, corps6 = corps6, corps7 = corps7,
corps8 = corps8, corps9 = corps9, corps10 = corps10,
corps11 = corps11 , corps14 = corps14, corps15 = corps15)

horsekick = pd.DataFrame(variables, columns = ['guardCorps',
'corps1', 'corps2',
'corps3', 'corps4',
'corps5', 'corps6',
'corps7', 'corps8',
'corps9', 'corps10',
'corps11', 'corps14',
'corps15'])

horsekick.index = [1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884,
1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894]

result = horsekick.apply(pd.value_counts).fillna(0); result




# In[]

#==============================================================================
# create a column based on conditional
#==============================================================================
data = {'name': ['davyh', 'carli', 'sando', 'widne', 'runco'],
'assetAge': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, 2, 3],
'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, columns = ['name', 'assetAge', 'preTestScore', 'postTestScore'])

# Create a new column where the value is yes
# if df.age is greater than 50 and no if not
df['assetRefurb'] = np.where(df['assetAge']>=50, 'yes', 'no')

#==============================================================================
# Update a column based on conditional
#==============================================================================
df.loc[(df.age >30) & (df.preTestScore>20),['name']]='reset'

#==============================================================================
#create column with a for loop 
#==============================================================================

assCap=[]
for row in df['preTestScore']:
    if row > 30:
        assCap.append('val1')
    elif row >20:
        assCap.append('val2')
    elif row >3:
        assCap.append('val3')
    else:
        assCap.append('fail')
        
df['conditionPass']=assCap

#==============================================================================
# create pipeline
#==============================================================================

def meanVal(inFrame, inCol):
    return inFrame.groupby(inCol).mean()

def ucase(inFrame):
    inFrame.columns = inFrame.columns.str.upper()
    return inFrame



df.pipe(meanVal,inCol='assetAge').pipe(ucase)

# In[]
#==============================================================================
# crosstabs
#==============================================================================
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons',
'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
'company': ['infantry', 'infantry', 'cavalry', 'cavalry', 'infantry', 'infantry', 'cavalry', 'cavalry','infantry',
            'infantry', 'cavalry', 'cavalry'],
'experience': ['veteran', 'rookie', 'veteran', 'rookie', 'veteran', 'rookie', 'veteran', 'rookie','veteran',
'rookie', 'veteran', 'rookie'],
'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'experience', 'name', 'preTestScore', 'postTestScore'])
df

pd.crosstab([df.company,df.regiment],df.experience)

df.corr()

# In[]
#==============================================================================
# expand cells containing lists into own column
#==============================================================================
data = {'name': ['sando', 'davyh', 'presto', 'carli', 'widnes'],
'year': [2012, 2012, 2013, 2014, 2014],
'reports': [4, 24, 31, 2, 3],
'coverage': [25, 94, 57, 62, 70],
'deltas':[['aa','bb'],['cc','dd'],['ee','ff'],['gg','hh'],['ii','jj']]}
df = pd.DataFrame(data, index = ['Coc', 'Pim', 'San', 'Mar', 'Tum'])

tags=df.deltas.apply(pd.Series)
tags=tags.rename(columns=lambda n : 'tag_' + str(n))

df2=pd.concat([df[:],tags[:]], axis=1)

#==============================================================================
#find max value / index for max value 
#==============================================================================
df.reports.max()
df.reports.idxmax()
df.year.unique



