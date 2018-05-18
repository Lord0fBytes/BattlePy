#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:45:05 2018

@author: x
"""

'''class Battleship(object):
    
    def __init__(self):
        '''
import os
        

class Ship(object):
    
    def __init__(self, shipName):
        self.name = shipName
        self.health=100
        if(shipName == 'Carrier'):
            self.size=5
        elif(shipName == 'Battleship'):
            self.size=4
        elif(shipName == 'Cruiser'):
            self.size=3
        elif(shipName == 'Submarine'):
            self.size=3
        elif(shipName == 'Destroyer'):
            self.size=2
    
    def getHealth(self):
        return self.health
    
    def getSize(self):
        return self.size
    
    def getName(self):
        return self.name
    
    def hit(self):
        self.health*=1-(1/self.size)
        
        
class Armada(object):
    
    def __init__(self):
        self.armada = []
        
    def printShips(self):
        for ship in self.armada:
            print(f"Ship: {ship.getName()}")
    
    def addShip(self, shipType):
        self.armada.append(Ship(shipType))
        
        

        
def AddShip(armada):
    os.system('clear')
    shipName = input("Ship: (C)arrier, (B)attleship, C(r)uiser, (S)ubmarine, (D)estroyer\n:")
    if(shipName == 'C'):
        name = 'Carrier'
    elif(shipName == 'B'):
        name = 'Battleship'
    elif(shipName == 'R'):
        name = 'Cruiser'
    elif(shipName == 'S'):
        name = 'Submarine'
    elif(shipName == 'D'):
        name = 'Destroyer'
    armada.addShip(name)
    print(f"{armada[len(armada)-1].getName()} has beean added")
    

def RemoveShip():
    pass

def ViewArmada(armada):
    armada.printShips()

def HitShip():
    pass  

def mainMenu(choice, armada):
    if(choice == 'a'):
        AddShip(armada)
    elif(choice == 'r'):
        RemoveShip()
    elif(choice == 'v'):
        ViewArmada(armada)
    elif(choice == 'h'):
        HitShip()

def main():
    armada = Armada()
    while True:
        #This should be a loop for the player
        #There will be (a)dd, (r)emove, (v)iew armada, (h)it ship
        print(f"Main Menu: (a)dd, (r)emove, (v)iew armada, (h)it ship, (q)uit")
        cmdMain = input("Option: ")
        
        if(cmdMain == 'q'):
            break
        else:
            mainMenu(cmdMain, armada)
        

    
    
main()