import pygame
from code.menu import Menu
from code.Const import JAN_LARGURA, JAN_ALTURA


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(JAN_LARGURA,JAN_ALTURA))

    

    def run(self):

        while True: 
            menu = Menu(self.screen)
            menu.run()
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # fill the screen with a color to wipe away anything from last frame

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip() # limits FPS to 60

        pygame.quit()