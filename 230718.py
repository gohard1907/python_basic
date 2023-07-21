# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:03:38 2023

@author: Jung
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(15))


names = ['토미', '지미', '낸시', '불독']
fes = ['OT', 'CONCERT', 'MT', 'PLAY']

import random

def match_fes(names, fes):
    fes = fes.copy()
    sample_dict = {}
    for i in names:
        a = random.choice(fes)
        sample_dict[i] = a
        fes.remove(a)
    return sample_dict

print(match_fes(names, fes))


print(random.sample(fes, 2))
print(random.choice(fes))
random.shuffle(fes)
print(fes)
print(random.randint(1, 6)) #1부터 6까지 수 중에서 하나를 랜덤으로 추출
print(random.randrange(1, 7)) #1부터 6까지 수 중에서 하나를 랜덤으로 추출


numb = [11, 15, 2, 7]
target = 9

def add_numb(numb, target):
    index = []
    result = random.choice(numb) + random.choice(numb)
    while result != target:
        index = random.sample(range(len(numb)), 2)
        result = numb[index[0]] + numb[index[1]]
    return index

print(add_numb(numb, target))


def find_numb(numb, target):
    index = []
    for i in range(len(numb)):
        for j in range(i+1, len(numb)):
            if numb[i] + numb[j] == target:
                index = [i, j]

    return index

print(find_numb(numb, target))



def mysum(*args):
    total = 0
    for i in args:
        total += i
    return total

print(mysum(1, 2, 3))
print(mysum(1, 3))
print(mysum(1, 5, 1, 1, 1))



def gambling(money, goal, bet, trial):
    success = 0

    for _ in range(trial):
        current_money = money
        while current_money > 0 and current_money < goal:
            bet += 1
            result = random.randrange(0, 2)
            if result == 0:
                current_money -= 1
            else:
                current_money += 1

        if current_money >= goal:
            success += 1

    success_percent = success / trial
    total_bet = bet // trial
    
    return success_percent, total_bet

print(gambling(10, 20, 1, 1000))





