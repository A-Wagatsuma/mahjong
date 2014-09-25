#!/usr/bin/env python

class Turn_info():
    def __init__(self, turn, last_tile, before_player, move, tile):
        self.turn           = turn
        self.last_tile      = last_tile
        self.before_player  = before_player
        self.move           = move
        self.tile           = tile
