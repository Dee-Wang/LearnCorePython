#!/usr/bin/env python
#coding:utf-8
import random
N = random.randint(2,100)
lis = []
for i in range(N):
    n = random.randint(0,2**31 -1)
    lis.append(n)
print lis
lis2 = []
for i in range(N):
    lis2.append(lis[random.randint(0,N-1)])

lis2.sort()
print lis2
