from code.Entity import Entity
from code.EntityFactory import EntityFactory
import pygame
import sys

class Level:
    
    def __init__(self, windows, name, start_game):
        self.windows = windows
        self.name = name
        self.start_game = start_game
        self.entity_list: list[Entity] = []    
        self.entity_list.extend(EntityFactory.get_entity('jungle_bg'))

    def run(self,):
        pygame.mixer_music.load('assets/images/Ensiferum_In_My_SwordITrust.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        # clock = pygame.time.Clock()
        while True:
            # clock.tick(60)
            for ent in self.entity_list:
                self.windows.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
    pass

