import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import JAN_ALTURA, JAN_LARGURA, TEXT_COLOR, TEXT_1, TEXT_1_POSITION, TEXT_FONT, TEXT_2, TEXT_2_POSITION, MENU_OPTIONS,MENU_OPTIONS_POSITION


# pygame.init()
# pygame.font.init()

class Menu():

    def __init__(self,screen):
        self.screen = screen
        self.background = pygame.image.load('./assets/Designer_menu.png')
        self.rect = self.background.get_rect()


    def run(self):    
        pygame.mixer_music.load('assets/Dorian_Concept _Hide.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.screen.blit(source=self.background, dest=self.rect) 
            
            # renderizando os textos
            text_one = TEXT_FONT.render(TEXT_1, True, TEXT_COLOR).convert_alpha()
            text_two = TEXT_FONT.render(TEXT_2, True, TEXT_COLOR).convert_alpha()

            
            #criando o retangulo para cada texto
            text_rect = text_one.get_rect(center=TEXT_1_POSITION)
            text_react_2 = text_two.get_rect(center=TEXT_2_POSITION)
            

            # desenhando os textos na tela
            self.screen.blit(source=text_one, dest=text_rect)
            self.screen.blit(source=text_two, dest=text_react_2)

            pygame.display.flip()


            # Menu de opções

        



            # checa todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('assets\fonts\Pixelmax-Regular.otf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)