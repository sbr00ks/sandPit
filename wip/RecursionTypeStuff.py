# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:48:40 2016

@author: n393637
"""

import builtins
print(dir(builtins))

import os
d=dict(os.environ)
print(d)

class c1:
    def __init__(self,name):
        self.name =name
class c2(c1):
    def __init__(self, name):
        self.name=name*2
class c3:
    def __init__(self, name):
        self.name = name*3

d1={'c1':'dave','c2':'bill','c3':'frank'}
l1=['dave','bill','martin']
for v in l1:
    v= c3(v)
    

i2=c3('bill')
print(i1.name)

exec('i2=c3("bill")')



class FirstClass(int):
    def setData(self, value):
        self.data=value
    def display(self):
        print(self.data)
#    def __add__(self, other):
#        return self.data - other.data
        

class SecondClass(FirstClass):
    def display(self):
        print('current value %s' % self.data)

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data=value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return 'ThirdClass  %s' % self.data
    def mul(self,other):
        self.data *= other
    def display(self,x):
        return FirstClass.display(x) + 'bla'
        
                
i1= FirstClass()
i1.setData(33)
i1.display()
i3= FirstClass()
i3.setData(22)
i3.display()

i3 + i1


i2= SecondClass()
i2.setData(33)
i2.display()

i3= ThirdClass(33)

i3.age=55

list(i3.__dict__.keys())

i3.__dict__['data']
i2.__class__

class Facility(AttrDisplay):
    def __init__(self, siteName, siteType):
        self.siteName= siteName
        self.siteType= siteType
    #def __str__(self):
    #    #return 'Site name  %s  site code %s' % (self.siteName ,self.siteType)
    #    return str(self.__dict__.items())

s1=Facility('davyh','ww')    
s1.__dict__.items()
print(s1)
s2=Facility('leigh','sf')

#collection of objects in composite
class AllFacility(AttrDisplay):
    def __init__(self, *args):
        self.all= list(args)
    def addCapacity(self):
        for e in self.all:
            e.capacity= 99
    def showAll(self):
        for e in self.all:
            print(e)
    
coll=AllFacility(s1,s2)

coll.addCapacity()

print(coll)
for ob in coll:
    print(list(ob.__dict__.items()))
    
import classtools  
    
list(coll.__dict__.items())

coll.showAll()

help(pickle)


class simple:
    def f(self, val):
        self.val= val
        
class subsimp(simple):
    def f(self,val, plus):
        simple.f(self,val)
        self.val= self.val + '    ' + plus
c= subsimp()
c.f('ddd','hhh')
c.val



class Super:
    def method(self):
        print('in Super.method')

class Sub(Super):
    def method(self): # Override method
        print('starting Sub.method') # Add actions here
        Super.method(self) # Run default action
        print('ending Sub.method')

b= Sub()
b.method()


class Super:
    def hello(self):
        self.data1 = 'spam'
        
class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'
        
        
        
        
class Number:
    def __init__(self,start):
        self.start=start
    def __sub__(self,other):
        #return Number(self.start - other)
        return self.start - other
n=Number(5)
n1= n-2
n1.start

d.__len__()

        
class Stepper:
    def __getitem__(self,i):
        return self.data[i]

i1=Stepper()
i1.data='blak'
i1[2]

for v in i1:
    print(v)

s='deffe'
i=iter(s)
type(i)
next(i)

def mysum(l):
    #print(l)
    if not l:
        return 0
    else:
        return l[0] + mysum(l[1:])
        
l1=[1,2,3,4]
mysum(l1)

def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])

def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])

       
l2=['pea','run','est']

mysum(l2)

sum=0
while l1:
    sum += l1[0]
    l1 = l1[1:]


def sumtree(l):
    print(l)
    tot=0
    for x in l:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))

def sumtree(l): #breadth first explit queue alternative to recursion
    tot=0
    items=list(l)
    while items:
        front = items.pop(0)
        if not isinstance(front,list):
            tot+= front
         else:
            items[:0]= front
    return tot
    
L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))    

def sumtree(l):
    


L.append(43)        
L.extend([[44,44]])

L
dir(sumtree.__code__)

bla=sumtree


bl= L.reverse()


bla.count=35
            