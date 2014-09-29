#!/usr/bin/env python

class Tile:
    def __init__(self,c):
        
        if type(c) == int:
            self.index = c
            if c < 10:
                self.string = str(c) + 'm'
            elif c < 20:
                self.string = str(c-10) + 'p'
            elif c < 30:
                self.string = str(c-20) + 's'
            elif c < 44:
                self.string = str(int((c-31)/2)+1)+'z'
    
        elif type(c) == str:
            self.string = c
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
    
        else:
            print("error")
                
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
print(Tile(1).__int__())
print(Tile('1m').__str__())
