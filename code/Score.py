import pygame




class Score:

    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.image.load('./assets/images/Designer_menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self):
        pygame.mixer_music.load('assets/Dorian_Concept _Hide.mp3')
        pygame.mixer_music.play(-1)
        self.screen.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass



    def show_score(self):
        pygame.mixer_music.load('assets/Dorian_Concept _Hide.mp3')
        pygame.mixer_music.play(-1)
        self.screen.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass



    
    def score_text(self,text_size: int, text:str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typerwriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)