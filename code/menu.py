import pygame
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
            pygame.display.flip()


            #checa todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

