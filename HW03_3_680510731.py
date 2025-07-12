#!/usr/bin/env python3
# Phutthachat Sawatnathi (Champagne)
# 680510731
# HW03_3
# 204111 sec 002


import math


def main():
    𝑛𝑢𝑚𝑏𝑒𝑟 = int(input())
    𝑘 = int(input())
    𝑣𝑎𝑙𝑢𝑒 = int(input())
    A = T_post(𝑛𝑢𝑚𝑏𝑒𝑟, k)
    P = set_kth_digit(𝑛𝑢𝑚𝑏𝑒𝑟, 𝑘, 𝑣𝑎𝑙𝑢𝑒)
    Z = kth_digit(𝑛𝑢𝑚𝑏𝑒𝑟, P, k, A)
    print (Z)

def T_post(𝑛𝑢𝑚𝑏𝑒𝑟: int, 𝑘: int) -> int:
    G = (math.floor(abs(𝑛𝑢𝑚𝑏𝑒𝑟)/(10**𝑘)))%10
    return G

def set_kth_digit(𝑛𝑢𝑚𝑏𝑒𝑟: int, 𝑘: int, 𝑣𝑎𝑙𝑢𝑒: int) -> int:
    Y = 𝑣𝑎𝑙𝑢𝑒
    return Y


def kth_digit(𝑛𝑢𝑚𝑏𝑒𝑟: int, P: int, 𝑘: int, A: int) -> int:
    q = (abs(𝑛𝑢𝑚𝑏𝑒𝑟)-(A*(10**k)))+(P*(10**k))
    return q


if __name__ == '__main__':
    main()