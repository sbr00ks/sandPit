# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 11:11:59 2016

@author: n393637
"""

import re

re.search(r'(ab)+c',r'ababac') # group any number of 'ab' repetions  'c'
# use groups when have meaningful subpatterns inside the main pattern

re.search('Espan(a|ol)','Espanol')

re.search('Espan(a|ol)','Espana') # matches Espan with a or ol

#groups also capture the matched pattern so that you can use them later

#product id digits representing the country of the product, - seperator  and alpha chars as ID

pattern= re.compile(r'(\d+)-\w+')
it = pattern.finditer(r"1-a\n20-baer\n34-afcr")
match =it.next()
print(match.group(0)) # returns 1-a
print(match.group(1)) # returns only the 1
match2 =it.next()
print(match2.group(0)) # returns 20-baer
print(match2.group(1)) # returns only the 20
match3=it.next()
print(match2.group(0)) # you get the idea
print(match3.group(1)) #returns only 34

#can use the captured group inside the regex or other operations
#can use it to find duplicated words

v=re.search(r'(ab)+c',r'ababc')
v.group(1)


pattern = re.compile(r"(\w+) \1")
#note the \1 at the end. Backrefence  means it must exactly match  the same thing as the first group

match=pattern.search('davy davy manch davy')

match.groups()


pattern = re.compile(r"(\d+)-(\w+)")

pattern.sub(r"\2-\1", "1-a\n20-baer\n34-afcr")

pattern = re.compile(r"(\w+) (\w+)") # two groups
match=pattern.search('Hello world')
print(match.group(0)) # all groups
print(match.group(1)) #first group
print(match.group(2)) #second group

#named groups 
pattern = re.compile(r"(?P<first>\w+) (?P<second>\w+)")
match=re.search(pattern,'Hello world')
match.group('second')
match.group('second','second')

pattern = re.compile(r"(?P<country>\d+)-(?P<id>\w+)")

pattern.sub(r'\g<id>-\g<country>', '1-a\n20-baer\n34-afcr')

#==============================================================================
#Look Ahead 
#==============================================================================

pattern = re.compile(r'fox')
result = pattern.search("The quick brown fox jumps over the lazy dog")

print result.start(), result.end()
#16 19
pattern = re.compile(r'(?=fox)') #lookahead assertion
result = pattern.search("The quick brown fox jumps over the lazy dog")
print result.start(), result.end()
#16 16

#lookahead does not consume any characters and can be used to filter where
#the expression should match

pattern = re.compile(r'\w+(?=,)') #any word followed by a comma
pattern.findall("They were three: Felix, Victor, and Carlos.")
#Out[89]: ['Felix', 'Victor']

#do it the standard way get the comma included
pattern = re.compile(r'\w+,')
pattern.findall("They were three: Felix, Victor, and Carlos.")
['Felix,', 'Victor,']

#lookahead for any delimiter
pattern = re.compile(r'\w+(?=,|\.)')
pattern.findall("They were three: Felix, Victor, and Carlos.")
#['Felix', 'Victor', 'Carlos']

#==============================================================================
# Negative Look Ahead
#==============================================================================
pattern = re.compile(r'John(?!\sSmith)')  # ?1 John whitespace Smith

result = pattern.finditer("I would rather go out with John McLane than with John Smith or John Bon Jovi")

for i in result:
    print(i.start(), i.end())
    
#==============================================================================
#Look around and substitution 
#==============================================================================
#look ahead substitution could be used for conversion of numeric characters such as 
# 6323332     into 6,323,332
#to do this need to group numbers into blocks of three that will be
#substituted by the same group plus a comma character
    
pattern = re.compile(r'\d{1,3}')
pattern.findall("The number is: 1234556789")
#['123', '455', '678', '9'] doesn't work


#==============================================================================
# Look Behind
#==============================================================================

pattern = re.compile(r'(?<=John\s)McLane')
result = pattern.finditer("I would rather go out with John McLane than with John Smith or John Bon Jovi")

for i in result:
    print i.start(), i.end()





    
    
    
    
    
    
    
















