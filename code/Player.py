from code.Entity import Entity
from code.Const import PLAYER_SIZE, PLAYER_POSITION
from code.Const import JAN_LARGURA
import pygame

class Player(Entity):

    def __init__(self, name:str, position:tuple):
        super().__init__(name, position)
        self.sprites = []
        for i in range (6):
            sprite = pygame.image.load(f'assets/images/Walk{i}.png')
            sprite = pygame.transform.scale(sprite, PLAYER_SIZE)
            self.sprites.append(sprite)
        self.current_sprite = 0
        self.surf = self.sprites[self.current_sprite]
        self.rect = self.surf.get_rect(topleft=position)
        self.animation_time = 100
        self.last_update_time =pygame.time.get_ticks()

        # self.surf = pygame.image.load(f'assets/images/{name}.png')
        # self.surf = pygame.transform.scale(self.surf, PLAYER_SIZE)
        # self.react = self.surf.get_rect(topleft=position)

    def move(self,):
        player_speed = 3
        pressed_key = pygame.key.get_pressed()
        moved = False
        if pressed_key[pygame.K_RIGHT]:
            self.rect.centerx += player_speed
            moved = True
        if pressed_key[pygame.K_LEFT]:
            self.rect.centerx -= player_speed
            moved = True
        

        self.update_sprite(moved)

    
    def update_sprite(self,moved):
        if moved:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update_time > self.animation_time:
                self.last_update_time = current_time
                self.current_sprite = (self.current_sprite + 1) % len(self.sprites)
                self.surf = self.sprites[self.current_sprite]
 

        