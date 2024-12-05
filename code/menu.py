import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import JAN_ALTURA, JAN_LARGURA, TEXT_COLOR, TEXT_1, TEXT_CENTER_POSITION, TEXT_FONT, TEXT_2


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
            
            
            # self.menu_text(text_size=70,text='Floresta',text_color=(255,255,255), text_center_pos=((JAN_LARGURA / 2), 90))
            text_one = TEXT_FONT.render(TEXT_1, True, TEXT_COLOR).convert_alpha()
            text_rect = text_one.get_rect(center=TEXT_CENTER_POSITION)
            text_two = TEXT_FONT.render(TEXT_2, True, TEXT_COLOR).convert_alpha()
            text_rect = text_one.get_rect(center=TEXT_CENTER_POSITION)
            self.screen.blit(source=text_one, dest=text_rect)

            pygame.display.flip()


            #checa todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('assets\fonts\Pixelmax-Regular.otf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)