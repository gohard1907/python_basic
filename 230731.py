# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:38:02 2023

@author: Jung
"""

class MyStr:
    def __init__(self, s):
        self.s = s
    def __add__(self, b):
        print('왼쪽에 있을 때만 사용해 주세요.')
        return self.s + b
    
s1 = MyStr('a:b:c')
print(s1)
print(s1 + ':d')

class MyStr:
    def __init__(self, s):
        self.s = s
    def __add__(self, b):
        return self.s + b    
    def __radd__(self, c):
        return c + self.s
    
s2 = MyStr('a:b:c')
print('z:' + s2 + ':d')


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def __add__(self, a):
        return self.first + self.second + a

    def __mul__(self, a):
        return self.first * self.second * a

    def __sub__(self, a):
        return self.first - self.second - a

    def __truediv__(self, a):
        return self.first / self.second / a
    
fc = FourCal(10, 5)
print(fc - 3)



class A:
    def __repr__(self):
        return('class A print')
class B:
    def __str__(self):
        return('class B print')
class C(A):
    def __str__(self):
        return('class C print')

c1 = A()
print(c1)
c2 = B()
print(c2)
c3 = C()
print(c3)


class StringRepr:
    def __repr__(self):
        return 'repr called'
    def __str__(self):
        return 'str called'
    
sr = StringRepr()
print(sr)
print(str(sr))
print(repr(sr))


class StringRepr:
    def __str__(self):
        return 'str called'

sr = StringRepr()
print(sr)
print(str(sr))
print(repr(sr))


class StringRepr:
    def __repr__(self):
        return 'repr called'

sr = StringRepr()
print(sr)
print(str(sr))
print(repr(sr))


print(eval('10 + 20')) #eval() 함수에 의하여 같은 객체로 재생성 될 수 있는 문자열 표현

a = '10 + 20'
print(eval(a))

b = '''print('abc')'''
eval(b)


class StringRepr:
    def __init__(self, i = 10):
        self.i = i
    def __repr__(self):
        return 'StringRepr(100)' #return이 아닌 print면 오류가 남

sr = StringRepr()
print(sr.i)

q = eval(repr(sr)) #repr(sr) == 'StringRepr(100), eval('StringRepr(100)')
print(q)
print(q.i)


class MyClass:
    def __init__(self, x = 10, y = 20):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'MyClass(x={self.x}, y={self.y})'

obj = MyClass(10, 20)
print(repr(obj))
print(obj)


class Accumulator:
    def __init__(self):
        self.sum = 0
    def __call__(self, *args):
        self.sum += sum(args)
        return self.sum

acc = Accumulator()
print(acc(1, 2, 3, 4, 5))
print(acc(6))
print(acc.sum)


class A:
    def __call__(self, v):
        return v

class B:
    def func(self, v):
        return v

def check(func):
    if callable(func):
        print('callable')
    else:
        print('not callable')

a = A()
b = B()
check(a)
check(b)
print(callable(a))
print(callable(b))



a = 10
result = 1
for item in range(1, a+1, 1):
    result *= item
print(result)

def my_fact(n):
    if n == 0:
        return 1
    else:
        return n * my_fact(n-1)

print(my_fact(10))

import math

class Factorial():
    def __call__(self, i):
        return math.factorial(i)

fact = Factorial()
for i in range(10):
    print(f'{i}! = {fact(i)}')



class MyStr:
    def __init__(self, word):
        self.word = word # word == "I like python and python"

    def __repr__(self):
        return (f"My_Str('{self.word}')")

    def __add__(self, a):
        return MyStr(self.word + ' ' + a) #word == "I like python and python  stuff"

    def __sub__(self, a):
        return MyStr(self.word.replace(a, '', 1)) #"I like python and python".replace('python', '', 1)

a = MyStr("I like python and python")
print(a)
b = a + "struff"
print(b)
c = a - "python"
print(c)



class Test_no_getitem:
    def __init__(self):
        print('생성자 __init__을 호출하였습니다. ')
        self._numbers = [ n for n in range(1, 11)]
        
a = Test_no_getitem()
print(a._numbers)
print(a._numbers[3])
#print(a[3])


class Test:
    def __init__(self):
        print('생성자 __init__을 호출하였습니다. ')
        self._numbers = [ n for n in range(1, 11)]

    def __getitem__(self, index):
        print('__getitem__ 을 호출하였습니다. ')
        return self._numbers[index]

a = Test()
print(a[3])
print(a[4])
#print(a[12])


class MyList:
    def __init__(self, items):
        self.items = items
    def __getitem__(self, indexs):
        if isinstance(indexs, int):
            return self.items[indexs]
        elif isinstance(indexs, str):
            return self.items.index(indexs)
        else:
            raise TypeError('잘못된 형식입니다.')

my_list = MyList(['red', 'blue', 'green', 'black']) #  items

# __getitem__ 의 파라미터가 list 일때 --> isinstance
print(my_list[0]) # 출력 : red
print(my_list[2]) # 출력 : green

# __getitem__ 의 파라미터가 string 일때 --> isinstance
print(my_list['red']) # 출력 : 0
print(my_list['green']) # 출력 : 2
#print(my_list[2.7])


class Square:
    def __init__(self, n):
        self.n = n
    def __getitem__(self, k): #반복자 for 문 사용이나 형변환시 오류발생 고려
        if 0 <= k <= self.n:
            return k*k
        raise IndexError('선을 넘었습니다.')
        
s = Square(10)
print(s[2]) # 4
print(s[3] )# 9
print(s[9]) # 81        
#print(s[21]) 
print(list(s))    



class Person:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone
    def __repr__(self):
        return f'<Person {self.name} {self.phone} >'

class Employee(Person):
    def __init__(self, name, phone, position, salary):
        #Person.__init__(self, name, phone)
        #super(Employee, self).__init__(name, phone)
        super().__init__(name, phone)

        self.position = position
        self.salary = salary

p1 = Person('홍길동', 1498)
print(p1)

e1 = Employee('손석구', 5564, '대리', 200)
print(e1)
print(e1.name)
print(e1.salary)
print(e1.position)


l1 = [x for x in dir(p1) if not x.startswith('__')]
print(l1)

l2 = [x for x in dir(e1) if not x.startswith('__')]
print(l2)


class Employee(Person):
    def __init__(self, name, phone, position, salary):
        super().__init__(name, phone)
        self.position = position
        self.salary = salary
    def __repr__(self):
        s = super().__repr__()
        return s + f'Employee {self.name} {self.phone} {self.position} {self.salary}'

e2 = Employee('손석구', 5564, '대리', 200)
print(e2)



import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return 0
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def __repr__(self):
        return f'x={self.x}, y={self.y}'

class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.radius = r
    def area(self):
        return math.pi * self.radius * self.radius
    def __repr__(self):
        return f'{super().__repr__()}, radius={self.radius}'

class Cylinder(Circle):
    def __init__(self, x, y, r, h):
        super().__init__(x, y, r)
        self.height = h
    def area(self):
        return 2 * Circle.area(self) + 2 * math.pi * self.radius * self.height
    def volume(self):
        return super().area() * self.height
    def __repr__(self):
        return f'{super().__repr__()}, height={self.height}'

p1 = Point(3, 5)
c1 = Circle(3, 4, 5)
c2 = Cylinder(3, 4, 5, 6)

print(p1)
print(c1)
print(c1.area)
print(c2)
print(c2.volume)
print(c2.area)
print(c2.volume() / c1.area())
c1.move(10, 10)
print(c1)


class Base:
    def f(self):
        self.g()
    def g(self):
        print('Base')

class Derived(Base):
    def g(self):
        print('Derived')

b = Base()
b.f()
d = Derived()
d.f()


class Job:
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary
    def __repr__(self):
        return f'Job position={self.position}, salary={self.salary}'
        
class Employee(Person, Job):
    def __init__(self, name, phone, position, salary):
        Person.__init__(self, name, phone)
        Job.__init__(self, position, salary)
    def __repr__(self):
        return Person.__repr__(self) + Job.__repr__(self)
    
e4 = Employee('손석구', 5564, '대리', 200)
print(e4)
print(Employee.mro()) #method resolution order