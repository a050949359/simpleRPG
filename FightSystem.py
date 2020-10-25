from getkey import getkey, keys
from GameUnit import Player, Monster
from subprocess import call 
import random as rd

class Fight():
    def __init__(self, _own, _enemy):
        self.end = False
        self.own = _own
        self.enemy = _enemy
    # 顯示血量與指令表
    def showCommandList(self):
        call('clear') 
        print("*** F * I * G * H  * T ***")
        print("Player HP : " + str(self.own.hp )+"/10")
        print("Eneny  HP : " + str(self.enemy.hp) +"/10\n")
    
        print("1. 攻擊")
        print("2. 防禦")
        print("3. 發呆")
        print("4. 狀態")
        print("**************************")
    
    # 等待使用者輸入
    def waitCommand(self):
        while True:
            action = input("請輸入指令:")
            if len(action) == 1 and '1234'.find(action) != -1:
                return action
            else:
                self.showCommandList()
                print("輸入錯誤")

    # 隨機選擇敵人行動
    def randomEnenyAction(self):
        # 1攻擊 2防禦 3發呆
        return rd.choice(self.enemy.actinMode)

    # 計算雙方行動結果
    def getCommandResult(self, ownAction):
        if ownAction != "4":
            enemyAction = self.randomEnenyAction()
            if ownAction == "1":
                myPower = self.own.power
                myDefense = self.own.defense
            elif ownAction == "2":
                myPower = 0
                myDefense = self.own.defense + 2
            elif ownAction == "3":
                myPower = 0
                myDefense = 0

            if enemyAction == "1":
                enemyPower = self.enemy.power
                enemyDefense = self.enemy.defense
            elif enemyAction == "2":
                enemyPower = 0
                enemyDefense = self.enemy.defense + 2
            elif enemyAction == "3":
                enemyPower = 0
                enemyDefense = 0

            myHurt = enemyPower - myDefense
            enemyHurt = myPower - enemyDefense
            self.own.hurt(myHurt if myHurt >= 0 else 0)
            self.enemy.hurt(enemyHurt if enemyHurt >= 0 else 0)

            print("You suffered",str(myHurt if myHurt >= 0 else 0),"damage")
            print("Enemy suffered",str(enemyHurt if enemyHurt >= 0 else 0),"damage")

            if self.own.hp == 0 or self.enemy.hp == 0:
                return True
            else:
                return False
            
        else:
            self.showStats()
            return False

    # 戰鬥結果
    def displayFightResult(self):
        if self.own.state == "死亡":
            print("your HP is 0")
            print("press any key")
            getkey()
            return True
            
        elif self.enemy.state == "死亡":
            print("enemy's HP is 0")
            print("press any key")
            getkey()
            self.enemy.state = "死亡"
            return False

    # 指令4
    def showStats(self):
        print("{:>8}{:>8}{:>8}".format("","Player","Enemy"))
        print("{:>8}{:>8}{:>8}".format("power",self.own.power,self.enemy.power))
        print("{:>8}{:>8}{:>8}".format("defense",self.own.defense,self.enemy.defense))