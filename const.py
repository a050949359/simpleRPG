# Constant 
class _const:
    class ConstError(TypeError):pass
    def __setattr__(self,name,value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" %name)
        self.__dict__[name]=value
        
import sys
sys.modules[__name__]=_const()

import const

const.MAZE_MAP = [[2,2,2,2,2,2,2,2],
                [2,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,2],
                [2,2,2,2,2,2,2,2]]

const.PLAYER_POSITION = [1,1]
const.MONSTER_POSITION = [2,2]
const.MONSTER_ETHNICITY = {"slime":'1111112223'}
const.MONSTER_AMOUNT = 5
const.VICTORY_MP3 = 'fanfare.mp3'