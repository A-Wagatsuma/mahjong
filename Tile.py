#!/usr/bin/env python

class Tile:
    def __init__(self, n=0, s='0m'):
    
        if n < 10:
            self.string = str(n) + 'm'
        elif n < 20:
            self.string = str(n-10) + 'p'
        elif n < 30:
            self.string = str(n-20) + 's'
        elif n < 44:
            self.string = str(int((n-31)/2)+1)+'z'
        else:
            self.string = '0m'

        if s[1] == "m" or s[1] == "M":
            self.index = 0 + int(s[0])
        elif s[1] == "p" or s[1] == "P":
            self.index = 10 + int(s[0])
        elif s[1] == "s" or s[1] == "S":
            self.index = 20 + int(s[0])
        elif s[1] == "t":
            self.index = 30 + (int(s[0])-1)*2+1
        else:
            self.index = 0
        
    def __str__(self):
        return self.string
    
    def __int__(self):
        return self.index
    
    
    
    
    
    
    
    
    '''
    def __init__(self, c):
        
        if c[1] == "m" or c[1] == "M":
                self.index = 0 + int(c[0])        
        elif c[1] == "p" or c[1] == "P":
                self.index = 10 + int(c[0])
        elif c[1] == "s" or c[1] == "S":
                self.index = 20 + int(c[0])
        elif c[1] == "z":
                self.index = 30 + (int(c[0])-1)*2+1
        else:
                print("error!")
    def __str__(self):
        if self.index < 10:
            return str(self.index)+'m'
        elif self.index < 20:
            return str(self.index-10)+'p'
        elif self.index < 30:
            return str(self.index-20)+'s'
        else:
            return str(int((self.index-31)/2)+1)+'z'
    def number(self):
        return self.index
'''

