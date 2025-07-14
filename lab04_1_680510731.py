#!/usr/bin/env python3
# Phutthachat Sawatnathi (Champagne)
# 680510731
# Lab04_1
# 204111 sec 002

# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function circle_intersect()

def main():
    test_circle_intersect()


def circle_intersect(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float, epsilon=10**-6) -> int:
    circle = 
    return 1


def test_circle_intersect():
    assert circle_intersect(2, 3, 5, 5, 7, 1) == 1
    assert circle_intersect(0, 0, 2.5, 3, 4, 2.5) == 0
    assert circle_intersect(1, 1, 5, 6, 17, 7) == -1

    # now using specified epsilon
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=1.5) == 0
    print("all ok!")


if __name__ == '__main__':
    main()
