# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:35:56 2023

@author: Jung
"""
# 3-01

## 함수 선언부

## 전역 변수부
katok = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부
print(katok)

## 데이터 추가 (모모가 1회)
katok.append(None)
katok[5] = '모모'
print(katok)

## 데이터 삽입 (3등 자리에 미나)
# 1단계 (빈칸 추가)
katok.append(None)
# 2단계 (한 칸씩 이동)
katok[6] = katok[5]
katok[5] = None
katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
# 3단계 (미나 삽입)
katok[3] = '미나'
print(katok)

## 데이터 삭제 (4등을 삭제)
# 1단계 (데이터 삭제)
katok[4] = None
# 2단계 (한 칸씩 앞으로 이동)
katok[4] = katok[5]
katok[5] = None
katok[5] = katok[6]
katok[6] = None
# 3단계 (마지막 칸 제거)
del(katok[6])
print(katok)


# 3-02

## 함수
def add_data(friend):
    # 1단계 : 빈 칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 친구 입력
    katok[kLen-1] = friend

def insert_data(position, friend):
    # 1단계 : 빈 칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 한 칸씩 옆으로 이동
    for i in range(kLen-1, position, -1): # 중요!
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계 : 친구 입력
    katok[position] = friend
    
def delete_data(position):
    # 1단계 : 데이터 삭제
    katok[position] = None
    kLen = len(katok)
    # 2단계 : 한 칸씩 앞으로 이동
    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    # 3단계
    del(katok[kLen-1])
        
## 전역
katok = []

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)

insert_data(3, '미나')
print(katok)

delete_data(4)
print(katok)



while True:
    
    select = int(input('선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> '))

    if (select == 1):
        data = input('추가할 데이터--> ')
        add_data(data)
        print(katok)
        
    elif (select == 2):
        pos = int(input('삽입할 위치--> '))
        data = input('추가할 데이터--> ')
        insert_data(pos, data)
        print(katok)

    elif (select == 3):
        pos = int(input('삭제할 위치--> '))
        delete_data(pos)
        print(katok)

    elif (select == 4):
        print(katok)
        break
        
    else:
        print('1~4 중 하나를 입력하세요.')
        continue


# 4-01

## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

## 전역


## 메인
node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

#newNode = Node()
#newNode.data = '재남'
#newNode.link = node2.link
#node2.link = newNode

node2.link = node3.link
del(node3)

current = node1
print(current.data, end = ' ')
while(current.link != None):
    current = current.link
    print(current.data, end = ' ')
print()

#print(node1.data, end=' ')
#print(node2.data, end=' ')
#print(node3.data, end=' ')
#print(node4.data, end=' ')
#print(node5.data, end=' ')

print(node1.data, end=' ')
print(node1.link.data, end=' ')
print(node1.link.link.data, end=' ')
print(node1.link.link.link.data, end=' ')
#print(node1.link.link.link.link.data, end=' ')
#print(node1.link.link.link.link.link.data, end=' ')

# 4-02

## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start):    
    current = start
    print(current.data, end = ' ')
    while(current.link != None):
        current = current.link
        print(current.data, end = ' ')
    print()

def insertNode(findData, insertData):
    global memory, head, pre, current
    # Case 1 : 하필 머리 앞에 삽입 (다현, 화사)
    if findData == head.data:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node) # 파이썬에선 필요 없음
        return
    # Case 2 : 중간 노드 앞에 삽입 (사나, 솔라)
    current = head
    while(current.link != None):
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node) # 파이썬에선 필요 없음
            return
    # Case 3 : 없는 노드 앞에 삽입 (재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node) # 파이썬에선 필요 없음
    return

def deleteNode(deleteData):
    global memory, head, pre, current
    # Case 1 : 하필 머리를 삭제 (다현)
    if deleteData == head.data:
        current = head
        head = head.link
        del current
        return
    # Case 2 : 중간 노드 삭제 (쯔위)
    current = head
    while(current.link != None):
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del current
            return
    # Case 3 : 없는 걸 지울 때 (재남)
    return

def findNode(findData):
    global memory, head, pre, current
    current = head
    if findData == current.data:
        return current
    while current.link != None:
        current = current.link
        if findData == current.data:
            return current
    return Node()
        
## 변수
memory = []
head, pre, current = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # 여러분의 데이터

## 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # 파이썬에선 필요 없음

for data in dataArray[1:]: # ['정연', '쯔위', ...]
    pre = node    
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node) # 파이썬에선 필요 없음

printNodes(head)

insertNode('다현', '화사') # 다현 앞에 화사를 삽입
printNodes(head)
insertNode('사나', '솔라')
printNodes(head)
insertNode('재남', '문별')
printNodes(head)
deleteNode('다현')
printNodes(head)
deleteNode('쯔위')
printNodes(head)
deleteNode('재남')
printNodes(head)
retNode = findNode('사나')
print(retNode.data, '뮤비가 나옵니다.')


# 6-01

## 함수


## 변수
stack = [None, None, None, None, None]
top = -1

## 메인
# Push()
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
print('바닥:', stack)
# Pop()
data = stack[top]
stack[top] = None
top -= 1
print('팝-->', data)
data = stack[top]
stack[top] = None
top -= 1
print('팝-->', data)
data = stack[top]
stack[top] = None
top -= 1
print('팝-->', data)
print('바닥:', stack)


# 6-2

## 함수
def isStackFull():
    global SIZE, stack, top
    if top == SIZE-1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if isStackFull():
        print('스택 꽉!')
        return
    else:
        top += 1
        stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False
    
def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 텅~')
        return
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data        
        
def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 텅~')
        return
    else:
        return stack[top]
    
    
## 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

## 메인
push('커피')
push('녹차')
#push('꿀물')
#push('콜라')
#push('환타')
#print('바닥:', stack)
#push('게토레이')
print('바닥:', stack)

retData = pop()
print('팝 데이터-->', retData)
print('다음 예정:', peek())
retData = pop()
print('팝 데이터-->', retData)
retData = pop()
print('팝 데이터-->', retData)
print('바닥:', stack)


SIZE = int(input('스택 크기를 입력하세요 ==> '))
stack = [None for _ in range(SIZE)]
top = -1
select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ')

while select != 'X' and select != 'x':
    if select == 'I' or select == 'i':
        data = input('입력할 데이터 ==> ')
        push(data)
        print('스택 상태 : ', stack)
    elif select == 'E' or select == 'e':
        data = pop()
        print('추출된 데이터 ==> ', data)
        print('스택 상태 : ', stack)
    elif select == 'V' or select == 'v':
        data = peek()
        print('확인된 데이터 ==> ', data)
        print('스택 상태 : ', stack)
    else:
        print('입력이 잘못됨')

    select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ')

print('프로그램 종료!')


# 7-01

## 함수


## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
# enQueue() : 삽입
rear += 1
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
rear += 1
queue[rear] = '문별'
print('출구<--', queue, '<--입구')
# deQueue() : 추출
front += 1
data = queue[front]
queue[front] = None
print('식사손님 :', data)
front += 1
data = queue[front]
queue[front] = None
print('식사손님 :', data)
front += 1
data = queue[front]
queue[front] = None
print('식사손님 :', data)
print('출구<--', queue, '<--입구')
