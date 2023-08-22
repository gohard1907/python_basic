# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:30:41 2023

@author: Jung
"""

# 7-02

## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear != SIZE-1) :
        return False
    elif (rear == SIZE-1 and front == -1) :
        return True
    elif (rear == SIZE-1 and front != -1) : # else
        for i in range(front+1, SIZE, 1) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpety() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpety()) :
        print('큐 텅~')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpety()) :
        print('큐 텅~')
        return
    return queue[front+1]

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front=rear=-1

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')

retData = deQueue()
print('손님 이리로==>', retData)
retData = deQueue()
print('손님 이리로==>', retData)

print('출구<--', queue, '<--입구')

enQueue('재남')
enQueue('정국')

print('출구<--', queue, '<--입구')

enQueue('길동')

print('출구<--', queue, '<--입구')


# 7-03

## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if ( (rear+1) % SIZE == front) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def isQueueEmpety() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpety()) :
        print('큐 텅~')
        return
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpety()) :
        print('큐 텅~')
        return
    return queue[ (front+1) % SIZE]

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front=rear=0

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')

retData = deQueue()
print('손님 이리로==>', retData)
retData = deQueue()
print('손님 이리로==>', retData)

print('출구<--', queue, '<--입구')
#
enQueue('재남')
enQueue('정국')
#
print('출구<--', queue, '<--입구')

enQueue('길동')

print('출구<--', queue, '<--입구')


# 8-01

## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
        
## 변수


## 메인
node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()
node6.data = '선미'
node3.left = node6

root = node1

#print(node1.data)
#print(node2.data, node3.data)
#print(node4.data, node5.data, node6.data)

print(root.data)
print(root.left.data, root.right.data)
print(root.left.left.data, root.left.right.data, root.right.left.data)


# 8-02

## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 변수
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '에이핑크', '걸스데이', '트와이스', '마마무'] # 여러분 데이터

## 메인
node1 = TreeNode()
node1.data = nameAry[0]
root = node1
memory.append(node1)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    
    current = root
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
            
    memory.append(node)
    
print('이진 탐색 트리 구성 완료')

findData = '마마무'
#findData = '바바부'
current = root
while True:
    if findData == current.data:
        print(findData, '찾았음!')
        break
    elif findData < current.data:
        if current.left == None:
            print(findData, '없음')
            break
        current = current.left
    else:
        if current.right == None:
            print(findData, '없음')
            break
        current = current.right


# 9-01

## 함수
class Graph():
    def __init__(self, size):
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        
## 변수
G1 = None
A, B, C, D = 0, 1, 2, 3

## 메인
G1 = Graph(4)
G1.graph[A][B] = 1; G1.graph[A][C] = 1; G1.graph[A][D] = 1
G1.graph[B][A] = 1; G1.graph[B][C] = 1
G1.graph[C][A] = 1; G1.graph[C][B] = 1; G1.graph[C][D] = 1
G1.graph[D][A] = 1; G1.graph[D][C] = 1

for i in range(4):
    for j in range(4):
        print(G1.graph[i][j], end = ' ')
    print()


# 11-01

## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx

## 변수
testAry = [55, 88, 33, 77, 11, 99, 8, 4]

## 메인
minPos = findMinIndex(testAry)
print('제일 작은 값 : ', testAry[minPos])


# 11-02
## 함수
import random
def findMinIndex(ary) :
    minIdx = 0
    for i in range(1, len(ary)) :
        if (ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx

## 변수
before = [random.randint(30, 190) for _ in range(8)]
after = []

## 메인
print('정렬 전 -->', before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후 -->', after)


## 11-03

##함수
import random
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for j in range(i+1, n):
            if ary[minIdx] > ary[j]:
                minIdx = j
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return ary

##변수
dataAry = [random.randint(30, 190) for _ in range(8)]

##메인
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)


#13-01

## 함수
import random
def seqSearch(ary, fData):
    pos = -1
    for i in range(len(ary)):
        if ary[i] == fData:
            pos = i
            break
    return pos

## 변수
dataAry = [random.randint(30, 190) for _ in range(8)]
findData = random.choice(dataAry)
#findData = 999

## 메인
print('배열 :', dataAry)
position = seqSearch(dataAry, findData)
if position == -1:
    print(findData, '는 없어요')
else:
    print(findData, '는', position, '위치에 있어요')
    
    
#13-02

## 함수
import random
def binSearch(ary, fData):
    global count
    pos = -1
    start = 0
    end = len(ary)-1
    while start <= end:
        count += 1
        mid = (start + end) // 2
        if ary[mid] == fData:
            pos = mid
            break
        elif ary[mid] < fData:
            start = mid + 1
        else:
            end = mid - 1
    return pos

## 변수
count = 0
dataAry = [random.randint(0, 999999999) for _ in range(10000000)]
findData = random.choice(dataAry)
dataAry.sort()

## 메인
print('배열 :', dataAry[:20])
position = binSearch(dataAry, findData)
if position == -1:
    print(findData, '는 없어요')
else:
    print(findData, '는', position, '위치에 있어요 (', count, '회)')


# 14-01
'''
## 함수
def openBox():
    print('상자를 엽니다')
    openBox()
    
## 메인
openBox()
'''

# 14-02

## 함수
def openBox():
    global count
    print('상자 열기')
    count -= 1
    if count == 0:
        print('## 선물 넣기 ##')
        return
    openBox()
    print('상자 닫기')
    
    
## 메인
count = 10
openBox()


# 14-03

## 함수
def addNumber(num):
    if num == 1:
        return 1
    return num + addNumber(num-1)

## 메인
print(addNumber(100))


# 14-04

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(5))


# 14-05

def countDown(n):
    if n == 0:
        print('발사!')
    else:
        print(n)
        countDown(n-1)

countDown(5)


# 14-06

def printStar(n):
    if n > 0:
        printStar(n-1)
        print('★' * n)

printStar(5)


# 14-07

def gugu(dan, num):
    print('%d x %d = %d' % (dan, num, dan*num))
    if num < 9:
        gugu(dan, num+1)
        
for dan in range(2, 10):
    print('## %d단 ##' % dan)
    gugu(dan, 1)


# 14-08

tab = ''
def pow(x, n):
    global tab
    tab += ' '
    if n == 0:
        return 1
    print(tab + '%d*%d^(%d-%d)' % (x, x, n, 1))
    return x * pow(x, n-1)

print('2^4')
print('답-->', pow(2, 4))


# 14-09

import random
def arySum(arr, n):
    if n <= 0:
        return arr[0]
    return arySum(arr, n-1) + arr[n]

ary = [random.randint(0, 255) for _ in range(random.randint(10, 20))]
print(ary)
print('배열 합계-->', arySum(ary, len(ary)-1))
