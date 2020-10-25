import const
import random as rd

# 角色基本單位
class Character():
    def __init__(self, _position = const.PLAYER_POSITION):
        self.position = _position
        self.hp = 10
        self.mp = 10
        self.power = rd.randint(3,4)
        self.defense = rd.randint(1,2)
        self.state = "正常"

    def hurt(self, hp):
        self.hp -= hp
        if self.hp <= 0:
            self.hp = 0
            self.state = "死亡"
    
    def heal(self, hp):
        self.hp += hp
        if self.hp > 10:
            self.hp = 10

    def action(self, action):
        if action == "攻擊":
            return self.power
        elif action == "防禦":
            return self.defense
        else:
            return 0
            
class Player(Character):
    def __init__(self, _position = const.PLAYER_POSITION):
        super(Player, self).__init__(_position)
        self.equip = "短劍"
        self.power += 1
        self.state = "正常"
    
    def showState(self):
        print("Player's hp = " + str(self.hp))
        print("Player's mp = " + str(self.mp))
        print("Player's power = " + str(self.power))
        print("Player's defence = " + str(self.defense))
        print("Player's equip = " + str(self.equip))

    def resetPlayer(self, _data):
        self.position = _data['position']
        self.hp = _data['hp']
        self.power = _data['power']
        self.defense = _data['defense']

class Monster(Character):
    def __init__(self, _position = const.PLAYER_POSITION, _monsterName = "slime"):
        super(Monster, self).__init__(_position)
        self.name = _monsterName
        self.actinMode = const.MONSTER_ETHNICITY[_monsterName]

    def resetMonster(self, _data):
        self.position = _data['position']
        self.hp = _data['hp']
        self.power = _data['power']
        self.defense = _data['defense']
        self.name = _data['name']
        self.actinMode = const.MONSTER_ETHNICITY[self.name]
        self.state = _data['state']

    def showState(self):
        print("monster's position = " + str(self.position))
        print("monster's hp = " + str(self.hp))
        print("monster's mp = " + str(self.mp))
        print("monster's power = " + str(self.power))
        print("monster's defence = " + str(self.defense))
        print("monster's state = " + str(self.state))
        print("monster's name = " + str(self.name))
        print("monster's actionMode = " + str(self.actinMode))
