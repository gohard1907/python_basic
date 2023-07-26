# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 17:34:49 2023

@author: Jung
"""

total_head = 20
total_leg = 56

def brute_force_algorithm_x(total_head, total_leg):
    for x in range(-100, 1001):
        for y in range(-100, 1001):
            if x + y == total_head and 2*x + 4*y == total_leg:
                return x, y
    return None, None


def brute_force_algorithm(total_head, total_leg):
    for i in range(total_head + 1):
        j = total_head - i
        condition = 2*i + 4*j
        if condition == total_leg:
            return i, j
    return None, None

print(brute_force_algorithm(20, 56))

def barnyard():
    total_head = int(input('총 마리수: '))
    total_leg = int(input('총 다리수: '))

    chicken, pig = brute_force_algorithm(total_head, total_leg)
    if any((chicken, pig)):
        print(f'닭 수: {chicken}, 돼지 수: {pig}')
    else:
        print('There is no solution.')
        
barnyard()


def brute_force_algorithm_2nd(total_head, total_leg):
    for x in range(total_head + 1):
            for y in range(total_head - x + 1):
                z = total_head - x - y
                condition = 2*x + 4*y + 8*z
                if condition == total_leg:
                    return x, y, z
    return None, None, None

print(brute_force_algorithm_2nd(20, 56))

def barnyard_2nd():
    total_head = int(input('총 마리수: '))
    total_leg = int(input('총 다리수: '))

    chicken, pig, spider = brute_force_algorithm_2nd(total_head, total_leg)
    if any((chicken, pig, spider)):
        print(f'닭 수: {chicken}, 돼지 수: {pig}, 거미 수: {spider}')
    else:
        print('There is no solution.')
        
barnyard_2nd()


#모든 경우의 수가 궁금할 때
def brute_force_algorithm_3rd(total_head, total_leg):
    result = []
    for x in range(total_head + 1):
            for y in range(total_head - x + 1):
                z = total_head - x - y
                condition = 2*x + 4*y + 8*z
                if condition == total_leg:
                    result.append((x, y, z))
    return result

def barnyard_3rd():
    total_head = int(input('총 마리수: '))
    total_leg = int(input('총 다리수: '))

    result = brute_force_algorithm_3rd(total_head, total_leg)
    
    if result:
        for i in result:
            print(f'닭 수: {i[0]}, 돼지 수: {i[1]}, 거미 수: {i[2]}')
    else:
        print('There is no solution.')

barnyard_3rd()


base1 = 'ATGCGCCTGCGTCTGTACTAG'
base2 = 'ATGCGCTGCGTCTGTACTAG'
base3 = 'ATGCGCCTGCGTCTGTAGTAG'
base4 = 'ATGCGCCTGCGTCTTAGATAG'

def is_DNA(DNA):
    if len(DNA) % 3 != 0:
        return False
     
    if not DNA.startswith('ATG') and DNA.endswith(('TAA', 'TGA', 'TAG')):
        return False
    
    middle_seq = DNA[3:-3]
    for i in range(0, len(middle_seq), 3):
        codon = middle_seq[i:i+3]
        for end_codon in ('TAA', 'TGA', 'TAG'):
            if codon == end_codon:
                return False
    
    return True


print(is_DNA(base1))
print(is_DNA(base2))
print(is_DNA(base3))
print(is_DNA(base4))



def check_DNA(base):
    if len(base) % 3 != 0:
        return False
    if not base.startswith('ATG'):
        return False
    for i in range(len(base)-3):
        if i % 3 == 0:
            if base[i:i+3] == 'TAA':
                return False
            if base[i:i+3] == 'TAG':
                return False
            if base[i:i+3] == 'TGA':
                return False
    if base.endswith('TAA'):
        return True
    if base.endswith('TAG'):
        return True
    if base.endswith('TGA'):
        return True
    return False


print(check_DNA(base1))
print(check_DNA(base2))
print(check_DNA(base3))
print(check_DNA(base4))

