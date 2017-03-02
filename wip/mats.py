# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:12:08 2016

@author: n393637
"""

import math

def deg2rad(n):
    l=[]
    for v in n:
        l.append(math.radians(v))
        print()
    return l        

chk=deg2rad([180,90,45,137])

print('degrees \n',chk)

math.radians(34)
math.degrees(34)

def rad2deg(n):
    l=[]
    
print(math.degrees(math.pi/3),'\n', 
      math.degrees(math.pi/6),'\n',
    math.degrees(math.pi/12))

import numpy as np

#need this for distance
from scipy.spatial import distance

a1=np.array([2,2,1])
a2=np.array([2,2,1])
#boom 3 4 5
dist = distance.euclidean(a1, a2)

a1*a2
a1=np.matrix([2,2,1])

a1.dot(a2)

def roots(a,b,c):
    D= (b*b -4*a*c) **0.5 #**.5 square root
    x_1=(-b + D)/ (2*a)
    x_2=(-b - D)/ (2*a)
    
    print('x1 : {0:.7f}'.format(x_1))
    print('x2 : {0:.7f}'.format(x_2))    

def roots(a, b, c):
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)
    print('x1: {0}'.format(x_1))
    print('x2: {0}'.format(x_2))    

roots(1,1,1)


#==============================================================================
# Plotting IPES  regression curves - see regressionGraph.py
#==============================================================================
#%cd 'Y:\\Users\\n393637\\Documents\\DevPython\\Assets'
import pandas as pd
import numpy as np
from numpy import exp, power, log

#P14 Waste regressionmodels for tetsing
#df=pd.read_csv('p14waste.csv')
#df.to_pickle('wasteP14RegressionPkl')
df = pd.read_pickle('wasteP14RegressionPkl')
df.columns
df['ELEMENT_CODE']=df.ELEMENT_CODE.astype('str')

from pylab import plot, show, xlabel, ylabel, title

def drawGraph(x,y):
    plot(x,y,marker='o')
    #xlabel('Yardstick')
    ylabel('Cost')
    title('Area Element code : \n' +  d['AREA_CODE'] + ' ' +d['ELEMENT_CODE'])
    show()
    
#generate points for curve and plot 
#todo add other stat methods 
d=df.ix[6].to_dict()

#datframe with C, M, E & combined
bla=s.loc[(s['AREA_CODE']=='W100') & (s['ELEMENT_CODE']=='200')]
#need some kind of itterows stuff.....
bla.loc[ bla['UCD_STAT_METHOD']=='LINEAR', ['curveCost']]= bla['INTERCEPT_NUM'] + (bla['YARDSTICK'] * bla['GRADIENT_NUM'] ) 

s=df.copy()

#put area element as parms
def genCurve():
    d=s.ix[88].to_dict()
    if d['UCD_STAT_METHOD'] == 'POWER-ADJ2':
        costDiff=abs(d['X_MAX_NUM'] -d['X_MIN_NUM'])  *.1
        print(costDiff)
        r= range(int(d['X_MIN_NUM']),int(d['X_MAX_NUM']),int(costDiff))
        f=[]
        for yardstick in r:
            cost=exp(d['INTERCEPT_NUM']) * power(yardstick, d['GRADIENT_NUM'] )  * d['POWER_ADJUST_FACTOR']
            f.append(cost)
        drawGraph(r,f)

genCurve()

#996 linear 89 power adj2 mean 950 1006 log  718 power
def genCurve2():
    #d=s.ix[1006].to_dict()
    #if d['UCD_STAT_METHOD'] == 'POWER-ADJ2':
    costDiff=abs(d['X_MAX_NUM'] -d['X_MIN_NUM'])  *.1
    print(costDiff)
    r= range(int(d['X_MIN_NUM']),int(d['X_MAX_NUM']),int(costDiff))
    f=[]
    
    for yardstick in r:

        if d['UCD_STAT_METHOD'] == 'POWER-ADJ2':
            cost=exp(d['INTERCEPT_NUM']) * power(yardstick, d['GRADIENT_NUM'] )  * d['POWER_ADJUST_FACTOR']
            f.append(cost)
            
        elif d['UCD_STAT_METHOD'] == 'LINEAR':
            cost=d['INTERCEPT_NUM'] + (yardstick * d['GRADIENT_NUM'] )
            f.append(cost)        
            
        elif d['UCD_STAT_METHOD'] == 'LOG':
            cost=log(yardstick) * d['GRADIENT_NUM'] + d['INTERCEPT_NUM']
            f.append(cost)        

        elif d['UCD_STAT_METHOD'] == 'POWER':
            cost=exp(d['INTERCEPT_NUM']) * power(yardstick, d['GRADIENT_NUM'] )
            f.append(cost)
            
        elif d['UCD_STAT_METHOD'] == 'MEAN':
            cost=d['INTERCEPT_NUM']
            f.append(cost)   
            
    drawGraph(r,f)

genCurve2()

 exp(s['INTERCEPT_NUM']) * power(s['YARDSTICK'], s['GRADIENT_NUM'] )  * s['POWER_ADJUST_FACTOR']
#linear calculating correct
s.loc[ s['UCD_STAT_METHOD']=='LINEAR', ['curveCost']]= s['INTERCEPT_NUM'] + (s['YARDSTICK'] * s['GRADIENT_NUM'] ) 

#log  calculating correct
s.loc[ s['UCD_STAT_METHOD']=='LOG', ['curveCost']]= log(s['YARDSTICK']) * s['GRADIENT_NUM'] + s['INTERCEPT_NUM']

#power calculating correct
s.loc[ s['UCD_STAT_METHOD']=='POWER', ['curveCost']]= exp(s['INTERCEPT_NUM']) * power(s['YARDSTICK'], s['GRADIENT_NUM'] )

#mean
s.loc[ s['UCD_STAT_METHOD']=='MEAN', ['curveCost']]= s['INTERCEPT_NUM']



from sympy import Symbol, factor, expand, pprint

x=Symbol('x')
y=Symbol('y')

expr = x**2 -y**2
factor(expr)
factors=factor(expr)
expand(factors)

expr=x**3 + 3*x**2*y + 3*x*y**2 + y**3




