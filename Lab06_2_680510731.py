#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# Lab06_2
# 204111 Sec 002

def main():
    list_a = [1, 2, 3, 4] 
    dest_rotate_list(list_a, 105)
    print('output =', list_a)

def dest_rotate_list (list_a: list[int], n: int) -> None:
    roal_list_a = n % len(list_a)
    x = list_a[:-1*(roal_list_a)]
    y = list_a[-1*(roal_list_a):]
    list_a[:] = y+x  #[:]การแทนที่ list ด้วย = ข้างหลัง





if __name__ == '__main__':
    main()