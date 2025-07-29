#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# Lab05_2
# 204111 Sec 002

import string

def main():
	test_palindrome_without()

def palindrome_without(text: str, c: str) -> bool :
	text = text.lower()
	text = text.replace(' ', '')
	c = c.lower()
	flib_text = text.replace(c , '')
	if len(text) >= 2 :
		if flib_text == flib_text[-1: :-1] :
			return True
		else :
			return False
	else:
		return False

def test_palindrome_without():
	assert palindrome_without('bana na', 'B') == True
	assert palindrome_without('Swap of paws', 'f') == True
	assert palindrome_without('T', 't') == False
	assert palindrome_without('Nan', 'a') == True
	assert palindrome_without('An', 'a') == True
	assert palindrome_without('', '') == False
	assert palindrome_without('Nan', 'a') == True
	print('All ok')



if __name__ == '__main__':
	main()