from code.Entity import Entity
from code.Const import JAN_LARGURA
from code.Const import VELOCIDADE_ENTIDADE


import pygame
from code.Entity import Entity

class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.image = pygame.image.load(f'assets/images/{name}.png').convert()
        self.rect = self.image.get_rect(topleft=position)

    def move(self):
        pass  # O fundo não se move por conta própria, o deslocamento é gerenciado pelo Level



# class Background(Entity):
#     def __init__(self, name:str, position:tuple):
#         super().__init__(name, position)


#     def move(self,):
#         self.rect.centerx -= VELOCIDADE_ENTIDADE[self.name]
#         if self.rect.right <= 0:
#             self.rect.left = JAN_LARGURA