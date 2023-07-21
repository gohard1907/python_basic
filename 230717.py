# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:13:59 2023

@author: Jung
"""

x = 10
y = 11

def fool():
    x = 20
    def bar():
        a = 30
        print(a, x, y)
    bar()
    x = 40
    bar()

fool()


g = 10
def f():
    global g
    a = g
    g = 20
    return a

print(f())
print(g)


def outer():
    x = 1 #L, E
    def inner():
        nonlocal x
        x = 2
        print('inner : ', x)
    inner()
    print('outer : ', x)
    
outer()   
    
    
def makeCounter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter 
    
c1 = makeCounter()
print(c1())

    
def makeCounter():
    count = []
    def counter():
        count.append(1)
        return count
    return counter    
    
c1 = makeCounter()
print(c1())    
    
'''    
def makeCounter():
    count = []
    def counter():
        count += [1]
        return count
    return counter    
    
 c2 = makeCounter()
 c2()   
'''   
    
def quadratic(a, b, c):
    #This is the outer enclosing fuction
    cache = {}
    def f(x):
        #This is the nested fuction
        if x in cache: # x = 1, 1 in cache, cache = {}, False
            return cache[x]
        y = a*x*x + b*x + c
        cache[x] = y
        return y
    return f #returns the nested fuction

f1 = quadratic(1, 2, 1)
print(f1(1))
f2 = quadratic(1, 6, 9)
print(f2(1))    
    
    
def divisor(n):
    divisors = []
    for i in range (1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors    
    
result = divisor(6)
print(result)


def add(n):
    sums = 0
    for i in range(n+1):
        sums += i
    return sums    
    
print(add(10))


def add_recur(n):
    if n == 1:
        return 1
    return n + add_recur(n-1)    
    
print(add_recur(10))


def c_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a  

print(c_divisor(78696, 19332))    

