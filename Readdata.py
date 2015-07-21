#!/usr/bin/env python
import re

#k2s = { '東' : '1z', '南' : '2z', '西' : '3z', '北' : '4z',
#        '白' : '5z', '発' :'6z', '中':'7z'}
dic = { 'z' : '4t', 'w' : '1t', 'x' : '2t', 'y' : '3t', 
        'h' : '5t', 'i' :'6t', 'j':'7t'}
def Read_data(line, o):
    for v in dic:
        line = line.replace(v,dic[v])
    #print(line)
    m1 = re.match('  (\d)\w\d局',line)
    if m1:
        o[0] = int(m1.group(1))-1
    m2 = re.match('    \[(\d)(\d)\w]((\d\w)*)',line)
    if m2:
        if m2.group(2) == '1':
            o[1] = int(m2.group(1))-1
        o[int(m2.group(1))+1] = m2.group(3)
    m3 = re.match('    \[o\]((\d\w)+) \[裏ドラ\]((\d\w)*)',line)
    if m3:
        o[6]=m3.group(1)
        o[7]=m3.group(3)
    m4 = re.match('    \* (\w+( \w+)*)\s$',line)
    if m4:
        o.extend(m4.group(1).split(' '))
    #if m1 or m2 or m3 or m4:
        #print(line)