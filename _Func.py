#!/usr/bin/env python3,4

#ref:http://yak-shaver.blogspot.jp/2013/08/blog-post.html
def split_str(s, n):
    #"split string by its length"
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]

#手牌    n=Trueでツモ n=Falseで牌を切る
def count_pai(c, n, l):
    if n:
        tmp = 1
    else:
        tmp= -1

    if c[1] == "m" or c[1] == "M":
        index = int(c[0])
    elif c[1] == "p" or c[1] == "P":
        index = 10+int(c[0])
    elif c[1] == "s" or c[1] == "S":
        index = 20+int(c[0])
    elif c[1] == "z":
        index = 30+int(c[0])
    else:
        print("error")
        print(c,n,l)
    l[index] += tmp


#print hand
def p_hand(h):
    s = []
    for n in range(38):
        for i in range(h[n]):
            if n < 10:
                s.append(str(n)+'m')
            elif n < 20:
                s.append(str(n-10)+'p')
            elif n < 30:
                s.append(str(n-20)+'s')
            else:
                s.append(str(n-30)+'z')
    
    return s
