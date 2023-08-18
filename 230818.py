# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 13:09:21 2023

@author: Jung
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(arr.shape)
print(arr.ndim)

arr_2d = arr.reshape(1, 5)
print(arr_2d)
print(arr_2d.shape)
print(arr_2d.ndim)

arr_2d_v = arr.reshape(5, 1)
print(arr_2d_v)
print(arr_2d_v.shape)
print(arr_2d_v.ndim)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.shape)
print(arr.ndim)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[10, 20, 30], [40, 50, 60]]])
print(arr)
print(arr.shape)
print(arr.ndim)

a = np.array(1)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
e = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
f = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

for i in (a, b, c, d, e, f):
    print(i.ndim, i.shape)
    
arr = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr)
print(arr.shape)
print(arr.ndim)

arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr[0])
print(arr[-1])
print(arr[-2])

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2)
print(arr2.shape)
print(arr2.ndim)
print(arr2[0][3])
print(arr2[1][2])
print(arr2[0, 3])

arr3 = np.arange(12)*10
print(arr3)
print(arr3.shape)
print(arr3.ndim)
print(arr3[5])

arr4 = arr3.reshape(2, 3, 2)
print(arr4)
print(arr4.shape)
print(arr4.ndim)
print(arr4[0])
print(arr4[1])
print(arr4[1][1][1])
print(arr4[1, 1, 1])

print(arr4[:, 0, 0])
print(arr4[0, :, 0])
print(arr4[0, 1, :])

print(arr3.shape)
print(arr3.reshape(2, 6))
print(arr3.reshape(3, 4))
print(arr3.reshape(1, 12))
print(arr3.reshape(1, 12).ndim)
print(arr3.reshape(2, 2, 3))
print(arr3.reshape(1, 4, 3))
print(arr3.reshape(2, 1, 6))
print(arr3.reshape(2, 6, 1))
print(arr3.reshape(2, 2, -1))
print(arr3.reshape(2, -1, 3))
print(arr3.reshape(-1, 1))
print(arr3.reshape(1, -1))
print(arr3.reshape(1, -1, 1))

print(arr3[:, np.newaxis])
print(arr3[np.newaxis, :])
print(np.newaxis)

arr_2d = arr3.reshape(3, 4)
print(arr_2d)
print(arr_2d[:, 2])
print(arr_2d[2, :])
print(arr3.reshape(-1, 3))

n = 0
for i in arr_2d:
    n += 1
    print(n, '번째', i)
    
for i in arr_2d:
    print(i)
    print('-'*10)
    for j in i:
        print(j)
        
for i in np.nditer(arr_2d):
    print(i)       
    
for idx, x in np.ndenumerate(arr_2d):
    print(idx, x)
    
for idx, x in np.ndenumerate(arr3.reshape(2, 3, -1)):
    print(idx, x)
    
    
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1)
print(arr2)

arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(arr1)
print(arr2)

arr = np.concatenate((arr1, arr2), axis = 0)
print(arr)

arr = np.concatenate((arr1, arr2), axis = 1)
print(arr)

print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))

def create_array(n_size):
    arr = np.arange(n_size)*10
    return arr

def print_array(n_arr):
    print('nditer 사용 예')
    for i in np.nditer(n_arr):
        print(i)
    print('ndenumerate 사용 예')
    for idx, x in np.ndenumerate(n_arr):
        print(idx, x)

print_array(arr3)


arr = np.array([1.1, 2.1, 3.1])
print(arr.dtype)

new_arr = arr.astype(int)
print(new_arr)
print(new_arr.dtype)

arr = np.array([1, 0, 3])
new_arr = arr.astype(bool)
print(new_arr)

new_arr = arr.astype(float)
print(new_arr)
print(new_arr.dtype)

x = arr.copy()
print(x)
arr[0] = 42
print(arr)
print(x)

x = arr.view()
print(x)
arr[0] = 1
print(x)
print(arr)
x[0] = 31
print(x)
print(arr)
print(x.base)

arr = np.array([1, 2, 3, 4])
x = arr.copy()
y = arr.view()

y[1] = 20
print(y)
print(y.base) #원본이 있는지 확인하는 용도. view()를 사용해야 base 확인 가능

print(arr)
print(arr.tolist())
print(arr.reshape(2,2).tolist())
print(np.arange(12).reshape(2, 2, 3).tolist())

arr = np.arange(12).reshape(2, 2, 3)
print(arr)
print(arr.reshape(-1))
print(arr.reshape(-1).tolist())
print(arr.reshape(3, 4))
print(arr.reshape(3, 4).base)

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr==4)
print(x)
print(type(x))
print(np.where(arr<3))

