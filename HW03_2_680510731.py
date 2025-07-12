#!/usr/bin/env python3
# Phutthachat Sawatnathi (Champ)
# 680510731
# HW03_2
# 204111 Sec002

import math

def main():
    𝑛𝑢𝑚𝑏𝑒𝑟 = int(input())
    𝑘 = int(input())
    H = kth_digit(𝑛𝑢𝑚𝑏𝑒𝑟, 𝑘)
    print (H)

def kth_digit(𝑛𝑢𝑚𝑏𝑒𝑟: int, 𝑘: int) -> int:
    Y = (math.floor(abs(𝑛𝑢𝑚𝑏𝑒𝑟)/(10**𝑘)))%10
    return Y


if __name__ == '__main__':
    main()