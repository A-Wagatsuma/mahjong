#!/usr/bin/env python

import sys
import fileinput
import re

k2s = { '東' : '1z', '南' : '2z', '西' : '3z', '北' : '4z', '白' : '5z', '発' :'6z', '中':'7z'}
sys.stdin = open('/dev/stdin', 'r', encoding='utf-8')
sys.stdout = open('format.txt','w', encoding='utf-8')
dealt={}
p_wind = ''
dealer = ''
# [p_wind dealer dealt1 dealt2 dealt3 dealt4 dora ura fu ....]
o = ['']*8
#print(o)
for line in fileinput.input(openhook=fileinput.hook_encoded('utf-8')):
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
    if o[0] != '' and o[5] != '' and re.match('^$',line):
        print(' '.join(o))
        #print(o)
        o = ['']*8
