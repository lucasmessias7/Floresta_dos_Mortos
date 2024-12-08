import pygame
pygame.init()
pygame.font.init()

#TELA DE JOGO
JAN_LARGURA = 600
JAN_ALTURA = 600

SCREEN_SIZE = 600,600


#MENU
TEXT_FONT = pygame.font.Font('assets/fonts/horroroidbold.ttf',40)
# TEXT_1 = 'Novo Jogo'
# TEXT_2 = 'Placar'
# TEXT_3 = 'Sair'
MENU_OPTIONS = (
        'Novo Jogo',
        'Placar',
        'Sair'
)
MENU_COLOR = (204,9,4)
TEXT_1_POSITION = ((JAN_LARGURA / 2), 450 )
TEXT_2_POSITION = ((JAN_LARGURA / 2), 500 )
TEXT_3_POSITION = ((JAN_LARGURA / 2), 550)
NAMING_POSITION_X = (150, 100)
COLOR_OPTIONS = (255,255,255)



VELOCIDADE_ENTIDADE = {
    'jungle_bg0' : 0,
    'jungle_bg1' : 2,
    'jungle_bg2' : 1,
    'jungle_bg3' : 1,
    'jungle_bg4' : 1,
    'jungle_bg5' : 1.6,
    'jungle_bg6' : 1,
    'jungle_bg7' : 1,
}


#Menu

# MENU_OPTIONS_POSITION = ((JAN_LARGURA / 2), 300 )
# MENU_OPTIONS = ('New Game', 
#                'Ranking',
#                'exit')