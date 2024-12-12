from code.Entity import Entity
from code.Const import PLAYER_SIZE, PLAYER_POSITION
from code.Const import JAN_LARGURA
import pygame

class Player(Entity):

    def __init__(self, name:str, position:tuple):
        super().__init__(name, position)
        self.sprites = []
        for i in range (6):
            sprite_walk = pygame.image.load(f'assets/images/Walk{i}.png')
            sprite_walk= pygame.transform.scale(sprite_walk, PLAYER_SIZE)
            self.sprites.append(sprite_walk)

        self.current_sprite = 0
        self.surf = self.sprites[self.current_sprite]
        self.rect = self.surf.get_rect(topleft=position)
        self.animation_time = 100
        self.last_update_time =pygame.time.get_ticks()


        self.sprites_attack = []
        for i in range (4):
            fight = pygame.image.load(f'assets/images/Attack{i}.png')
            fight = pygame.transform.scale(fight, PLAYER_SIZE)
            self.sprites_attack.append(fight)

        self.current_sprite_attack = 0
        self.surf = self.sprites_attack[self.current_sprite_attack]
        self.rect = self.surf.get_rect(topleft=position)
        self.animation_time_attack = 100
        self.last_update_time_attack =pygame.time.get_ticks()
        # self.surf = pygame.image.load(f'assets/images/{name}.png')
        # self.surf = pygame.transform.scale(self.surf, PLAYER_SIZE)
        # self.react = self.surf.get_rect(topleft=position)

    def move(self,):
        player_speed = 3
        pressed_key = pygame.key.get_pressed()

        moved = False
        attack = False 


        if pressed_key[pygame.K_SPACE]:
            attack = True

        if pressed_key[pygame.K_RIGHT]:
            self.rect.centerx += player_speed
            moved = True
        if pressed_key[pygame.K_LEFT]:
            self.rect.centerx -= player_speed
            moved = True

                


        self.update_sprite(moved)
        self.player_attack(attack)

    
    def update_sprite(self,moved):
        if moved:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update_time > self.animation_time:
                self.last_update_time = current_time
                self.current_sprite = (self.current_sprite + 1) % len(self.sprites)
                self.surf = self.sprites[self.current_sprite]


    def player_attack(self,attack):
        if attack:
            current_time_attack = pygame.time.get_ticks()
            if current_time_attack - self.last_update_time_attack > self.animation_time_attack:
                self.last_update_time_attack = current_time_attack
                self.current_sprite_attack = (self.current_sprite_attack + 1) % len(self.sprites_attack)
                self.surf = self.sprites_attack[self.current_sprite_attack]

        