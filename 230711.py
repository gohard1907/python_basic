# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:03:10 2023

@author: Jung
"""

x = float(input('숫자를 입력하세요. : '))
print(x)

a = 3
if a > 2 :
    print('a는 2보다 큽니다.')
    
if a < 2 :
    print('a는 2보다 큽니다.')
else :
    print('a는 a 입니다.')
    
    
names = input('이름을 입력하세요.')

if names == '정은주' :
    print('본인입니다')
    
month = int(input('아이가 태어난 지 몇 개월입니까?'))

if month < 2 :
    print('결핵 예방접종 대상자입니다.')
    print('B형간염 예방접종 대상자입니다.')
if 2 <= month < 6 :
    print('B형간염 예방접종 대상자입니다.')
    print('파상풍 예방접종 대상자입니다.')
    print('폐렴구균 예방접종 대상자입니다.')
if 6 <= month < 15 :
    print('파상풍 예방접종 대상자입니다.')
    print('폐렴구균 예방접종 대상자입니다.')
if month >= 15 :
    print('폐렴구균 예방접종 대상자입니다.')
    
    
months = int(float(input('아이가 태어난 지 몇 개월입니까?')))

if months <= 1:
    print('결핵 예방접종 대상자입니다. ')
if 1 <= months <= 2:
    print('B형간염 예방접종 대상자입니다.')
if 2 <= months <= 6:
    print('파상풍 예방접종 대상자입니다.')
if 2 <= months <= 15:
    print('폐렴구균 예방접종 대상자입니다.')


age = 6

if age < 5 :
    print('OK')
elif age > 5 and age < 10 :
    print('ok, good')
else :
    print('NO')
print('여기는 조건문 밖입니다.')

if not age > 10 :
    print('ok')
    
    
fash = '맨발'
    
if not fash == '샌들양말' :
    print('모두 좋습니다.')
    
if 3 in [1, 2, 3] :
    print('ok')    
    

new_town_list = ['경기도', '서울', '대전', '광주']

if '수원' not in new_town_list:
    print('ok')

num1 = 10
num2 = 14
num3 = 21

if num1 > num2 and num1 > num3:
    print('최대값은 ', num1)
elif num2 > num1 and num2 > num3:
    print('최대값은 ', num2)
else:
    print('최대값은 ', num3)
    
year = 2023

cond1 = (year%4) == 0
cond2 = (year%100) != 0
cond3 = (year%400) == 0

case1 = cond1 and cond2 or cond3

if case1:
    print('leap year')
else:
    print('not leap year')


score = float(input('점수를 입력하세요.'))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

x = int(input('정수를 입력하세요'))

if x%2 == 0:
    print('x는 짝수입니다.')
else:
    print('x는 홀수입니다.')
    
x = int(input('자연수를 입력하세요'))

if x <= 0:
    print('자연수가 아닙니다.')
elif x%2 == 0:
    print('x는 짝수입니다.')
else:
    print('x는 홀수입니다.')


weight = float(input('몸무게를 입력하세요.'))
height = float(input('키를 입력하세요.'))

bmi = weight / (height/100)**2

if 18.5 > bmi:
    print('저체중입니다.')
elif 18.5 <= bmi <= 23:
    print('정상입니다.')
elif 23 < bmi <= 24.9:
    print('과체중입니다.')
elif 25 < bmi <= 29.9:
    print('비만입니다.')
else:
    print('고도비만입니다.')
    
    
s = 'Strings in Python'

s[0:17:1]
s[::2]    
s[0:17]    
s[2]    
len(s)


x_list = [1, 2, 3]
print(len(x_list))
print(x_list[-1])
print(x_list[2])
print(type(x_list[2]))
print(type(x_list[0:2]))

ms = 'No matter how the wind howls. The mountain cannot bow to it.'
print(len(ms))
print(ms[12])
print(ms[-1])
print(ms[::])
print(ms[::3])
print(ms[::-1])


for i in ms:
    print(i)


sample_list = [10, 20, 30, 40, 50, 60]

print(sample_list[0], sample_list[2], sample_list[5])
print(sample_list[:20])


sample_list = [10, [12, ms]]

print(sample_list)
print(sample_list[1][1][18:22])


test_list = [1, 3, 'test', ms, sample_list]

print(len(test_list))
print(test_list[-1][-1][-1][18:22])


x = range(0, 1000000000)

for i in x[:3]:
    print(i)

print(list(range(0, 10, 2)))

for i in range(len(test_list)):
    print(i, test_list[i])

for i in range(len('test_sentence')):
    print(i)
    
for i in test_list[2:]:
    print(i, len(i))
    
    
fav_color = ['파랑', '노랑', '검정']

for i in fav_color:
    print(i)

words = ['코딩', '파이썬', '데이터분석']

for i in words:
    print(i, len(i))
    
list2 = [1, 2, 3, 4, 5]

for i in list2[1:]:
    print(i)    


for i in range(0,11):
    print(i)

for i in range(5,16):
    print(i)
    
for i in range(0, 22):
    if i%2 == 0:
        print(i)

for i in range(-100, 101):
    if i%4 == 0:
        print(i)
        

total = 0

for i in range(1,101):
    total += i
print(total)

total2 = 1

for i in range(1,11):
    total2 *= i
print(total2)

x = 2

for i in range(1, 10):
    print(x, '*', i, '=', x*i)
    
    
for x in range(2, 10):
    for y in range(1, 10):
        print(x, '*', y, '=', x*y)
        
for x in range(2, 10):
    for y in range(1, 10):
        print(x, '*', y, '=', x * y, end=' ')
    print()  # 각 구구단 사이에 줄바꿈 추가


for i, j in enumerate(test_list): # enumerate: 인덱스 값 반환
    print(i, j)



n = 0
while n < 5:
    n += 1
    print(n)    
  
    
  
num = 979
i = 2

while num % i != 0:
    i += 1

if i == num:
    print('소수입니다.')
else:
    print('소수가 아닙니다.')    