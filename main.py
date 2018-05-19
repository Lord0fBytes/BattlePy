#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:45:05 2018

@author: x
"""

'''class Battleship(object):
    
    def __init__(self):
        '''
import os     #System import for clearing screen
#import Ship   #This is in the ships.py file
from ships import Armada #This is in the ships.py file
from gameboard import GameBoard


def main():
    armada = Armada()
    armada.printShips()
    print(len(armada))
    newBoard = GameBoard(6)
    print(newBoard.showBoard()) 
    
    newBoard.placePiece(1,1,armada[0])
    print(newBoard.showBoard())
    
main()