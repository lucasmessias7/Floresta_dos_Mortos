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
            self.surf = self.sprites_enemy[self.current_sprite]
            print(f'posição inicial: , {position}')
            self.rect = self.surf.get_rect(topleft=position)
            print(f'posição final:  {self.rect}')
            print(f'tamanho da imagem: {sprite_walk.get_size()}')
            self.speed = 3
            self.animation_speed = 0.1  
            self.animation_counter = 0

    def move(self,):
        self.rect.x -= self.speed
        self.animation_counter += self.animation_speed
        if self.animation_counter >= 1:
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites_enemy)
            self.surf = self.sprites_enemy[self.current_sprite]
            self.animation_counter = 0
        self.rect = self.surf.get_rect(topleft=self.rect.topleft)
