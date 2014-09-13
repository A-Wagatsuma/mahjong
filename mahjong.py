#!/usr/bin/env python

#####################################################
# ver. 1.5                                          #
#                                                   #
#                                                   #
#####################################################

import sys
import fileinput
import re
#ref:http://yak-shaver.blogspot.jp/2013/08/blog-post.html
def split_str(s, n):
    #"split string by its length"
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]
   
#手牌    n=Trueでツモ n=Falseで牌を切る
def count_pai(c, n, l):
	if(n):		
		tmp = 1
	else:
		tmp = -1
	
	if c[1] == "m":
		index = 0 + int(c[0])	
	elif c[1] == "p":
		index = 10 + int(c[0])
	elif c[1] == "s":
		index = 20 + int(c[0])
	elif c[1] == "z":
		index = 30 + (int(c[0])-1)*2+1
	else:
		print("error!")
	l[index] += tmp
	return

#print hand
def p_hand(h):
    s = []
    for n in range(44):
        for i in range(h[n]):
            s.append(n)
    return s

#class Player
class Player:
 def __init__(self, hist, reach, menzen, naki, num_call,kawa):
        self.hist       = hist
        self.reach      = reach
        self.menzen     = menzen
        self.naki       = naki
        self.num_call   = num_call
        self.kawa       = kawa
 
 def player_move(self, turn, last, before, move, tile):
 
    if move == 'G':
        count_pai(tile, True, self.hist)
        pass

    elif move == 'D':
        self.kawa.append(last)
        count_pai(tile, False, self.hist)
        pass

    elif move == 'd':
        self.kawa.append(last)
        count_pai(tile, False, self.hist)
        pass

    elif move == 'N':
        self.menzen = False
        for c in range(2):
            count_pai(last, False, self.hist)
        
        pass

    elif move == 'C':
        self.menzen = False
        pass

    elif move == 'K':
        pass

    elif move == 'A':
        pass

    elif move == 'R':
        pass






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

print()
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
        agari = "0"
        tumoagari = False
        player = ['','','','']
        
        #format class
        for i in range(4):
            player[i] = Player([0]*44,False,True,[],0,[])
            for j in [0,10,20,30,32,34,36,38,40,42]:
                player[i].hist[j] = -9
            for c in split_str(o[i+2],2):
                count_pai(c, True, player[i].hist)

        for vv in o[8:]:
            m5 = re.match('(\d)(\w)((\d\w)*)',vv)
            if m5:
                turn = int(m5.group(1))-1
                player[turn].player_move(turn, last, before, m5.group(2),m5.group(3))
                last = m5.group(3)
                before = turm

        print()
        print()
        o = ['']*8
