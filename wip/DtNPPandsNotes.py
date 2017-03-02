
# coding: utf-8

# In[5]:

from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4)


# In[6]:

get_ipython().magic('pwd')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# In[8]:

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# In[7]:

arr2d[1,2]

# In[12]:

arr3d[0]
arr3d[1,0,2] #returned arrays are VIEWS

# In[14]:

arr2d


# In[21]:

arr2d[:2]


# In[5]:

l1 = ['davyh','cumwh','carls','leigh']

s1 = pd.Series(l1)
s1


# In[4]:

dates =pd.date_range('20150101', periods= 6)


# In[5]:

df =pd.DataFrame(np.random.randn(6,4), index = dates, columns = list('ABCD'))
#df


# In[11]:

df.dtypes


# In[15]:

df.index


# In[16]:

df.columns


# In[17]:

df.values


# In[26]:

df.B.describe()


# In[33]:

df.sort_index(axis=1, ascending = True) #1 horizontal 0 vertical sort


# In[34]:

df.sort(columns = 'B')


# In[35]:

df.ix[1:3,['A']]


# In[42]:

df[(df.A > 0.1) & (df.B <1.1)]


# In[43]:

df[df >0]


# In[6]:

df.where(df < 0) #same as the previous the where method is implicit


# In[7]:

df2 = df.copy()
#df2


# In[8]:

df2['E'] = ['one', 'one','two','three','four','three']
#df2


# In[63]:

df2[df2['E'].isin(['two','four'])]


# In[14]:

df2= df.copy()
#df2

# In[11]:

df2[df2 > 0] = -df2

# In[21]:

#boolean condition with setting
df2[ df2[1:4] > 0 ] = 3

# In[86]:

df.A.mean()


# In[88]:

df.mean(0)  #0 or 1 to select axis


# In[13]:

df3 = df.copy()
#df3.apply(np.cumsum)

s = pd.Series(np.random.randint(0, 7, size=10))

df4 =pd.Series(s)

df4.value_counts()


df = pd.DataFrame(np.random.randn(10, 4))


# In[113]:

pieces = [df[:3], df[3:7], df[7:]]
pieces


# In[112]:

type(pieces)


# In[114]:

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})


# In[115]:

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})


# In[116]:

pd.merge(left, right, on='key')


# In[117]:

dg = pd.DataFrame()

# In[125]:

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar','foo', 'foo'],
                   'B' : ['one', 'one', 'two','three','two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),'D' : np.random.randn(8)})


# In[128]:

df.groupby(['A','B']).count()


# See the Grouping section

# In[4]:

from pandas import Series
from pandas import DataFrame

s1 =Series(np.random.randn(5),index=[1,23,4,56,6])


# In[140]:

s1[[4,3,4]]


# In[142]:

x = s1+2
x


# In[148]:

s2 = Series(np.random.randn(6), index=[23,56,3,4,76,34])
s2


# In[5]:

d = {'one' : Series(np.random.randn(1), index=['a', 'b', 'c']),'two' : Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[6]:

df =DataFrame(d)
df


# In[166]:

df.index


# In[186]:

get_ipython().magic('pwd')


# In[187]:

get_ipython().magic('ls')


# In[195]:

path='tips2.csv'


# In[196]:

tips = pd.read_csv(path)


# In[22]:

#tips


# In[8]:

get_ipython().magic('ls')


# In[62]:

xy = pd.read_csv('tips2.csv')
#states = ['Texas', 'Utah', 'California']
#frame.reindex(columns=states)
#type(states)


# In[63]:

y = xy['total_bill']
z = xy['day']
l1 = list(y)
#z.reindex('29')
# In[19]:

xz = pd.Series[xy['day']]

s = pd.Series(np.random.randn(5), index=['aa', 'bb', 'cc', 'dd', 'ee'])

# In[85]:

i1= ['c', 'f', 'b']

# In[74]:

s.reindex(['e', 'b', 'f', 'd'])


# In[92]:

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'b', 'c', 'd', 'e'],columns=['one', 'three', 'two'])
#df.reindex(index=['c', 'f', 'b'], columns=['three', 'two', 'one'])
#df.reindex(index=i1, columns=['three', 'two', 'one'])
df


