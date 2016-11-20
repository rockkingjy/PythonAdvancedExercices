# -*- coding: utf-8 -*-
# float point 

a = 1000000000
for i in xrange(1):
    a = a + 0.000001
print a - 1000000000

print map(lambda x:2*x, range(20))

print type(map(lambda x:2*x, range(20)))

print filter(lambda x:x>5,range(20))

print [x for x in range(20) if x>5]

print reduce(lambda x,y:x+y,[47,11,42,13])

#Question 1
print reduce(lambda x,y:max(x,y),[47,11,42,13])

#Question 2
def fahrenheit(T):
    return ((float(9)/5)*T+32)

def celsius(T):
    return (float(5)/9)*(T-32)    

temp = (36.5,37,37.5,39)

F = map(fahrenheit,temp)
C = map(celsius,F)
print F
print C

#Question 3
print reduce(lambda x,y:x+y,map(lambda x:x, range(101)))
