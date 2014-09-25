#!/usr/bin/env python

import sys

def int_2_tile(n):
    if n < 10:
        return(str(n) + 'm')
    elif n < 20:
        return(str(n-10) + 'p')
    elif n < 30:
        return(str(n-20) + 's')
    else:
        return(str(int((n-31)/2+1)) + 'z')



def check_win(hist, mode, index): #mode 0:pair mode 1:set
    ret_tmp = []
    
    #pair
    if mode == 0:
        for i in range(44):
            if hist[i] > 1:
                Ltmp = [['pair', int_2_tile(i), int_2_tile(i)]]
                hist[i] -= 2
                set = check_win(hist, 1, 0)
                hist[i] += 2
                if set != []:
                    for c in set:
                        L1 = Ltmp[:]
                        L1.extend(c)
                        ret_tmp.append(L1)
                else:
                    ret_tmp.append(Ltmp)
        if ret_tmp == []:
            for i in range(44):
                if hist[i] > 0:
                    return [[False]]
    
    
        return ret_tmp
    #set
    elif mode == 1:
        for i in range(index,44):
            #pung
            if hist[i] > 2:
                Ltmp = [['pung', int_2_tile(i), int_2_tile(i), int_2_tile(i)]]
                hist[i] -= 3
                set = check_win(hist, 1, i)
                hist[i] += 3
                if set != []:
                    for c in set:
                        L1 = Ltmp[:]
                        L1.extend(c)
                        ret_tmp.append(L1)
                else:
                    ret_tmp.append(Ltmp)
        



            if hist[i] > 0 and hist[i+1] > 0 and hist[i+2] > 0:
                Ltmp = [['chow', int_2_tile(i), int_2_tile(i+1), int_2_tile(i+2)]]
                hist[i] -= 1
                hist[i+1] -= 1
                hist[i+2] -= 1
                set = check_win(hist, 1, i)
                hist[i] += 1
                hist[i+1] += 1
                hist[i+2] += 1
                if set != []:
                    for c in set:
                        L1 = Ltmp[:]
                        L1.extend(c)
                        ret_tmp.append(L1)
                else:
                    ret_tmp.append(Ltmp)
            
            
            
        if ret_tmp == []:
            for i in range(44):
                if hist[i] > 0:
                    return [[False]]
            
    
        return ret_tmp


    #以下テスト用
    elif mode == 2:
        return [[['set','1p'], ['set','2p']], [['set','3s'], ['set','4s']]]
    elif mode == 3:
        return []

##-----------------------------------------------------------------------------##

list = [0]*44
list[1] = 2
list[2] = 3
list[3] = 3
list[4] = 3

for L in check_win(list, 0, 0):
    if not(False in L):
        print(L)


