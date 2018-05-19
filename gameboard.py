# -*- coding: utf-8 -*-

class GameBoard():
    
    def __init__(self, size):
        ''' Creates the blank game board of size number of 0's ''' 
        self.size = size
        self.grid = []
        for x in range(0,10):
            self.grid.append([])
            for y in range(0,10):
                self.grid[x].append(0)
            
    def showBoard(self):
        ''' Prints the gameboard ''' 
        for i in range(0,self.size):
            print(f"{self.grid[i]}")
    
    def placePiece(self,x,y, ship):
        ''' Places the game piece on the board '''
        for i in range(0,ship.getSize()-1):    
            self.grid[x+i][y] = 1
    
    def printObj(self, ship):
        print(ship.getSize())