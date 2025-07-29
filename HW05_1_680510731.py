#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# HW05_1
# 204111 Sec 002

import string

def main():
	test_replace_in_range()

def test_replace_in_range():
	assert replace_in_range("Happy birthday", 3, 10, "p", "e") == 'Hapey birthday'
	assert replace_in_range("Happy birthday", 3, 10, "z", "e") == 'Happy birthday'
	assert replace_in_range("Happy birthday", 0, 14, "h", "w") == 'Wappy birtwday'
	assert replace_in_range("Happy birthday", 3, 10, "y", "i") == 'Happi birthday'
	assert replace_in_range("Happy birthday", -9, 14, "y", "i") == 'Happy birthdai'
	assert replace_in_range("Happy birthday", 3, 14, "y", "i") == 'Happi birthdai'
	assert replace_in_range("Happy birthday", -100, 100, "y", "i") == 'Happi birthdai'
	assert replace_in_range("HapPy Birthday", -100, 100, "y", "i") == 'HapPi Birthdai'
	assert replace_in_range("HAPPY BIRTHDAY", -100, 100, "y", "i") == 'HAPPI BIRTHDAI'
	print('All ok')

def replace_in_range(text: str, start: int, stop: int, old_c: str, new_c: str) -> str :
	text_re = text[ start:stop ]
	# print(text_re)
	text_L = text[:start]
	# print(text_L)
	text_R = text[stop:]
	# print(text_R)
	text_big_old = old_c.upper()
	text_big_new = new_c.upper()
	text_0 = text_re.replace(text_big_old, text_big_new)
	text_1 = text_0.replace(old_c, new_c)
	change_text = "".join([text_L, text_1, text_R])

	return change_text


if __name__ == '__main__':
	main()