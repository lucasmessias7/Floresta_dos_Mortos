import pygame
from code.Const import PLAYER_SIZE,ENEMY_SIZE
from code.Entity import Entity

class Enemy(Entity):


    def __init__(self, name:str, position:tuple):
            super().__init__(name, position)
            self.sprites_enemy = []
            for i in range (7):
                sprite_walk = pygame.image.load(f'assets/images/InimigoWalk{i}.png')
                sprite_walk= pygame.transform.scale(sprite_walk, ENEMY_SIZE)
                self.sprites_enemy.append(sprite_walk)
            self.current_sprite = 0
            self.image = self.sprites_enemy[self.current_sprite]
            print(f'posição inicial: , {position}')
            self.rect = self.image.get_rect(topleft=position)
            print(f'posição final:  {self.rect}')
            self.speed = 3

    def move(self,):
        self.rect.x -= self.speed
        self.current_sprite = (self.current_sprite + 1) % len(self.sprites_enemy)
        self.image = self.sprites_enemy[self.current_sprite]
