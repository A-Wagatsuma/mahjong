#!/usr/bin/env python
import unittest
from Tile import Tile

class TestTile(unittest.TestCase):
    def setUp(self):
        pass
    def testM(self):
        for i in range(1,9):
            s = str(i)+'m'
            self.assertEqual(i,Tile(s).number())
            self.assertEqual(s,Tile(s).__str__())
    def testP(self):
        for i in range(1,9):
            s = str(i)+'p'
            self.assertEqual(i+10,Tile(s).number())
            self.assertEqual(s,Tile(s).__str__())
    def testS(self):
        for i in range(1,9):
            s = str(i)+'s'
            self.assertEqual(i+20,Tile(s).number())
            self.assertEqual(s,Tile(s).__str__())
    def testZ(self):
        for i in range(1,7):
            s = str(i)+'z'
            self.assertEqual(i*2+29,Tile(s).number())
            self.assertEqual(s,Tile(s).__str__())

    def testI(self):
        
        self.assertEqual('7m',Tile(7).number())




if __name__ == '__main__':
    unittest.main()

