import pygame
from code.menu import Menu
from code.Const import JAN_LARGURA, JAN_ALTURA,MENU_OPTIONS
from code.Level import Level


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(JAN_LARGURA,JAN_ALTURA))

    

    def run(self):

        while True: 
            menu = Menu(self.screen)
            return_menu = menu.run()

            if return_menu == MENU_OPTIONS[0]:
                level = Level(self.screen, 'Inicio', return_menu)
                level_return = level.run()
            elif return_menu == MENU_OPTIONS[2]:
                pygame.quit()
                quit()