# In[86]:

rs = s.reindex(df.index)
rs


# In[97]:

#df.reindex(s.index)
df


# In[7]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[11]:

s1 = s[:4]
s1


# In[10]:

s2 = s[1:]
s2


# In[12]:

s1.align(s2)


# In[13]:

df.align(df2, join ='inner')


# In[ ]:




# In[ ]:

#filter and column selection in single statement
#frame.loc[frame['PRIMARY_DESIGN_VALUE']>20,['ARRANGEMENT_ID', 'PRIMARY_DESIGN_VALUE']]


# In[ ]:

#counts items in a list into dictionary
udc = defaultdict(int)
for x in time_zones:
    udc[x] +=1


# In[ ]:

#pretty print of dictionary
import pprint
pprint.pprint(counts.items())


#counting lists
from collections import Counter
counts = Counter(time_zones)
# In[38]:

#create array with any sequence like object
ls = [[1,2,3],[4,5,6],[7,8,9]]
arr= np.array(ls)
arr*3.141


# In[16]:

np.arange(5)  #np version of range function


# In[17]:

arr = np.arange(10)


# In[23]:

sl[1]= 12345


# In[24]:

sl


# In[25]:

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[0][0]


# In[26]:

arr2d[1][1] + 24


# In[28]:

arr2d[2,2]


# In[29]:

arr2d[2:,:1]


# In[32]:

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
names == 'Bob'


# In[34]:

data


# In[33]:

data[names == 'Bob']


# In[36]:

mask = (names == 'Bob') | (names == 'Will')
data[mask,2]


# In[40]:

arr


# In[42]:

arr[1:2,[0,1,2]]


# In[71]:

arr = np.arange(15).reshape((3, 5))


# In[49]:

arr.T #transpose array


# In[59]:

#np.exp(arr) #unary ufunc's perform elementwise opearations on ndarrays#
#np.sqrt(arr)
np.log(arr)


# In[58]:

#binary ufincs work on two or more ndarrays and returns single result
x =np.random.randn(8)
y=np.random.randn(8)
z = np.maximum(x,y)
z


# In[61]:

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = np.where(cond, xarr, yarr)  #where used to create new array of values based on another


# In[66]:

np.where(arr >1,4,99) #if value >1 return 4 else return 99


# In[73]:

arr.mean()
arr


# In[142]:

s = pd.Series(arr.mean(axis=0))


# In[145]:

#s.plot()


# In[80]:

arr.cumsum(1) #cumsum for rows axis = 1


# In[129]:

import matplotlib.pyplot as plt


# In[130]:

s = pd.Series(range(10))
s.plot()


# In[200]:

d = pd.DataFrame(np.arange(15).reshape((3, 5)))
d


# In[125]:

obj = pd.Series([4, 7, -5, 3])
obj.sort_index()
get_ipython().magic('pinfo obj.plot')


# In[131]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt


# In[201]:

#obj.plot()
d.index= ['a','b','c']


# In[155]:

pd.name='bla'


# In[161]:

obj.name='bla'
obj.index.name='baa'


# In[163]:

type(obj)


# In[184]:

d.columns= ['c1','c2','c3','c4','c5']
d.ix['b':,'c2']


# In[180]:

d


# In[189]:

d['debt']= 234


# In[192]:

d.columns


# In[193]:

d.T


# In[205]:

#d = d.T
d


# In[206]:

d2 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=['a','b','c'])
d2


# In[207]:

d.append(d2)


# In[208]:

get_ipython().magic('pinfo d.diff')


# In[12]:

pd.unstack()?


# In[14]:

get_ipython().magic('pinfo pd.MultiIndex')


# In[ ]:



