#class Player
from Turn_info import Turn_info

#ref:http://yak-shaver.blogspot.jp/2013/08/blog-post.html
def split_str(s, n):
    #"split string by its length"
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]

def count_pai(c, n, l):
    if n:
        tmp = 1
    else:
        tmp= -1

    if c[1] == "m" or c[1] == "M":
        index = int(c[0])
    elif c[1] == "p" or c[1] == "P":
        index = 10+int(c[0])
    elif c[1] == "s" or c[1] == "S":
        index = 20+int(c[0])
    elif c[1] == "z":
        index = 30+int(c[0])
    else:
        print("error")
        print(c,n,l)
    l[index] += tmp



class Player:
 def __init__(self, hist, reach, menzen, naki, num_call,kawa):
        self.hist       = hist
        self.reach      = reach
        self.menzen     = menzen
        self.naki       = naki
        self.kawa       = kawa
 
 def player_move(self, info):
 
    if info.move == 'G':
        count_pai(info.tile, True, self.hist)

    elif info.move == 'D' or info.move == 'd':
        count_pai(info.tile, False, self.hist)
        self.kawa.append(info.tile)

    elif info.move == 'N':
        self.menzen = False
        for c in range(2):
            count_pai(info.last_tile, False, self.hist)
        self.naki.append(['N',info.last_tile, info.last_tile, info.last_tile])

    elif info.move == 'C':
        tiles = ['C',info.last_tile]
        self.menzen = False
        for c in split_str(info.tile, 2):
            count_pai(c, False, self.hist)
            tiles.append(c)
        self.naki.append(tiles)
        pass

    elif info.move == 'K':
        #ka-kan#
        for c in self.naki:
            if 'N' in c:
                if info.tile in c:
                    c.append(info.tile)
                    c[0] = 'k'
                    return 0;
        #an-kan#
        if info.turn == info.before_player:
            for c in range(4):
                count_pai(info.last_tile, False, self.hist)
            self.naki.append(['K',info.last_tile, info.last_tile, info.last_tile, info.last_tile])
        #min-kan#
        else:
            for c in range(3):
                count_pai(info.last_tile, False, self.hist)
            self.naki.append(['k',info.last_tile, info.last_tile, info.last_tile, info.last_tile])
        pass

    elif info.move == 'A':
        if info.turn == info.before_player:
            return -1
        else:
            return 1
        pass

    elif info.move == 'R':
        self.reach = True
        pass

    return 0
