#!/usr/bin/env python3
#Phutthachat Sawatnathi (Champagne)
#680510731
#HW04_1
#204111 sec 002

def main():
	test_minute_diff()

def test_minute_diff():
	assert minute_diff ( 8, 23, 'AM', 8, 24, 'AM' ) == 1
	assert minute_diff ( 8, 23, 'AM', 1, 24, 'PM' ) == 301
	assert minute_diff ( 1, 24, 'PM', 8, 23, 'AM' ) == 301
	# Same time
	assert minute_diff(9, 30, 'AM', 9, 30, 'AM') == 0
    
    # Same period (AM to AM)
	assert minute_diff(9, 30, 'AM', 10, 45, 'AM') == 75  # 1hr 15min
    
    # Same period (PM to PM)
	assert minute_diff(2, 15, 'PM', 4, 30, 'PM') == 135  # 2hr 15min
    
    # Different periods (AM to PM)
	assert minute_diff(11, 30, 'AM', 1, 30, 'PM') == 120  # 2 hours
    
    # Edge cases with 12 hour
	assert minute_diff(12, 0, 'AM', 12, 0, 'PM') == 720  # 12 hours (midnight to noon)
	assert minute_diff(12, 30, 'PM', 12, 30, 'AM') == 720  # 12 hours (noon to midnight)
	assert minute_diff(12, 59, 'AM', 1, 00, 'AM') == 1
	assert minute_diff(8, 23, 'AM', 8, 24, 'AM') == 1
	assert minute_diff(8, 23, 'AM', 1, 24, 'PM') == 301
	assert minute_diff(1, 24, 'PM', 8, 23, 'AM') == 301
	assert minute_diff(8, 23, 'AM', 1, 24, 'PM') == 301
	assert minute_diff(1, 00, 'AM', 1, 00, 'AM') == 0
	assert minute_diff(1, 1, 'AM', 1, 00, 'PM') == 719
	assert minute_diff(12, 59, 'AM', 11, 30, 'PM') == 1351
	assert minute_diff(1, 31, 'AM', 2, 30, 'PM') == 779
	assert minute_diff(11, 00, 'AM', 12, 00, 'PM') == 60
	assert minute_diff(12, 00, 'PM', 12, 00, 'AM') == 720
	assert minute_diff(12, 00, 'AM', 12, 00, 'PM') == 720
	assert minute_diff(12, 00, 'PM', 12, 00, 'PM') == 0
	assert minute_diff(12, 00, 'AM', 12, 00, 'AM') == 0
	assert minute_diff(12, 00, 'AM', 12, 1, 'AM') == 1
	assert minute_diff(12, 00, 'PM', 12, 1, 'PM') == 1
	assert minute_diff(12, 1, 'AM', 11, 59, 'PM') == 1438
	assert minute_diff(12, 1, 'PM', 12, 1, 'AM') == 720
	assert minute_diff(12, 0, 'PM', 11, 59, 'PM') == 719
	assert minute_diff(12, 0, 'AM', 11, 59, 'AM') == 719
	assert minute_diff(12, 59, 'AM', 11, 58, 'PM') == 1379
	assert minute_diff(11, 1, 'PM', 12, 0, 'PM') == 661
	assert minute_diff(8,23,'AM',8,24,'AM') == 1
	assert minute_diff(8,23,'AM',1,24,'PM') == 301
	assert minute_diff(1,24,'PM',8,23,'AM') == 301
	assert minute_diff(12, 1, 'PM', 12, 2, 'PM') == 1
	assert minute_diff(12, 00, 'AM', 8, 0, 'PM') == 1200 
	assert minute_diff(12, 00, 'AM', 11, 59, 'PM') == 1439 
	assert minute_diff(12, 00, 'AM', 11, 59, 'AM') == 719 
	assert minute_diff(12, 00, 'AM', 12, 00, 'AM') == 0 
	assert minute_diff(12, 00, 'AM', 11, 00, 'PM') == 1380
	assert minute_diff(12, 00, 'PM', 12, 00, 'AM') == 720
	assert minute_diff(12, 1, 'PM', 11, 00, 'AM') == 659
	print ('all ok')

	

def minute_diff (h1: int, m1: int, p1: str, h2: int, m2: int, p2: str) -> int :
	if p1 == 'AM' :
		if p2 == 'AM' :
			if p1 == 'AM' and h1 == 12 and h2 != 12:
				h = 0
				minute = abs((((h*60)+m1))+((h2*60)+m2))
			else :
				minute = abs(((h1*60)+m1)-(((h2*60)+m2)))
		if p2 == 'PM' :
			if h1 == 12 and h2 != 12 :
				h = 0
				minute = abs((720-((h*60)+m1))+((h2*60)+m2))
			elif h1 == 12 and h2 == 12 and m1 == 0 and m2 == 0 :
				h=0
				minute = abs((((h*60)+m1))+((h2*60)+m2))
			elif h1 == 12 and h2 == 12 and m1 != 0 and m2 != 0 :
				minute = abs((720-((h*60)+m1))+((h*60)+m2))
			else:
				minute = abs((720-((h1*60)+m1))+((h2*60)+m2))
	if p1 == 'PM' :
		if p2 == 'PM' :
			minute = abs(((h1*60)+m1)-((h2*60)+m2))
		if p2 == 'AM' :
			if p1 == 'PM' and h1 == 12 and h2 != 12:
				h = 0
				minute = abs((720-((h*60)+m1))+((h2*60)+m2))
			elif h1 == 12 and h2 == 12 and m1 == 0 and m2 == 0 :
				h=0
				minute = abs((((h*60)+m1))+((h2*60)+m2))
			elif h1 == 12 and h2 == 12 and m1 != 0 and m2 != 0 :
				h=0
				minute = abs((720-((h*60)+m1))+((h*60)+m2))
			else :
				minute = abs(((h1*60)+m1)+(720-((h2*60)+m2)))
	return minute

if __name__ == '__main__':
	main()