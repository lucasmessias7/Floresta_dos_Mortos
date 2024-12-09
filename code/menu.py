import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import JAN_LARGURA, COLOR_OPTIONS, MENU_COLOR, TEXT_1_POSITION, TEXT_3_POSITION, TEXT_FONT, TEXT_2_POSITION, NAMING_POSITION_X, MENU_OPTIONS


# pygame.init()
# pygame.font.init()

class Menu():

    def __init__(self,screen):
        self.screen = screen
        self.background = pygame.image.load('./assets/Designer_menu.png')
        self.name_game = pygame.image.load('assets/Nome_jogo_2.png')
        self.rect = self.background.get_rect()
        self.rect_name = self.name_game.get_rect()


    def run(self):    
        # pygame.mixer_music.load('assets/Dorian_Concept _Hide.mp3')
        # pygame.mixer_music.play(-1)
        menu_option = 0


        while True:
            self.screen.blit(source=self.background, dest=self.rect) 
            self.screen.blit(self.name_game, (NAMING_POSITION_X))
            

            for i in range(len(MENU_OPTIONS)):

                self.menu_text(40,MENU_OPTIONS[i],MENU_COLOR,((JAN_LARGURA/2), 450 + 50 * i))
                if i  == menu_option:
                    self.menu_text(40,MENU_OPTIONS[i],COLOR_OPTIONS,((JAN_LARGURA/2), 450 + 50 * i))
                else:
                    self.menu_text(40,MENU_OPTIONS[i],MENU_COLOR,((JAN_LARGURA/2), 450 + 50 * i))





            # checa todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1
                    
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]


            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('assets/fonts/horroroidbold.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)