# -*- coding: utf-8 -*-

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
        
    def getLocation(self):
        ''' Gets the ships location on the game board '''
        return self.location
    
    def setLocation(self,x,y,direction):
        ''' Sets the ships location on the game board '''
        self.location = [x,y,direction]
        
    


class Armada(object):
    
    def __init__(self):
        self.armada = [Ship('Carrier'),Ship('Battleship'),Ship('Cruiser'),Ship('Submarine'),Ship('Destroyer')]
        
    def printShips(self):
        for ship in self.armada:
            print(f"Ship: {ship.getName()}")
    
    def addShip(self, shipType):
        self.armada.append(Ship(shipType))
    
    def __len__(self):
        return len(self.armada)
    
    def __getitem__(self, index):
        return self.armada[index]