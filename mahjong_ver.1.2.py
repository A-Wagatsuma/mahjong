#!/usr/bin/env python

import sys
import fileinput
import re
#ref:http://yak-shaver.blogspot.jp/2013/08/blog-post.html
def split_str(s, n):
    #"split string by its length"
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]

k2s = { '東' : '1z', '南' : '2z', '西' : '3z', '北' : '4z', '白' : '5z', '発' :'6z', '中':'7z'}
sys.stdin = open('/dev/stdin', 'r', encoding='utf-8')
sys.stdout = open('/dev/stdout','w', encoding='utf-8')
dealt={}
p_wind = ''
dealer = ''
# [p_wind dealer dealt1 dealt2 dealt3 dealt4 dora ura fu ....]
o = ['']*8
hand = ['']*4


#print(o)


for line in fileinput.input(openhook=fileinput.hook_encoded('utf-8')):
    #reading
    for v in k2s:
        line = line.replace(v,k2s[v])
    m1 = re.match('  (\d\w)\d局',line)
    if m1:
        o[0] = m1.group(1)
    m2 = re.match('    \[(\d)(\d)\w]((\d\w)*)',line)
    if m2:
        if m2.group(2) == '1':
            o[1] = m2.group(1)
        o[int(m2.group(1))+1] = m2.group(3)
    m3 = re.match('    \[表ドラ\]((\d\w)+) \[裏ドラ\]((\d\w)+)',line)
    if m3:
       o[6]=m3.group(1)
       o[7]=m3.group(3)
    m4 = re.match('    \* (\w+( \w+)*)\s$',line)
    if m4:
        o.extend(m4.group(1).split(' '))

    #reproduce
    if o[0] != '' and o[5] != '' and re.match('^$',line):
        reach = [False]*4
        menzen = [True]*4
        tumoagari = False
        naki = ['']*4
        kawa  = [[],[],[],[]]
        agari = "0"
        for i in [0,1,2,3]:
            hand[i] = split_str(o[i+2],2)
        for vv in o[8:]:
            m5 = re.match('(\d)(\w)((\d\w)*)',vv)
            if m5:
                player = int(m5.group(1))-1
                if m5.group(2) == 'G':
                    tumo = m5.group(1)
                    get = m5.group(3)
                    last = m5.group(3)
                
                elif m5.group(2) == 'd':
                    hand[player][hand[player].index(m5.group(3))] = get
                    hand[player].sort()
                    hand[player].sort(key=lambda x:x[1:])
                    last = m5.group(3)
                    kawa[player].extend(last.split(' '))

                elif m5.group(2) == 'D':
                    last = m5.group(3)
                    kawa[player].extend(last.split(' '))

                elif m5.group(2) == 'A':
                    if int(tumo) == int(m5.group(1)):
                        tumoagari = True
                    agari = m5.group(1)

                elif m5.group(2) == 'R':
                    reach[player] = True


#elif m5.group(2) == 'K': #カン

                elif m5.group(2) == 'N': #ポン
                    menzen[int(m5.group(1))-1] = False
                elif m5.group(2) == 'C': #チー
                    menzen[int(m5.group(1))-1] = False


        if tumoagari:
            print(' '+agari+'  tumo')
        elif agari != "0":
            print(' '+agari)
        else:
        	print("")
        for i in [0,1,2,3]:
            if reach[int(i)]:
                hand[int(i)].insert(0,'R')
            else:
                hand[int(i)].insert(0,' ')
            if menzen[int(i)]:
                hand[int(i)].insert(0,' ')
            else:
                hand[int(i)].insert(0,'N')
            if int(i) == int(agari)-1:
                hand[int(i)].extend(last.split(' '))
            print(' '.join(hand[int(i)]))
            print(kawa[int(i)])

        print('')
        o = ['']*8
