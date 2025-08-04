#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# HW06_2
# 204111 Sec 002
# Helper p'wit 745 

def main():
    test_medal_allocation()

def test_medal_allocation():
    assert medal_allocation ([9, 8, 7, 6, 5, 4, 3, 2, 6]) == ([9], [8], [7])
    assert medal_allocation ([9, 8, 7, 7,7, 6, 5, 4, 3, 2]) == ([9], [8], [7, 7, 7])
    assert medal_allocation ([9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9], [], [8])
    assert medal_allocation ([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9, 9, 9], [], [])
    # medal_allocation ([9, 9,9,6,0]) == ([9, 9 , ], [8], [7])
    assert medal_allocation ([9,9, 8,8,7]) == ([9,9], [], [8,8])
    assert medal_allocation ([0 , 0, 0,0,0,0]) == ([], [], [])
    assert medal_allocation ([12,66,16,33,33]) == ([66], [33,33], [])
    assert medal_allocation ([9,9, 9,9,9]) == ([9,9, 9,9,9], [], [])
    assert medal_allocation ([1,2,1,1]) == ([2], [1,1,1], [])
    assert medal_allocation ([0, 0,0,1]) == ([1], [], [])
    assert medal_allocation ([9, 9, 8, 8, 8,8, 7, 6, 5, 4, 3, 2]) == ([9, 9], [], [8,8,8,8])
    assert medal_allocation ([1,2,1,1]) == ([2], [1,1,1], [])
    assert medal_allocation ([5,5,0,0]) == ([5,5], [], [])
    assert medal_allocation ([5,0,0,0]) == ([5], [], [])
    assert medal_allocation ([5,5,5,0]) == ([5,5,5], [], [])

    print('kuy yai')


    # print(medal_allocation ([9, 9,9,6,0]))

def medal_allocation(list_a: list[int]) -> tuple[list[int], list[int], list[int]]:
    list_all = list(reversed(sorted(list_a)))
    list_all = list(filter(lambda x: x>0 , list_all))
    # print(list_all)

    max_list_all = list(filter(lambda x: x==max(list_all), list_all))
    # print(max_list_all) #Gold

    list_del_max = list_all[len(max_list_all):]
    # print(list_del_max)

    max_list_del_max = list(filter(lambda x: x==max(list_del_max), list_del_max))
    # print(max_list_del_max) #silver

    min_list_max = list_del_max[len(max_list_del_max):]
    # print(min_list_max)
    min_list_del_max = list(filter(lambda x: x==max(min_list_max), min_list_max))
    # print(min_list_del_max) #brone
    # print(list_del_max[:1])
    if len(max_list_all) == 2 and len(max_list_del_max) == 0 and len(min_list_del_max) == 0 :
        return max_list_all , [] ,[]
    if len(max_list_all) <= 1 and len(max_list_del_max) > 1:
        return max_list_all , max_list_del_max , []
    if len(max_list_all) <= 1 and len(max_list_del_max) <= 1:
        return max_list_all , max_list_del_max , min_list_del_max
    if len(max_list_all) < 3 and len(max_list_del_max) >= 1:
        return max_list_all , [] , max_list_del_max
    if len(max_list_all) >= 3:
        return max_list_all , [] , []


if __name__ == '__main__':
    main()