from code.Entity import Entity
from code.EntityFactory import EntityFactory
import pygame

class Level:
    
    def __init__(self, windows, name, start_game):
        self.windows = windows
        self.name = name
        self.start_game = start_game
        self.entity_list: list[Entity] = []    
        self.entity_list.extend(EntityFactory.get_entity('jungle_bg'))

    def run(self,):
        while True:
            for ent in self.entity_list:
                self.windows.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()