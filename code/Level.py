from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import ENEMY_TIME, NAMING_POSITION_X
from code.Enemy import Enemy
from code.Player import Player
import pygame
import sys


class Level:
    
    def __init__(self, windows, name, start_game):
        
        self.windows = windows
        self.name = name
        self.start_game = start_game
        self.game_over_image = pygame.image.load('assets/images/FIMDEJOGO.png')
        self.entity_list: list[Entity] = []    
        self.entity_list.extend(EntityFactory.get_entity('jungle_bg'))
        self.player = EntityFactory.get_entity('Walk1')
        self.entity_list.append(self.player)
        # self.game_over_img = pygame.image.load('assets/images/FIMDEJOGO.png').convert_alpha()
        pygame.time.set_timer(ENEMY_TIME, 6000)


    def run(self,):
        pygame.mixer_music.load('assets/images/Ensiferum_In_My_SwordITrust.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            for ent in self.entity_list:
                self.windows.blit(source=ent.surf, dest=ent.rect)
                if isinstance(ent, Enemy):
                    ent.move(self.player, self)
                elif isinstance(ent, Player):
                    ent.move(self.entity_list)  # Passa a lista de entidades para o jogador
                else:
                    ent.move()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == ENEMY_TIME:
                    self.entity_list.append(EntityFactory.get_entity('InimigoWalk1'))
            self.player.move(self.entity_list) 
            pygame.display.flip()


    def game_over(self):
        self.windows.blit(self.game_over_image, (NAMING_POSITION_X))
        pygame.display.flip()
        pygame.time.wait(5000)
        from code.game import Game
        self.game = Game()
        self.game.run()
