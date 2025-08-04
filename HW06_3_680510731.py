#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# HW06_3
# 204111 Sec 002

def main():
    test_moving_average()


def test_moving_average():
    assert moving_average([1, 2, 3, 4, 5], 2) == [1.5, 2.5, 3.5, 4.5]
    assert moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]

def moving_average(list_x: list[float], w: int) -> list[float] :

    list_  = (list(map(lambda x: (sum(list_x[x:x+w]))/w, range((len(list_x)+1)-w))))
    # print(type(sleep))
    return list_




if __name__ == '__main__':
    main()