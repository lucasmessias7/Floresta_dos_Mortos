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
        menu_option = 'text_one'

        while True:
            self.screen.blit(source=self.background, dest=self.rect) 
            self.screen.blit(self.name_game, (NAMING_POSITION_X))
            
            # # renderizando os textos
            # text_one = TEXT_FONT.render(TEXT_1, True, TEXT_COLOR).convert_alpha()
            # text_two = TEXT_FONT.render(TEXT_2, True, TEXT_COLOR).convert_alpha()
            # text_three = TEXT_FONT.render(TEXT_3, True, TEXT_COLOR).convert_alpha()

            
            # #criando o retangulo para cada texto
            # text_rect = text_one.get_rect(center=TEXT_1_POSITION)
            # text_react_2 = text_two.get_rect(center=TEXT_2_POSITION)
            # text_react_3 = text_three.get_rect(center=TEXT_3_POSITION)
            

            # # desenhando os textos na tela
            # self.screen.blit(source=text_one, dest=text_rect)
            # self.screen.blit(source=text_two, dest=text_react_2)
            # self.screen.blit(source=text_three, dest=text_react_3)
            for i in range(len(MENU_OPTIONS)):
                self.menu_text(40,MENU_OPTIONS[i],MENU_COLOR,((JAN_LARGURA/2), 450 + 50 * i))


            pygame.display.flip()


            # Menu de opções

        



            # checa todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('assets/fonts/horroroidbold.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)