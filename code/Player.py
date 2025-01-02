from code.Entity import Entity
from code.Const import PLAYER_SIZE,NAMING_POSITION_X
from code.Enemy import Enemy
import pygame


class Player(Entity):

    def __init__(self, name:str, position:tuple):
        super().__init__(name, position)
        self.attacking = False
        self.game_over = pygame.image.load(f'assets\images\FIMDEJOGO.png').convert_alpha()
        self.rect_name = self.game_over.get_rect(topleft = position)
        self.sprites = []
        for i in range (6):
            sprite_walk = pygame.image.load(f'assets/images/Walk{i}.png').convert_alpha()
            sprite_walk= pygame.transform.scale(sprite_walk, PLAYER_SIZE).convert_alpha()
            self.sprites.append(sprite_walk)

        self.current_sprite = 0
        self.surf = self.sprites[self.current_sprite]
        self.rect = self.surf.get_rect(topleft=position)
        self.animation_time = 100
        self.last_update_time =pygame.time.get_ticks()
        self.score = 0

        self.sprites_attack = []
        for i in range (4):
            fight = pygame.image.load(f'assets/images/Attack{i}.png').convert_alpha()
            fight = pygame.transform.scale(fight, PLAYER_SIZE).convert_alpha()
            print(f'tamanho da imagem {fight.get_size()}')
            self.sprites_attack.append(fight)

        self.current_sprite_attack = 0
        self.surf = self.sprites_attack[self.current_sprite_attack]
        self.rect = self.surf.get_rect(topleft=position)
        self.animation_time_attack = 100
        self.last_update_time_attack =pygame.time.get_ticks()
        
        self.lives = 3

    def move(self,entity_list):
        player_speed = 3
        pressed_key = pygame.key.get_pressed()

        moved = False

        if pressed_key[pygame.K_RIGHT]:
            self.rect.centerx += player_speed
            moved = True
        if pressed_key[pygame.K_LEFT]:
            self.rect.centerx -= player_speed
            moved = True

        if pressed_key[pygame.K_SPACE]:
            self.attacking = True
          

        self.player_attack(entity_list)
        self.update_sprite(moved)


    def move_backwards(self):
        self.rect.x -= 50


    def update_sprite(self,moved):
        if moved:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update_time > self.animation_time:
                self.last_update_time = current_time
                self.current_sprite = (self.current_sprite + 1) % len(self.sprites)
                self.surf = self.sprites[self.current_sprite]


    def player_attack(self, entity_list):
        if self.attacking:
            current_time_attack = pygame.time.get_ticks()
            if current_time_attack - self.last_update_time_attack > self.animation_time_attack:
                self.last_update_time_attack = current_time_attack
                self.current_sprite_attack = (self.current_sprite_attack + 1) % len(self.sprites_attack)
                self.surf = self.sprites_attack[self.current_sprite_attack]
            if self.current_sprite_attack == len(self.sprites_attack) - 1:
                self.attacking = False

        enemies_to_remove = []
        for entity in entity_list:
            if isinstance(entity, Enemy) and self.rect.colliderect(entity.rect):
                if entity not in enemies_to_remove:  # Verifica se o inimigo já está na lista
                    enemies_to_remove.append(entity)
                    self.score += 0.5  # Incrementa a pontuação ao derrotar um inimigo
                    print(f"Pontuação: {self.score}")  # Adiciona um print para depuração

        # Remover inimigos fora do loop de colisão
        for enemy in enemies_to_remove:
            entity_list.remove(enemy)



    def show_score(self, screen):
        font = pygame.font.Font(None, 36)
        score_display = font.render("Score: " + str(self.score), True, (220, 20, 60))
        screen.blit(score_display, (10, 10))
    
    
    def show_live(self, screen):
        font = pygame.font.Font(None, 36)
        score_display = font.render("Vida: " + str(self.lives), True, (220, 20, 60))
        screen.blit(score_display, (10, 40))