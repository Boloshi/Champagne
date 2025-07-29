#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# HW05_3
# 204111 Sec 002

import datetime



def main():
	test_display_post_time()


def display_post_time(post_time: str, post_tz:str, view_time: str, view_tz: str) -> str:
	post_time1 = datetime.datetime.strptime(post_time, '%Y-%m-%d %H:%M:%S')
	view_time1 = datetime.datetime.strptime(view_time, '%Y-%m-%d %H:%M:%S')
	# print(post_time1)
	# print(view_time1)
	u1 = post_tz[3:]
	u2 = view_tz[3:]
	if u1 == '' :
		u1 = '0'
	if u2 == '':
		u2 = '0'
	utc_del_post = float(u1)
	utc_del_view = float(u2)
	sp = utc_del_view - utc_del_post
	time_utc_post = datetime.timedelta(hours=sp)
	post_time0 = post_time1 + time_utc_post
	# print(post_time0)
	spac_view = view_time1 - post_time0
	# print(spac_view)
	if post_time0.year != view_time1.year:
		p = post_time0.strftime('%b %d, %Y')
		# print(p)
		return p
	if spac_view < datetime.timedelta(minutes=1) :
		# print(spac_view.seconds)
		return ('just now')
	if spac_view < datetime.timedelta(hours=1):
		p = spac_view.total_seconds()//60
		o = int(p)
		y = str(o)
		# print(y+'m')
		return (y+'m')
	if spac_view < datetime.timedelta(days=1):
		p = spac_view.total_seconds()//3600
		o = int(p)
		y = str(o)
		# print(y+'h')
		return (y+'h')
	if spac_view < datetime.timedelta(weeks=1):
		p = post_time0.strftime('%A')
		# print(p)
		return p
	if spac_view < datetime.timedelta(days=365):
		p = post_time0.strftime('%b %d')
		# print(p)
		return p




def test_display_post_time():
	assert display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-15 10:30:45', 'UTC') == 'just now'
 	# print(display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-15 10:30:45', 'UTC'))
	assert display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-15 11:15:00', 'UTC') == '45m'
# 	print(display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-15 11:15:00', 'UTC'))
	assert display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-15 15:45:00', 'UTC') == '5h'
# 	print(display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-15 15:45:00', 'UTC'))
	assert display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-19 15:45:00', 'UTC') == 'Monday'
# 	print(display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-19 15:45:00', 'UTC'))
	assert display_post_time('2023-05-15 03:30:00', 'UTC+7','2023-12-19 15:45:00', 'UTC+3') #== 'May 14'
# 	print(display_post_time('2023-05-15 03:30:00', 'UTC+7','2023-12-19 15:45:00', 'UTC+3'))
	assert display_post_time('2023-05-15 03:30:00', 'UTC+7','2024-12-19 15:45:00', 'UTC+4') == 'May 15, 2023'
# 	print(display_post_time('2023-05-15 03:30:00', 'UTC+7','2024-12-19 15:45:00', 'UTC+4'))
	assert display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-15 18:15:00', 'UTC+7') == '45m'
# 	print(display_post_time('2023-05-15 10:30:00', 'UTC','2023-05-15 18:15:00', 'UTC+7'))
	assert display_post_time('2023-09-01 12:00:00', 'UTC-10','2023-09-05 00:00:00', 'UTC+2') == 'Saturday'
# 	print(display_post_time('2023-09-01 12:00:00', 'UTC-10','2023-09-05 00:00:00', 'UTC+2'))
	assert display_post_time('2023-01-01 00:00:01', 'UTC+14','2023-12-31 09:59:59', 'UTC') == 'Dec 31, 2022'
# 	print(display_post_time('2023-01-01 00:00:01', 'UTC+14','2023-12-31 09:59:59', 'UTC'))
	assert display_post_time('2023-08-01 10:00:00', 'UTC','2023-08-02 09:59:59', 'UTC') == '23h'
# 	print(display_post_time('2023-08-01 10:00:00', 'UTC','2023-08-02 09:59:59', 'UTC'))
	assert display_post_time('2022-12-31 23:59:59', 'UTC','2023-01-01 00:00:00', 'UTC') == 'Dec 31, 2022'
	assert display_post_time('2023-05-15 10:30:00', 'UTC+5.50','2023-05-15 10:30:00', 'UTC+5') == '30m'
	assert display_post_time('2023-05-15 09:00:00', 'UTC','2023-05-15 09:00:00', 'UTC-1.25') == '1h'
	print('All Suuuuuu')


if __name__ == '__main__':
	main()
