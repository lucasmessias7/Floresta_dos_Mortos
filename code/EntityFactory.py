from code.Background import Background
from code.Const import JAN_LARGURA

class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'jungle_bg':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'jungle_bg{i}', (0,0)))
                    list_bg.append(Background(f'jungle_bg{i}', (JAN_LARGURA,0)))
                return list_bg
                

