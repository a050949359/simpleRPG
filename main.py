import const
from getkey import getkey, keys
from MapSystem import Map
from GameUnit import Player, Monster
from FightSystem import Fight
import Menu
# load map and display
mapS = Map(const.MAZE_MAP)

while True:
    mapS.showMap()
    print("------------------------------------")
    print("Press Arrow key to Move ")
    print("Press 'ESC' to menu ")
    print("Press 's' show player status ")
    print("------------------------------------")
    print("enter key:")
    
    # wait press keyboard
    key = getkey()
    result = False

    # show state
    if key == 's' or key == 'S':
        mapS.showPlayerState()
        mapS.showMonsterState()
    
    #show menu
    elif key == keys.ESC:
        command = Menu.showMenu()
        # leave game
        if command == keys.ESC:
            Menu.showGameOver()
            break

        # save
        elif command == 's' or command == 'S':
            keySave = Menu.showSaveMenu(mapS.getSaveData())
            if keySave == '1' or keySave == '2' or keySave == '3':
                mapS.saveGame(keySave)
                Menu.showSaveSuccess()
        
        # load
        elif command == 'l' or command == 'L':
            keyLoad = Menu.showSaveMenu(mapS.getSaveData())
            if keyLoad == '1' or keyLoad == '2' or keyLoad == '3':
                if mapS.loadGame(keyLoad):
                    # mapS.showPlayerState()
                    # mapS.showMonsterState()
                    Menu.showLoadSuccess()
                else:
                    Menu.showLoadFailed()
        
        # delete
        elif command == 'd' or command == 'D':
            keyDel = Menu.showSaveMenu(mapS.getSaveData())
            if keyDel =='1' or keyDel == '2' or keyDel == '3':
                if mapS.deleteSave(keyDel):
                    Menu.showDeleteSuccess()
                else:
                    Menu.showDeleteFailed()

    # get up down left right esc
    if key == keys.LEFT:
        positionNumber = mapS.moveTo("left")
    elif key == keys.RIGHT:
        positionNumber = mapS.moveTo("right")     
    elif key == keys.UP:
        positionNumber = mapS.moveTo("up") 
    elif key == keys.DOWN:
        positionNumber = mapS.moveTo("down")
    else:
        continue

    # check enter result
    gameOver, targetNumber = mapS.checkPositionNumber(positionNumber)
    if gameOver:
        Menu.showGameOver()
        break
    elif not gameOver and targetNumber == 3:
        Menu.showVictory()
    
    