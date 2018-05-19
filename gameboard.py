# -*- coding: utf-8 -*-
from tkinter import *

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
        
        
class DrawBoard:
    
    def __init__(self,board,size):
        #self.ships = Button(board, text="Ship1")
        #self.ships.grid(columnspan=2)
        self.frames = []
        self.ctr = 0
        for x in range(0,size):
            self.frames.append([])
            for y in range(0,size):
                self.frames[x].append(Frame(board, width=20, height=20, bg="blue"))
                self.frames[x][y].grid(row=x+2, column=y)
                self.frames[x][y].bind("<Enter>", self.on_enter)
                self.frames[x][y].bind("<Leave>", self.on_leave)
                self.frames[x][y].bind("<Button-1>", self.mouse_click)
                
    def on_enter(self, event):
        if(event.widget.cget('bg') != 'purple'):
            event.widget.configure(bg='red')
        
    def on_leave(self, event):
        if(event.widget.cget('bg') != 'purple'):
            event.widget.configure(bg='blue')
    
    def mouse_click(self, event):
        event.widget.configure(bg='purple')
        