# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 09:22:24 2016

@author: n393637
"""
#%cd 'Y:\\Users\\n393637\\Documents\\DevPython\\Assets'
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd 
from numpy import exp, power, log, add
prjSecArEleDsc=pd.read_csv('p14WaterPrjsecareledsc.csv')

prjSecArEleDsc['ELEMENT_CODE']=prjSecArEleDsc.ELEMENT_CODE.astype('str')

tf1=prjSecArEleDsc[(prjSecArEleDsc.AREA_CODE=='A203') 
                    & (prjSecArEleDsc.ELEMENT_CODE=='874')
                    & (prjSecArEleDsc.DISC_CODE=='C')
                    ]                    
tf1.to_csv('A203-874.csv')

import random, re
random.seed(10)


#==============================================================================
# list comprehension
#==============================================================================
l=[n  for n in range(10)] 
fourl=[random.randint(0,100) for _ in range(4)]
def dl(i):
    return i*2
    
l2=[dl(i) for i in l]

#map same as list comprehension. Applies a function to each element
l2 =list(map(dl, l))


def dl(x,y):
    return x * y
#map with multiple inputs 
l3=list(map(dl,l,l2))

#filter does the work of  alist comprehension if

for i,v in enumerate(l2):
    print(i,v)
    
l3=[(i,v) for i,v in enumerate(l2)]

# pairs lists into tuples
l3=list(zip(l,l2))

#unzips tupls pairs into seperate lists
a,b=zip(*l3)

#can use unpacking anywhere
add(*[1,2])

def doubler(f):
    def g(x):
        return 2 * f(x)
    return g
    
def f1(x):
    return x +1

g=doubler(f1)

def mgc(*args,**kwargs):
    print('args  ',args)
    print('kwargs ',kwargs)

mgc(1,2,3,p='bolt',q='price')

def doubler_correct(f):
    def g(*args,**kwargs):
        return 2 * f(*args, **kwargs)
    return g
    
def f2(x,y):
    return x +y
    
g=doubler_correct(f2)

g(1,2)
def vectorAdd(x,y):
    return [xe + ye for xe,ye in zip(x,y)]

def vectorSubtract(x,y):
    return [xe - ye for xe,ye in zip(x,y)]   
    
vectorAdd(l,l2)

def vectorSum(vectors):
    result=vectors[0]
    for vector in vectors[1:]:
        result= vectorAdd(result, vector)
    return result
    
vectorSum([l,l2,l3])

l4= reduce(vectorAdd, [l,l2,l3])
#scaler multi

def scalarMultiple(s,v):
    return [s * ve for ve in v]

sMu(i,l)

def scalarMean(vectors):
    n=len(vectors)
    return scalarMultiple(1/n, vectorSum(vectors))

scalarMean([l,l2,l3])

def dot(v,w):
    return sum(v_i * w_i for v_i, w_i in zip(v,w))
    
v=[0,3]
w=[0,4]
    
dot(v,w)  #12

def sumofSquare(v):
    return dot(v,v)

sumofSquare(v)

from math import sqrt

def magnitude(v):
    return sqrt(sumofSquare(v))

magnitude(v)

def squaredDistance(v,w):
    return sumofSquare(vectorSubtract(v,w))
  
squaredDistance(v,w)

def distance(v,w):
    return sqrt(squaredDistance(v,w))

distance(v,w)

m1=[[22,23.5,45],[11,3,77],[9,9,35.7],[19.9,87,89]]

def shape(m):
    num_rows=len(m)
    num_cols=len(m[0])
    return num_rows,num_cols

shape(m1)

def get_row(A, i):
    return A[i] 

def get_column(A, j):
    return [A_i[j] for A_i in A]
    
def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i,j)th entry is entry_fn(i, j)"""
    return [
            [entry_fn(i, j) # given i, create a list
            for j in range(num_cols)] # [entry_fn(i, 0), ... ]
            for i in range(num_rows)] 

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)    

# In[ ]:
    