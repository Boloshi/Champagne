#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# HW04_2
# 204111 Sec 002

def main():
	test_calculate_exp()


def calculate_exp( p: int, c: int ) -> int:
	
	kanpi = ((((p+c)-13)//11)+1)

	if p != 0 and c < (10*p)+9:
		if ((((p+c)-13)//11)+1) >= 0 :
			exp = ((((p+c)-13)//11)+1)*(1000)
			return exp

	elif p == 0:
		exp = 0
		return exp

	else:
		if p != 0 and c >= (10*p)+9:
			exp = p*1000
			return exp






# p=78
# p+c = 782
# exp=78000

# p=12
# k=122
# exp=12000


def test_calculate_exp():
    assert calculate_exp(1, 12) == 1000
    assert calculate_exp(2, 12) == 1000
    assert calculate_exp(1200, 0) == 108000
    assert calculate_exp(55, 5) == 5000
    assert calculate_exp(2, 0) == 0
    assert calculate_exp(12, 0) == 0
    assert calculate_exp(7, 6) == 1000
    assert calculate_exp(1, 12) == 1000
    assert calculate_exp(78, 590) == 60000
    assert calculate_exp(78, 5900) == 78000

    # assert calculate_exp(900, 9000) == 899000



if __name__ == '__main__':
	main()