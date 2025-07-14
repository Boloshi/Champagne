#!/usr/bin/env python3
# Phutthachat Sawatnathi (Champagne)
# 680510731
# Lab04_2
# 204111 Sec 002


def less_than(x: int, y: int) -> bool:
    return x < y


def my_min_mid_max(a: int, b: int, c: int) -> str:
        if less_than(a,b,c) :
           a = min_ 
           b = mid 
           c = max_
        elif less_than(b,c,a) :
           b = min_ 
           c = mid 
           a = max_
        else : 
           c = min_
           a = mid 
           b = max_
        min_ = mid = max_ = None
    return f'{min_} {mid} {max_}'


if __name__ == '__main__':
    assert my_min_mid_max(1, 2, 3) == '1 2 3'
    assert my_min_mid_max(7, 9, 8) == '7 8 9'