#!/usr/bin/env python



def int_2_tile(n):
    if n < 10:
        return(str(n) + 'm')
    elif n < 20:
        return(str(n-10) + 'p')
    elif n < 30:
        return(str(n-20) + 's')
    else:
        return(str(n-30) + 't')


    
def check_win(hist, index): #mode 0:pair mode 1:set
    ret_tmp = []


##--------------------------------------------------------------------------------------##
## 2m2m2m3m3m4m4m5m5m6m7m8m8m8m
## 2m2m 2m3m4m 3m4m5m 5m6m7m 8m8m8m
## 8m8m 2m2m2m 3m4m5m 3m4m5m 6m7m8m
'''
hist = [0,0,3,2,2,2,1,1,3]+[0]*36

for c in Check_win.check_win(hist, 0, 0):
        print(c)
'''