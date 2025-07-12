#!/usr/bin/env python3
# Phutthachat Sawatnathi (Champ)
# 680510731
# Lab02_1
# 204111 Sec002

import math

a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

s = (a+b+c)*(1/2)

area = (s*(s-a)*(s-b)*(s-c))**(1/2)
area = math.ceil (area)
print (area)