import pygame
from code.Const import ENEMY_SIZE
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
            self.rect = self.surf.get_rect(topleft=position)
            self.speed = 3
            self.animation_speed = 0.1  
            self.animation_counter = 0
            self.game_over = pygame.image.load(f'assets/images/FIMDEJOGO.png')
            self.show_score = 0

    def move(self, player, level):
        self.rect.x -= self.speed
        self.animation_counter += self.animation_speed
        if self.animation_counter >= 1:
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites_enemy)
            self.surf = self.sprites_enemy[self.current_sprite]
            self.animation_counter = 0
        self.rect = self.surf.get_rect(topleft=self.rect.topleft)


        if self.rect.colliderect(player.rect):
                    if not player.attacking:
                        self.enemy_attack(player, level)
                    else:
                        player.player_attack([self])
    

    def enemy_attack(self, player, level):
        damage_sound = pygame.mixer.Sound('assets/damage.mp3')
        pygame.mixer.Sound.play(damage_sound)
        player.move_backwards()
        player.lives -= 1
        if player.lives == 0:
            level.game_over()

        #    player.life()
        
        