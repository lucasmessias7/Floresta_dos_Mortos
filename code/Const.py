import pygame
pygame.init()
pygame.font.init()


JAN_LARGURA = 600
JAN_ALTURA = 600
TEXT_FONT = pygame.font.Font('assets/fonts/Pixelmax-Regular.otf',40)
TEXT_1 = 'Novo Jogo'
TEXT_2 = 'Placar'
TEXT_COLOR = (255,255,255)
TEXT_1_POSITION = ((JAN_LARGURA / 2), 450 )
TEXT_2_POSITION = ((JAN_LARGURA / 2), 500 )


#Menu
MENU_OPTIONS_POSITION = ((JAN_LARGURA / 2), 300 )
MENU_OPTIONS = ('New Game', 
               'Ranking',
               'exit')