arr = np.arange(6).reshape(2, 3)
print(arr)
print(np.where(arr<3))
print(np.where(arr<3, 100, -50)) #3보다 작으면 100, 그렇지 않으면 -50
print(np.where(arr<3, 100, arr))

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
tmp = np.random.randint(1, 10, 20)
print(tmp)
print(np.sort(tmp))
print(np.sort(tmp)[::-1])
tmp.sort()
print(tmp)

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
new_arr = arr[x]
print(new_arr)

mx = np.ma.array([1, 2, 3, 4, 5], mask = [True, False, False, False, False])
print(mx)
print(mx.mask)
print(mx.data)

mx_3 = mx > 3
print(mx_3)
mx_4 = mx[mx>3]
print(mx_4)

d = np.array([30, 40, 50, 60, 70])
print(d[mx_3])

print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.empty((2, 3)))

arr = arr3.reshape(3, 4)
print(arr)
print(np.ones_like(arr))
print(np.zeros_like(arr))
print(np.empty_like(arr))

print(np.arange(0, 1, 0.2))
print(np.linspace(1, 10, 100))

arr = np.array([[1, 2], [3, 4]])
brr = np.array([[5, 6], [7, 8]])
print(arr)
print(brr)
print(arr + brr)
print(arr - brr)
print(arr * brr)
crr = np.array([10, 30])
print(crr)
print(arr + crr)

print(np.arange(3) + 5)
print(np.ones((3, 3)) + np.arange(3)) # broadcasting
print(np.arange(3).reshape((3, 1)) + np.arange(3))

a3 = np.array([1, 10, 100])
b3 = np.array([1])
print(a3 - b3)

a3 = np.array([[1, 10, 100], [1000, 1000, 1000]])
b3 = np.array([1, 2, 3])
print(a3 - b3)

arr = np.random.randn(5)
print(arr)
print(arr.min())
print(arr.argmin()) # 인덱스 번호 반환
print(arr.max())
print(arr.argmax())
print(arr[np.where(arr<0)])

def f(x):
    result = 4 * np.sin(x) + x
    return result
x = np.arange(1, 10, np.pi/30)
y = f(x)
print(y)

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()

a2 = np.arange(6).reshape(3, 2)
print(a2)
print(np.sum(a2))
print(np.sum(a2, axis = 0))
print(np.sum(a2, axis = 1))
print(np.mean(a2))
print(np.mean(a2, axis = 0))
print(np.mean(a2, axis = 1))
print(np.max(a2))
print(np.max(a2, axis = 0))
print(np.max(a2, axis = 1))
print(np.argmax(a2, axis = 0))
print(np.argmax(a2, axis = 1))
print(np.exp(a2))
print(np.sum(np.exp(a2), axis = 0))


# 1. a, b 가 모두 1차원 행렬일 때 : 모두 곱해서 더해준다.
a = np.array([1, 2])
b = np.array([3, 4])
print(np.dot(a, b))


# 2. a, b 가 모두 2차원 행렬일 때 : 일반적인 행렬 곱
arr = np.arange(1, 5).reshape(2, 2)
brr = np.arange(5, 9).reshape(2, 2)
print(arr)
print(brr)
print(np.dot(arr, brr))

arr = np.arange(1, 7).reshape(2, 3)
brr = np.arange(5, 11).reshape(3, 2)
print(np.dot(arr, brr))


# 3. a, b 중 하나가 스칼라일 때 : 단순 곱셈
print(arr)
c = 10
print(np.dot(arr, c))


# 4. a가 n차원, b가 1차원 행렬일 때 : a의 마지막 축에 b를 곱하여 더한 값을 나타낸다.
a = np.array([[1, 2], [3, 4]])
b = np.array([10, 100])
print(a)
print(b)
print(np.dot(a, b)) # b가 (2, 1)의 행렬이 되었다고 생각하면 편함
print(np.dot(b, a))

k = np.arange(2*2*3).reshape(2, 2, 3)
print(k)
c = np.array([1, 100, 10000])
print(np.dot(k, c))


# 5. a, b 가 모두 2차원 이상 행렬일 때 : a의 마지막 축과 b의 마지막에서 두번째 축을 곱한 뒤 합한 값을 표시
a = np.arange(3*4*5*6).reshape((3, 4, 5, 6))
b = np.arange(3*4*5*6).reshape((5, 4, 6, 3))
print(np.dot(a, b))
print(np.dot(a, b).shape)



a = np.arange(6).reshape(3, 2)
b = np.array([[10, 100, 1000]])
print(a)
print(b)
print(np.dot(b, a))
print(a.T) # 행과 열을 바꿔줌
print(b.T)

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.dot(x, w) + b
    if tmp < 0:
        return 0
    else:
        return 1
    
print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))