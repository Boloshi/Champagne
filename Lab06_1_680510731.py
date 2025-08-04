#!/usr/bin/env python3
# Phutthachat Sawatnsthi (champagne)
# 680510731
# Lab06_1
# 204111 Sec 002

def main():
    test_square_frame()

def test_square_frame():
    square_frame(100)
    # square_frame(4, '.')

def square_frame(n: int, sep: str=' ') -> None :
    start_range = (list(range(1, (((n)*4)-4)+1)))
    sa = len(str(start_range[-1]))
    start_range = (list(map(lambda x: ((str(x)).zfill(sa)), start_range)))
    # print(type( start_range))
    # print(start_range)

    up = list(start_range[:n])
    up = sep.join(up)
    # print(up)

    r = (list(start_range[n:(n+n)-2]))
    # r = sep.join(r)
    # print(r)

    down = list(start_range[(n+n)-2:((n+n)-2)+n])
    down.reverse()
    down = sep.join(down)

    l = list(start_range[((n+n)-2)+n:])
    l.reverse()
    # l = sep.join(l)
    # print(l)
    c = len(up)-(sa*2)
    all_ = list(map(lambda x: ((str([(l[x])+(sep*c)+r[x]])).replace('\'','')).strip('[]') , range(0,n-2)))
    # all_ = all_.replace('\'','')
    all_ = '\n'.join(all_)
    # all_ = int(all_)
    # print(type(all_))
    # all_ = list(lambda l, y: [l]+(sep*n)+[r])
    # print (all_)
    # print(down)
    # p = list(l)+list(r)
    # h = (sep*n).join(p)
    # h = '\n'.join(h)
    # print(h)

    print('----------------')
    print(up)
    print(all_)
    print(down)

    # all_ = 
    # print(all_)
    # tang_l = '\n'.join(l).replace(',','')
    # print(tang_l)

    # tang_r ='\n'.join(l).replace(',','')

    # # print(g)
    









if __name__ == '__main__':
    main()