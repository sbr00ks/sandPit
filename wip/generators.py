# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# In[]
#%cd "Y:\Users\n393637\Documents"

#%cd "C:\\Users\\n393637\\Documents\\GitPortable\\Data\\home"
import numpy as np, itertools, random

a= np.random.random(15).reshape(3,5)

g= (np.random.random(15))

g=sum(e for e in a) # 
type(g)
iter(g)

# In[]
#brackets make gen a generator
gen=(random.randint(0,1) for i in range(10))
l=[]
for k,g in itertools.groupby(gen):
    print(k, list(g), type(g))
    l.append(k)
    if k and len(list(g)) >=4:
        #if k equivalent to if k==1
        success=True        
print(l)


#can do this more succinctly as...
# any() goes through the generator until it finds element that matches condition
success=any(k and len(list(g))>4 for k, g in 
            itertools.groupby(random.randint(0,1) for i in range(10)))   


# In[]
gen=(random.random() for i in range(10))
l=[n for n in range(10)]    
def ty(it):
    for e in it:
        yield str(e)

ty(l)
# In[]
def gs(n):
    for e in range(n):
        yield e **2

for e in gs(3):
    print(e)

for e in ty(l):
    print(e)

    
def gs(n):
    for e in range(n):
        yield e **2

        
# In[]
gen=(1,2,3,4)
gen=(e for e in range(4))

n=0
for e in gen:
   n+=e
   if n > 3:
       break
   print(n)
   
gen=(1,2,3,4)
tsum= sum(e for e in gen)
tsum= sum(e for e in gen)

g=(random.randint(0,1) for n in range(10))

for k, gr in itertools.groupby(g):
    print(k,' ',list(gr))
    if len(list(gr))>4:
        success=True
        
g=(random.randint(0,1) for n in range(10))        
t2=any( len(list(gr)) >4 for k, gr in itertools.groupby(g) )

def cnt():
    cnt=0
    for n in range(1000):
        g=(random.randint(0,1) for n in range(10))        
        t2=any( len(list(gr)) >4 for k, gr in itertools.groupby(g) )
        if t2== True:
            cnt+=1
    return cnt
    
l=[]
for n in range(1000):
    l.append(cnt())

lc=[x**2 for x in range(5)]

gc=(x**2 for x in range(5))

for e in gc:
    print(e)
    

     