import pygame
pygame.init()
pygame.font.init()

#TELA DE JOGO
JAN_LARGURA = 600
JAN_ALTURA = 600
SCREEN_SIZE = 600,600


#ENTIDADES
PLAYER_SIZE = 90,110
ENEMY_SIZE = 90,110
PLAYER_POSITION = 10,300
ENEMY_POSITION = 500, 300
ENEMY_TIME = pygame.USEREVENT + 1



#MENU
TEXT_FONT = pygame.font.Font('assets/fonts/horroroidbold.ttf',40)
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
    'jungle_bg2' : 0,
    'jungle_bg1' : 0,
    'jungle_bg3' : 0,
    'jungle_bg4' : 0,
    'jungle_bg5' : 0,
    'jungle_bg6' : 0,
    'jungle_bg7' : 0,
}


SCORE_POS = {'Title': (JAN_LARGURA / 2 , 50),
             'EnterName': (JAN_LARGURA / 2, 80),
             'Label': (JAN_LARGURA / 2, 90),
             'Name': (JAN_LARGURA / 2, 110),
             0: (JAN_LARGURA / 2 , 110),
             1: (JAN_LARGURA / 2, 130),
             2: (JAN_LARGURA / 2, 150),
             3: (JAN_LARGURA / 2, 170),
             4: (JAN_LARGURA / 2, 170)
}
