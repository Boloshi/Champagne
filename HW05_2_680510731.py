#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# HW05_2
# 204111 Sec 002

import string

def main():
	test_transform_name()

def test_transform_name():
	assert transform_name('elizabeth andre') == 'Andre.Elizabeth'
	assert transform_name('          lena Eive') == 'Eive.Lena'
	assert transform_name('Toyoakini shidai') == 'Shidai.Toyoakin'
	assert transform_name('lala Divesdentinala') == 'Divesdenti.Lala'
	assert transform_name('Yoshimasa Ohmotoyoshi') == 'Ohmotoyos.Yoshi'
	assert transform_name('Tse Michelangelo') == 'Michelangel.Tse' 
	print('All work!')

def transform_name(name: str) -> str :
	t1 , t2 = name.split()
	t2 = t2.capitalize()
	t1 = t1.capitalize()
	full_name = t2 + "." + t1
	if len(full_name) <= 15:
		return full_name
	else :
		if len(t1) >= 5 and len(t2) >= 9:
			z = t2[:9]
			x = t1[:5]
			full = z + '.' + x
			
			return full
		elif len(t1) > 5 and len(t2) < 9:
			x = t1[:5]
			z = t1[:(9-len(t2))+len(x)]
			full = t2 + '.' + z
			
			return full
		elif len(t1) <= 5 and len(t2) > 9:
			z = t2[:9]
			x = t2[:(5-len(t1)+len(z))]
			full = x + '.' + t1
			
			return full

if __name__ == '__main__':
	main()
