from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import ENEMY_TIME, NAMING_POSITION_X, JAN_LARGURA
from code.Enemy import Enemy
from code.Player import Player
from code.Background import Background
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
        self.bg_offset_x = 0
        self.bg_images = [pygame.image.load(f'assets/images/jungle_bg{i}.png').convert() for i in range(0,8)]
        # self.game_over_img = pygame.image.load('assets/images/FIMDEJOGO.png').convert_alpha()
        pygame.time.set_timer(ENEMY_TIME, 6000)


    def run(self,):
        pygame.mixer_music.load('assets/images/Ensiferum_In_My_SwordITrust.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == ENEMY_TIME:
                    self.entity_list.append(EntityFactory.get_entity('InimigoWalk1'))

            # Atualiza o deslocamento do fundo com base no movimento do jogador
            self.update_bg_offset()

            # Desenha o fundo com base no deslocamento
            self.draw_background()

            for ent in self.entity_list:
                if isinstance(ent, Enemy):
                    ent.move(self.player, self)
                elif isinstance(ent, Player):
                    ent.move(self.entity_list)  # Passa a lista de entidades para o jogador
                else:
                    ent.move()
                self.windows.blit(source=ent.surf, dest=ent.rect)

            self.player.show_score(self.windows)
            self.player.show_live(self.windows)
            pygame.display.flip()

    def update_bg_offset(self):
        player_speed = 3
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT]:
            self.bg_offset_x -= player_speed
        if pressed_key[pygame.K_LEFT]:
            self.bg_offset_x += player_speed
        print(f"bg_offset_x: {self.bg_offset_x}")

    def draw_background(self):
        bg_width = self.bg_images[0].get_width()
        for i in range(len(self.bg_images)):
            x_position = (self.bg_offset_x + i * bg_width) % (bg_width * len(self.bg_images))
            if x_position < 0:
                x_position += bg_width * len(self.bg_images)
            print(f"x_position: {x_position}")
            self.windows.blit(self.bg_images[i], (x_position, 0))
            # Desenha a imagem novamente para criar um efeito de rolagem contínua
            self.windows.blit(self.bg_images[i], (x_position - bg_width * len(self.bg_images), 0))

    def game_over(self):
        self.windows.blit(self.game_over_image, (NAMING_POSITION_X))
        pygame.display.flip()
        pygame.time.wait(5000)
        from code.Score import Score
        self.score = Score(self.windows)
        self.score.save()



