from code.Background import Background
from code.Const import JAN_LARGURA,PLAYER_POSITION, ENEMY_POSITION
from code.Player import Player
from code.Enemy import Enemy
import random
class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str, position=(0,0), level = None):
        match entity_name:
            case 'jungle_bg':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'jungle_bg{i}', (0,0)))
                    list_bg.append(Background(f'jungle_bg{i}', (JAN_LARGURA,0)))
                return list_bg
            
            case 'Walk1':
                return Player('Walk1', PLAYER_POSITION)
            
            case 'InimigoWalk1':
                return Enemy('InimigoWalk1', ENEMY_POSITION)
                
                

