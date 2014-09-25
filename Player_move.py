#!/usr/bin/env python

class Player_move():
    
        if move == 'G':
            count_pai(tile, True, self.hist)
            pass
                
                elif move == 'D':
                    self.kawa.append(last)
                    count_pai(tile, False, self.hist)
                    self.kawa.append(tile)
                    pass
                
                elif move == 'd':
                    self.kawa.append(last)
                    count_pai(tile, False, self.hist)
                    self.kawa.append(tile)
                    pass
                
                elif move == 'N':
                    self.menzen = False
                    for c in range(2):
                        count_pai(last, False, self.hist)
                    self.naki.append(['N',last, last, last])
                    pass
                
                elif move == 'C':
                    tiles = ['C',last]
                    self.menzen = False
                    for c in split_str(tile, 2):
                        count_pai(c, False, self.hist)
                        tiles.append(c)
                    self.naki.append(tiles)
                    pass
                
                elif move == 'K':
                    #ka-kan#
                    for c in self.naki:
                        if 'N' in c:
                            if tile in c:
                                c.append(tile)
                                c[0] = 'k'
                                return 0;
                    #an-kan#
                    if turn == before:
                        for c in range(4):
                            count_pai(last, False, self.hist)
                        self.naki.append(['K',last, last, last, last])
                    #min-kan#
                    else:
                        for c in range(3):
                            count_pai(last, False, self.hist)
                        self.naki.append(['k',last, last, last, last])
                    pass
                
                elif move == 'A':
                    if turn == before:
                        return -1
                    else:
                        return 1
                    pass
                
                elif move == 'R':
                    self.reach = True
                    pass
