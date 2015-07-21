#!/usr/bin/env python

#####################################################
# ver. 1.7                                          #
#                                                   #
#                                                   #
#####################################################
#export PYTHONDONTWRITEBYTECODE=1 or -B


import sys
import fileinput
import re
from Player import Player
from Turn_info import Turn_info
from Readdata import Read_data
from _Func import *
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
    #print(o)
    Read_data(line, o)
    #print(line)
    #reproduce
    if o[0] != '' and o[5] != '' and re.match('^$',line):
        agari = "0"
        tumoagari = False
        player = ['','','','']
        
        #format class
        for i in range(4):
            player[i] = Player([0]*38,False,True,[],0,[])
            for j in [0,10,20,30]:
                player[i].hist[j] = 0
            for c in split_str(o[i+2],2):
                count_pai(c, True, player[i].hist)
        info = Turn_info(-1,'',-1,'','')



        for vv in o[8:]:
            m5 = re.match('(\w)(\w)((\d\w)*)',vv)

            if m5:
                print(vv)
                if m5.group(1) is "f" and m5.group(2) is "o":
                    print(m5.group(1), m5.group(2))

                elif m5.group(1) is "m" and m5.group(2) is "a":
                    print(m5.group(1), m5.group(2))

                else:
                    info.turn           = int(m5.group(1))-1
                    info.move           = m5.group(2)
                    info.tile           = m5.group(3)
                    flag                = player[info.turn].player_move(info)
                    info.last_tile      = m5.group(3)
                    info.before_player  = info.turn

            for i in range(4):
                print(p_hand(player[i].hist))
                print(player[i].naki)
            print()

        
        o = ['']*8
