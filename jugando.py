# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

arr = [1,2,2,3,3,3]


def diagonal(arr):
    n = len(arr)
    a = []
    b = []
    for i,j in zip(range(0,n),reversed(range(0,n))):
            a.append(arr[i][i])
            b.append(arr[i][j])
    result = abs(sum(a) - sum(b))
    return result

def masmenos(arr):
    n = len(arr)
    mas = []
    menos = []
    cero = []
    for i in range(0,n):
        if arr[i] > 0:
            mas.append(1)
        elif arr[i] < 0:
            menos.append(1)
        elif arr[i] == 0:
            cero.append(1)
    print(len(mas)/n)
    print(len(menos)/n)
    print(len(cero)/n)

def staircase(n):
    for i,k in zip(range(1,n+1),reversed(range(0,n))):
        print(' '*k + '#'*i)

def minmaxsum(arr):
    n = len(arr)
    a = []
    for i in range(0,n):
        a.append(sum(arr)-arr[i])
    print(min(a),max(a))

def cumplanito(arr):
    m = max(arr)
    n = len(arr)
    a = []
    for i in range(0,n):
        if arr[i] == m:
            a.append(1)
    result = sum(a)
    return result

s = '12:45:54PM'
#output = '20:45:06'

def convertime(s):
    time = s.rstrip('APM')
    h,m,seg = time.split(':')
    if (s.find('P') != -1):
        if h == '12':
            pass
        else:
            h = int(h) + 12
    else:
        if h == '12':
            h = '00'
        else:
            pass
    hora = f'{h}:{m}:{seg}'
    return hora



        