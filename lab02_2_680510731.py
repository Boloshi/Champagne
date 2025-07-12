#!/usr/bin/env python3
# Phutthachat Sawatnathi (Champ)
# 680510731
# Lab02_2
# 204111 Sec002

import math 

x = float(input('input milliseconds'))

a = (x%1000)
b = ((x//1000)%60)
c = (((x//1000)//60)%60) 
d = ((((x//1000)//60)//60)%24)
e = (((((x//1000)//60)//60)//24)%30)
a = math.floor (a)
b = math.floor (b)
c = math.floor (c)
d = math.floor (d)
e = math.floor (e)

print  (e, "day(s)", d, "hour(s)" , c, "minute(s)" , b, "second(s)" ,"and", a ,"millisecond(s)")





