from getkey import getkey,keys
from subprocess import call 
import const
import os

def showStartView():
    file = "prelude.mp3"
    os.system("afplay " + file)
    call('clear')
    print("**************************")
    print("\n\n\n\n")
    print("        Simple RPG        ")
    print("\n")
    print("  press any key to start  ")
    print("\n\n\n\n")
    print("**************************")
    return getkey()

def showSaveMenu(saves):
    call('clear')
    print("**************************")
    print("\n\n\n\n")
    if checkKey(saves, '1'):
        print("          save  1         ")
    else:
        print("      save  1 no data     ")
    if checkKey(saves, '2'):
        print("          save  2         ")
    else:
        print("      save  2 no data     ")
    if checkKey(saves, '3'):
        print("          save  3         ")
    else:
        print("      save  3 no data     ")
        print("       press b back       ")
    print("\n\n\n")
    print("**************************")
    while True:
        key = getkey()
        if key == '1' or key == '2' or key == '3' or \
            key == 'b' or key == 'B':
            return key

def showMenu():
    call('clear')
    print("******** M E N U *********")
    print("\n\n\n")
    print("       s  = Save")
    print("       l  = Load")
    print("       d  = delete save")
    print("      esc = leave")
    print("       b  = back")
    print("\n\n\n")
    print("**************************")
    while True:
        key = getkey()
        if key == keys.ESC or \
            key == 's' or key == 'S' or \
            key == 'l' or key == 'L' or \
            key == 'd' or key == 'D' or \
            key == 'b' or key == 'B':
            return key


def showSaveSuccess():
    call('clear')
    print("******** M E N U *********")
    print("\n\n\n\n\n")
    print("       Save success       ")
    print("\n\n\n\n\n")
    print("**************************")
    return getkey()

def showLoadSuccess():
    call('clear')
    print("******** M E N U *********")
    print("\n\n\n\n\n")
    print("       Load success       ")
    print("\n\n\n\n\n")
    print("**************************")
    return getkey()

def showDeleteSuccess():
    call('clear')
    print("******** M E N U *********")
    print("\n\n\n\n\n")
    print("      delete success      ")
    print("\n\n\n\n\n")
    print("**************************")
    return getkey()

def showDeleteSuccess():
    call('clear')
    print("******** M E N U *********")
    print("\n\n\n\n\n")
    print("      delete success      ")
    print("\n\n\n\n\n")
    print("**************************")
    return getkey()

def showDeleteFailed():
    call('clear')
    print("******** M E N U *********")
    print("\n\n\n\n")
    print("       delete failed      ")
    print("      file not exist      ")
    print("         or no data       ")
    print("\n\n\n\n\n")
    print("**************************")
    return getkey()

def showLoadFailed():
    call('clear')
    print("******** M E N U *********")
    print("\n\n\n\n")
    print("       Load failed        ")
    print("\n")
    print(" You don't have save Data ")
    print("\n\n\n\n")
    print("**************************")
    return getkey()

def showGameOver():
    call('clear')
    print("******** M E N U *********")
    print("\n\n\n\n")
    print("    G A M E    O V E R    ")
    print("\n")
    print("           orz            ")
    print("\n\n\n\n")
    print("**************************")
    getkey()
    call('clear')

def showVictory():
    call('clear') 
    print("**************************")
    print("\n\n\n\n")
    print("          Victory         ")
    print("\n")
    print("         ㄟ(≧◇≦)ㄏ         ")
    print("\n\n\n\n")
    print("**************************")
    # play music
    # os.system("afplay " + const.VICTORY_MP3)
    return getkey()

def checkKey(dict, key): 
    if key in dict.keys(): 
        return True
    else: 
        return False