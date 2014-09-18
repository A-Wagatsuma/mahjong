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

'''
def check_win(hist, mode): #mode 0:pair mode 1:set
    tmp_hist = hist
    tmp_list = []
    L1 = [[1,'c']]
    L2 = []
    L = []
    if mode == 0:
        for i in range(44):
            if tmp_hist[i] > 1:
                tmp_hist[i] = tmp_hist[i] - 2
                L.extend(check_win(tmp_hist, 1))
                tmp_hist[i] = tmp_hist[i] + 2
        L2 = L1[:]
        for c in L:
            #print(c)
            L1.append(c)
            #print(L1)
            tmp_list.append(L1)
            L1 = L2[:]
        return tmp_list
    
    
    elif mode == 1:
        return [[2,'a'], [3,'b']]
'''

def check_win(hist, mode): #mode 0:pair mode 1:set
    #print(hist)
    L1 = []
    L2 = []
    Ltmp = []
    ret_tmp = []
    if mode == 0:
        for i in range(10):
            if hist[i] > 1:
                #雀頭
                Ltmp = ['pair']
                for j in range(2):
                    Ltmp.append(int_2_tile(i))
                L1.append(Ltmp)

                #面子を探しにいく
                hist[i] -= 2
                set = check_win(hist, 1)
                hist[i] += 2
                for c in set:
                    Ltmp = L1[:]
                    Ltmp.append(c)
                if Ltmp != []:
                    ret_tmp.append(Ltmp)
        
        return ret_tmp
                
    elif mode == 1:
        for i in range(10):
            #刻子
            if hist[i] > 2:
                Ltmp = ['set1']
                for j in range(3):
                    Ltmp.append(int_2_tile(i))
                L1.append(Ltmp)
                #他の面子を探しにいく
                hist[i] -= 3
                set = check_win(hist, 1)
                hist[i] += 3
                for c in set:
                    Ltmp = L1[:]
                    Ltmp.append(c)
                ret_tmp.append(Ltmp)

            #順子
            elif hist[i] > 0 and hist[i+1] > 0 and hist[i+2] > 0:
                Ltmp = ['set1']
                for j in range(3):
                    Ltmp.append(int_2_tile(i+j))
                L1.append(Ltmp)
                #他の面子を探しにいく
                hist[i] -= 1
                hist[i+1] -= 1
                hist[i+2] -= 1
                set = check_win(hist, 1)
                hist[i] += 1
                hist[i+1] += 1
                hist[i+2] += 1
                for c in set:
                    Ltmp = L1[:]
                    Ltmp.append(c)
                ret_tmp.append(Ltmp)
    

        return ret_tmp




list = [0]*10
list[1] = 3
list[2] = 1
list[3] = 1
list[4] = 3

for L in check_win(list, 0):
    print(L)


