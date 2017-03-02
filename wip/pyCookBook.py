import os
import sys
#print(os.environ)
#==============================================================================
# print(sys.argv)
# l=[1,2]
# for n in range(10):
#     l.append(l[-1]+l[-2])
# 
# a,b= 0,1
#==============================================================================
#while b <10:
#    a,b= b, a+b


def fib(n):
    """ output series """
    l=[]
    a,b=0,1
    while b <n:
        l.append(b)
        a,b=b, a+b
    return l

fib(20)
for n in range(2,10):
    for x in range(2,n):
        if n % x ==0:
            print(n, 'no')
            break
    else:
        print(n, ' is')
        
f= fib
f(20)

def ts (a,l=[]):
    l.append(a)
    return l
print(ts(1))
print(ts(2))
print(ts(3))
def ts(a,l=None):
    if l is None:
        l=[]
    l.append(a)
    return a
print(ts(1))
print(ts(2))
print(ts(3))


def ts(**keywords):
    for k,v in keywords.items():
        print(k,v)

ts(site1=20,site2=30,site3=40)
r=[3,6]
[n for n in range(*r)]

# In[]
al = [66.25, 333, 333, 1, 1234]
t, *v=al
[(a,b) for a in al for b in range(5)]    
    
# In[]
from collections import deque
l= [n **2 for n in range(20)]
d=deque(maxlen=10)
d.extend(l)
# In[]
import heapq, random
l=[random.randint(1,100) for n in range(10)]
heapq.nlargest(3,l) # largest 3 items from list
heapq.nsmallest(3,l) # smallest

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

c=heapq.nsmallest(3,portfolio,key=lambda s: s['price'])

# In[]
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index=0
        
    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index +=1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def lgst(self, n):
        return heapq.nlargest(n,self._queue, lambda s: s[0])

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

# In[]
q=PriorityQueue()
q.push(Item('bla'),1)
q.push(Item('foo'), 1)
q.push(Item('fan'), 12)
q.push(Item('ban'), 33)
q.push(Item('can'), 3)

q.lgst(2)

# In[]
# dict key refernces multiple values
from collections import defaultdict
d=defaultdict(list)
d[1].append(11)
d[1].append(12)
d[2].append(13)
d[2].append(14)
d[2].append(15)
# In[]
#order in dictionaries
from collections import OrderedDict



        
        
        
        
