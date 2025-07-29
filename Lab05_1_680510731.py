#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# Lab05_1
# 204111 Sec 002

import string
number = string.digits
A_Z = string.ascii_uppercase

def main():
    test_is_valid_license()


def is_valid_license(license_str: str) -> bool:
    number = len(license_str)
    if 2 < number 



def test_is_valid_license() :
    assert is_valid_license('9AB8954') == True
    assert is_valid_license('9999') == False
    assert is_valid_license('CD700') == True
    assert is_valid_license('TA89F') == False
    assert is_valid_license('99D1234') == False
    assert is_valid_license('9DD123F') == False
    assert is_valid_license('99D123445') == False
    assert is_valid_license('CD1') == True
    assert is_valid_license('9CD198') == True

    print ('All ok')



if __name__ == '__main__':
    main()

# คุณได้รับมอบหมายให้เขียนฟังก์ชัน
# is_valid_license(𝑙𝑖𝑐𝑒𝑛𝑠𝑒_𝑠𝑡𝑟: str) ‐> bool 
# เพือคืนค่า Boolean True หาก 𝑙𝑖𝑐𝑒𝑛𝑠𝑒_𝑠𝑡𝑟 เป็นเลข
# ทะเบียนทีมีรูปแบบรูปแบบตามกฎหมาย และคืนค่า False หาก 𝑙𝑖𝑐𝑒𝑛𝑠𝑒
# 𝑠𝑡𝑟 เป็นเลขทะเบียนทีมีรูปแบบไม่ตรง
# ตามกฎหมาย โดย 𝑙𝑖𝑐𝑒𝑛𝑠𝑒
# 𝑠𝑡𝑟 จะมีความยาวตังแต่ 1 แต่ไม่เกิน 7 อักขระ และประกอบด้วยอักษรในรูป 
# upper-case [A‐Z] และอักขระตัวเลข [0‐9] เท่านัน
# Input Output
# 9AB8954 True
# 9999 False
# CD700 True
# 99D1234 False