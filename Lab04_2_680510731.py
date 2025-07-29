#!/usr/bin/env python3
# Phutthachat Sawatnathi (Champagne)
# 680510731
# Lab04_2
# 204111 Sec 002


def less_than(x: int, y: int) -> bool:
    return x < y


def my_min_mid_max(a: int, b: int, c: int) -> str:
         if less_than(a,b) :
            if less_than(a,c) :
               if less_than(c,b) :
                  min_ = a
                  max_ = b
                  mid  = c
               else :  
                  min_ = a
                  mid  = b
                  max_ = c
            else :
               mid  = a
               max_ = b
               min_ = c
         else : 
            if less_than(b,c) :
               if less_than (a,c) :
                  mid  = a
                  min_ = b
                  max_ = c
               else:
                  min_ = b
                  mid  = c
                  max_ = a
            else:
               min_ = c
               mid  = b
               max_ = a
               
         return f'{min_} {mid} {max_}'


if __name__ == '__main__':
    assert my_min_mid_max(1, 2, 3) == '1 2 3'