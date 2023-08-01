# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 16:55:48 2023

@author: Jung
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:38:02 2023

@author: Jung
"""

class A:
    def __init__(self, x):
        self.x = x
    def print_x(self):
        print(self.x)
        
class B(A):
    def setdata(self, y):
        self.y = y
    def print_y(self):
        print(self.y)
        
b_io = B(10)        
b_io.print_x()        
        
print([x for x in dir(b_io) if not x.startswith('__')])      
b_io.setdata(100)  
print([x for x in dir(b_io) if not x.startswith('__')])      
b_io2 = B(10)       
print([x for x in dir(b_io2) if not x.startswith('__')])      
b_io2.print_x()
b_io2.setdata(77)        
b_io2.print_y()        
print([x for x in dir(b_io2) if not x.startswith('__')])      
        
        
class Person:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone
    def __repr__(self):
        return f'<Person {self.name} {self.phone} >'        
        
class Employee(Person):
    #def __init__(self):
        #pass
    def setdata(self, position, salary):
        self.position = position
        self.salary = salary
    def print_info(self):
        print(self.name, self.phone)        
        
e1 = Employee('홍길동', 1984)        
e1.print_info()       
print([x for x in dir(e1) if not x.startswith('__')])   
e1.setdata('대리', 200)        
print([x for x in dir(e1) if not x.startswith('__')])   
#e2 = Employee()        
#print([x for x in dir(e2) if not x.startswith('__')])   
        
        
class Stack(list):
    push = list.append        
        
s = Stack()        
s.push(4)        
print(s)        
s.push(5)       
print(s)        
s = Stack([1, 2, 3])        
print(s)        
s.push(18)        
print(s)        
        
        
class Queue(list):
    enqueue = list.append
    def dequeue(self):
        return self.pop(0)        
        
q = Queue()        
q.enqueue(1)
q.enqueue(2)
print(q)        
q.dequeue()        
print(q)        
q = Queue([1, 2, 3, 4])        
print(q)        
        
        
class MyDict(dict):
    def keys(self):
        L = super().keys()
        return sorted(L)        
        
d = MyDict()       
print(d.keys())        
d = MyDict({10:100, 21:200, 3:300})        
print(d.keys())        
        
          
class Animal:
    def cry(self):
        print('...')

class Dog(Animal):
    def cry(self):
        print('멍멍')

class Duck(Animal):
    def cry(self):
        print('꽥꽥')

class Fish(Animal):
    pass        

for each in (Dog(), Duck(), Fish()):
    each.cry()

        
        
class OrderedList(list):
    def __init__(self, item):
        super().__init__(item)
        self.sort()
    def append(self, item):
        super().append(item)
        self.sort()
    def extend(self, item):
        super().extend(item)
        self.sort()        

L = OrderedList([3, 10, 2])
print(L)
L.append(5)
print(L)
L.extend((4, 8, 20))
print(L)
        
        
class Counter:
    def __init__(self, value=0, step=1):
        self.value = value
        self.step = step
    def incr(self):
        self.value += self.step
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f'{self.value}'        
        
c = Counter()
c.incr()
print(c)     
c.incr()
print(c)         
        
        
class Counter:
    def __init__(self, value=0, step=1):
        self.value = value
        self.step = step
    def incr(self):
        self.value += self.step
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f'{self.value}'
    def __call__(self):
        self.incr()
        return self.value        

c = Counter()
print(c())
print(c())


class Book:
    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"책 제목 : {self.title}")
        print(f"책 저자 : {self.author}")

book1 = Book()
book1.set_info('하얼빈', '김훈')
book1.print_info()

book2 = Book()
book2.set_info('채식주의자', '한강')
book2.print_info()

data_list = [('하얼빈', '김훈'), ('채식주의자', '한강'), ('어린왕자', '생텍쥐페리')]
for each in data_list:
    book3 = Book()
    book3.set_info(each[0], each[1])
    book3.print_info()



class Song:
    def set_song(self, title, genre):
        self.title = title
        self.genre = genre
    def print_song(self):
        print(f'노래제목 : {self.title}({self.genre})')

class Singer:
    def set_singer(self, name):
        self.name = name
    def hit_song(self, song):
        self.hits = song 
    def print_singer(self):
        print(f'가수이름 : {self.name}')
        #print(f'노래제목 : {self.song.title}({self.song.genre})')
        self.hits.print_song()

obj_song = Song()
obj_song.set_song('취중진담', '발라드')
obj_song.print_song()
obj_singer = Singer()
obj_singer.set_singer('김동률')
obj_singer.hit_song(obj_song)
obj_singer.print_singer()



class Personal(list):
    def __init__(self, name, dob, descs):
        self.name = name
        self.dob = dob
        self.append(descs)
    def present(self):
        print(self.name, ':', self.dob)
        print(self)

p1 = Personal('홍길동', '1990-08-01', '휴가 중')
p1.append('전화하지 마세요')
p1_dict = {p1.name:p1}

print(p1)
print(p1_dict)
p1.present()
p1_dict['홍길동'].append('소설 속 인물')
p1_dict['홍길동'].present()



def wrapper(func):
    def wrapped_func():
        print('====before====')
        func()
        print('====after====')
    return wrapped_func

def myfunc():
    print('     I am here')

result = wrapper(myfunc)
result()

@wrapper #decorator
def myfunc2():
    print('     me too')
myfunc2()


def makebold(fn):
    def wrapped():
        return '<b>'+fn()+'</b>'
    return wrapped

def makeitalic(fn):
    def wrapped():
        return '<i>'+fn()+'</i>'
    return wrapped

@makeitalic
@makebold
def say():
    return 'Hello'
print(say()) # f = makeitalic(makebold(say()))의 형태


def debug(fn):
    def wrapped(a, b): #fn과 동일한 인수를 적어준다
        print('debug', a, b)
        return fn(a, b) #함수 fn을 호출한다
    return wrapped    

@debug
def add(a, b):
    return a + b
print(add(1, 2))


def debug(fn):
    def wrapped(*args, **kwargs): 
        print('calling',fn.__name__, 'args = ', args, 'kwargs = ', kwargs)
        result = fn(*args, **kwargs)
        print('     result =', result)
        return result
    return wrapped

@debug
def add(a, b, c):
    return a + b + c
print(add(1, 2, 3))


def wrapper(func):
    def wrapped_func(*args):
        print('====before====')
        result = func(*args)
        print('====after====')
        return result
    return wrapped_func

@wrapper 
def myfunc4(a, b):
    print('I am here.')
    return a + b

result = myfunc4(10, 20)
print(result)


















