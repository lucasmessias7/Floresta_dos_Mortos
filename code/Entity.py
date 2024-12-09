from abc import ABC, abstractmethod
import pygame.image
from code.Const import SCREEN_SIZE

class Entity(ABC):

    def __init__ (self, name:str, position:tuple):
        self.name = name 
        self.surf = pygame.image.load('assets/images/' + name + '.png')
        self.surf = pygame.transform.scale(self.surf, SCREEN_SIZE)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0



    @abstractmethod
    def move(self, ):
        pass