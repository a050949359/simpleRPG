from getkey import getkey
from subprocess import call 
from GameUnit import Player, Monster
from FightSystem import Fight
import random
import const
import json

class Map():
    def __init__(self, _map):
        self.map = _map
        self.player = self.createPlayer()
        self.monsterList = self.createMonster(const.MONSTER_AMOUNT)

    def createPlayer(self):
        self.map[const.PLAYER_POSITION[0]][const.PLAYER_POSITION[1]] = 1
        return Player(const.PLAYER_POSITION)

    def createMonster(self, _amount):
        amount = _amount
        monsterList = []
        while amount > 0:
            x = random.randrange(1,len(self.map[0]))
            y = random.randrange(1,len(self.map))

            if self.map[y][x] == 0:
                monsterList.append(Monster([y,x],"slime"))
                self.map[y][x] = 3
                amount -= 1
            else:
                continue
        
        return monsterList

    def showMap(self):
        call('clear') 
        for i in range(len(self.map)):
            print(self.map[i])
            
    def moveTo(self, direction):
        moveVector = []
        if direction == "left":
            moveVector = [0, -1]
        elif direction == "right":
            moveVector = [0, 1]
        elif direction == "up":
            moveVector = [-1, 0]
        elif direction == "down":
            moveVector = [1, 0]

        destination = [self.player.position[0] + moveVector[0], self.player.position[1] + moveVector[1]]
        positionNum = self.map[destination[0]][destination[1]]
        if self.map[destination[0]][destination[1]] != 2:
            self.move(destination)
            return positionNum
        else:
            return positionNum
        
    def move(self, destination):
        self.map[self.player.position[0]][self.player.position[1]] = 0
        self.map[destination[0]][destination[1]] = 1
        self.player.position = destination

    def searchMonster(self, _position):
        for monster in self.monsterList:
            if monster.position == _position:
                return monster

    def checkPositionNumber(self, result):
        if result == 0:
            self.showMap()
            return False, result
        if result == 3:
            enemy = self.searchMonster(self.player.position)
            fight = Fight(self.player, enemy)

            while fight.end != True:
                fight.showCommandList()
                action = fight.waitCommand()
                isEnd = fight.getCommandResult(action)
                getkey("press any key")
                if isEnd == True:
                    return fight.displayFightResult(), result

        else:
            return False, result

    def showPlayerState(self):
        call('clear')
        self.player.showState()
        getkey()

    def showMonsterState(self):
        for monster in self.monsterList:
            call('clear')
            monster.showState()
            getkey()

    def saveGame(self,_no):
        try:
            with open('saveData.txt', 'r') as jsonFile:
                originalData = json.load(jsonFile)
        
                saveDict = {}
                saveDict['map'] = self.map
                saveDict['player'] = {'position':self.player.position,
                                        'hp':self.player.hp,
                                        'power':self.player.power,
                                        'defense':self.player.defense}

                saveDict['monster'] = []
                for i, monster in enumerate(self.monsterList):
                    saveDict['monster'].append({'position':monster.position,
                                                'hp':monster.hp,
                                                'power':monster.power,
                                                'defense':monster.defense,
                                                'name':monster.name,
                                                'state':monster.state})
                    
                originalData[_no] = saveDict
                with open('saveData.txt', 'w') as outfile:
                    json.dump(originalData, outfile)
        except:
            dataDict = {}
            dataDict['map'] = self.map
            dataDict['player'] = {'position':self.player.position,
                                    'hp':self.player.hp,
                                    'power':self.player.power,
                                    'defense':self.player.defense}

            dataDict['monster'] = []
            for i, monster in enumerate(self.monsterList):
                dataDict['monster'].append({'position':monster.position,
                                            'hp':monster.hp,
                                            'power':monster.power,
                                            'defense':monster.defense,
                                            'name':monster.name,
                                            'state':monster.state})

            saveDict = {_no:dataDict}
            with open('saveData.txt', 'w') as outfile:
                    json.dump(saveDict, outfile)

    def loadGame(self,_no):
        call('clear')
        try:
            with open('saveData.txt', 'r') as jsonFile:
                data = json.load(jsonFile)
                if data[_no]: 
                    self.resetMapSystem(data[_no])
                    self.resetPlayer(data[_no]['player'])
                    self.resetMonsterList(data[_no]['monster'])
                    return True
                else:
                    return False
        except:
            return False

    def deleteSave(self, _no):
        try:
            with open('saveData.txt', 'r') as jsonFile:
                originalData = json.load(jsonFile)
                if originalData[_no]:
                    del originalData[_no]
                else:
                    return False
            with open('saveData.txt', 'w') as outfile:
                json.dump(originalData, outfile)
                return True
        except:
            return False


    def resetMapSystem(self,_data):
        self.map = _data['map']
    
    def resetPlayer(self,_data):
        self.player.resetPlayer(_data)
        
    def resetMonsterList(self,_data):
        self.monsterList.clear()
        for monsterData in _data:
            monster = Monster()
            monster.resetMonster(monsterData)
            self.monsterList.append(monster)
        
    def getSaveData(self):
        try:
            with open('saveData.txt', 'r') as jsonFile:
                return json.load(jsonFile)
        except:
            return {}