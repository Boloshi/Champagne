#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# HW06_1
# 204111 Sec 002

import string

def main():
    test_same_letters()

def test_same_letters():
    same_letters('your reader' ,'You are ready.') #== True
    same_letters('4i2r3ol\{l3n}6mtG7o8d9' ,'GooLm#tdM4498orn23ing')# == True
    same_letters('WelCome', 'weldoNe') # == False
    same_letters('reST334RoOm344home56' ,'256889HBbro455om55s') #== False
    same_letters('B','b') #== False
    same_letters('abcd','abcde') #false
    same_letters('asduwq','qwds') #F
    print('all ok')

def same_letters(str1: str, str2: str) -> bool:
    a_Z = string.ascii_letters
    str1 = str1.lower()
    str2 = str2.lower()
    abc_first = list(filter(lambda x: (x in a_Z) , str1))
    # print(abc_first)
    abc_secon = list(filter(lambda x: (x in a_Z) , str2))
    # abc_secon = ''.join(abc_secon)
    # print(abc_secon)

    if not all(map(lambda x: abc_first[x] in abc_secon, range(len(abc_first)))) or (not all(map(lambda x: abc_secon[x] in abc_first, range(len(abc_secon))))) :
        # print(False)
        return False
    else:
        # print(True)
        return True






if __name__ == '__main__':
    main()