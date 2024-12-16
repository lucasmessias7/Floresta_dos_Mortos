from code.Entity import Entity
from code.Const import JAN_LARGURA
from code.Const import VELOCIDADE_ENTIDADE



class Background(Entity):
    def __init__(self, name:str, position:tuple):
        super().__init__(name, position)


    def move(self,):
        self.rect.centerx -= VELOCIDADE_ENTIDADE[self.name]
        if self.rect.right <= 0:
            self.rect.left = JAN_LARGURA