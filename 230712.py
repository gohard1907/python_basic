# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:14:31 2023

@author: Jung
"""

num = 103
i = 2
flag = 1
while i < num:
    res = num % i
    if res == 0:
        flag = 0
        break
    i += 1

if flag: #flag가 참이면
    print('소수 입니다.')
else:
    print('소수가 아닙니다.')
    
    
for i in range(10):
    if 3 < i < 6:
        continue
        break
    print(i)
    
for i in range(20):
    if i % 3 == 0:
        continue
    if i > 16:
        break
    print(i)


i = 0
while i < 10:
    i += 1
    if 6 < i < 8:
        break
    print(i)


def prime(number):
    for i in range(2, number):
        if number % i == 0:
            return(False)
    return(True)

prime(7)


passwds = input('패스워드를 입력해주세요.')

while passwds != '1234567':
    passwds = input('패스워드를 정확하게 입력해주세요.')

print('패스워드가 맞습니다.')

pw = '1234567'

while True:
    input_pw = input('패스워드를 입력해주세요.')
    if input_pw == pw:
        break
    else: print('패스워드를 정확하게 입력해주세요.')

print('패스워드가 맞습니다.')


input_name = input('''당신의 이름을 입력하세요. 'q'를 입력하면 종료합니다. : ''')
stop = 'q'

while input_name != stop:
    input_name = input('''당신의 이름을 입력하세요. 'q'를 입력하면 종료합니다. : ''')
    print(input_name)


input_num = int(input())
binary = ''

while input_num > 0:
    a = input_num % 2
    binary = str(a) + binary
    input_num = input_num // 2

print(binary)



answer = 50

while True:
    input_num = int(input('예상 숫자를 입력하세요: '))
    if input_num < answer:
        print('UP')
    elif input_num > answer:
        print('DOWN')
    else:
        print('정답')
        break


se = ''' Humans are odd. They think order and chaos are somehow opposites and try to control what won't be. But there is grace in their failings.'''


print(se.isalpha()) #영문인지 아닌지 판별
print(se.strip().strip('.'))
print(se.isnumeric())
print(se.lower())
print(se.upper())
print(se.strip().capitalize())
print(se.replace('Humans', 'We'))
result = se.split() # 리스트로 값 반환
print('//'.join(result))
print(se.replace('.', '\n'))

se = ''' Humans are odd. They think order and chaos are somehow opposites and try to control what won't be. But there is grace in their failings.'''

se = se.strip().replace('.', '').replace("'", '')
result = se.split()
'/'.join(result)

print(result)


print(se.find('u'))
print(se[:3])
print(se.find('u', 3))
print(se[101])
print(se.index('u'))
print(se.find('z'))


stop = 'q'
sentence = ''

while sentence != stop:
    sentence = input('''문장을 입력하세요. 'q'를 입력하면 종료합니다. : ''')
    if sentence != stop:
        sen_num = len(sentence.split())
        print('이 문장은', sen_num, '어절입니다.')



for item in range(2, 4):
    for each in range(2, 6):
        print(' %d X %d = %d' % (item, each, item*each))
        
sentence_num = 4
print(f'이 문장은 {sentence_num} 어절입니다.')        

for i in range(1, 14):
    print(f' 제{i}의아해가무섭다고그리오.')
    
x = 1
print(f' 제{x:2d}의아해가무섭다고그리오.') # 2d : 공백 1칸, 02d : 빈칸에 0을 채움


y = lambda para1 : 3 * para1
print(y(4))

def y(para1):
    return(3*para1)
print(y(4))

add = lambda a, b : a + b
print(add(2, 3))



se = ''' Humans are odd. They think order and chaos are somehow opposites and try to control what won't be. But there is grace in their failings.'''

print(se[:10])

short = lambda x : x[:10]

print(short(se))


def calculator(a, b):
    return a+b, a-b, a*b, a/b

print(calculator(2, 3))
print(calculator(12, 3))
print(type(calculator(12, 3)))



valid_pw = False

for input_count in range(5):
    pw_input = input('PASSWORD:')

    is_alpha = False
    is_digit = False
    is_special = False

    for char in pw_input:
        if char.isalpha():
            is_alpha = True
        elif char.isdigit():
            is_digit = True
        elif char in '!@#$':
            is_special = True
        else:
            is_special = False
            break

    if is_alpha and is_digit and is_special:
        valid_pw = True
        break
    elif len(pw_input) < 4:
        print('==== 4글자 이상으로 다시 입력하세요. ====')
    else:
        print('다시 입력하세요.')


if valid_pw:
    print('비밀번호가 정상으로 만들어 졌습니다.')
else:
    print('입력 5회를 초과하였습니다.')

attempts = 0
is_alpha = False
is_digit = False
is_special = False


for input_count in range(5):
    pw_input = input('PASSWORD:')

    for char in pw_input:
        if char.isalpha():
            is_alpha = True
        elif char.isdigit():
            is_digit = True
        elif char in '!@#$':
            is_special = True
        else:
            is_special = False
            break

    if is_alpha and is_digit and is_special:
        print('비밀번호가 정상으로 만들어 졌습니다.')
        break
    elif len(pw_input) < 4:
        print('==== 4글자 이상으로 다시 입력하세요. ====')
    else:
        print('다시 입력하세요.')

    attempts += 1

    if attempts >= 5:
        print('입력 5회를 초과하였습니다.')
        break
