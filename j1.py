import pygame
import time

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

#Inicializando pygame
pygame.init()
#definindo tamanho da tela
tela = pygame.display.set_mode((640,480))
#Alterando o titulo do jogo - barra de título
pygame.display.set_caption('Aula de Hoje')
#Definindo cor de fundo
tela.fill(BLACK)

pygame.draw.line(tela, WHITE, [10,100], [630,100], 5)
pygame.draw.rect(tela, BLUE, [200,210,40,20])
pygame.draw.ellipse(tela, RED, [300,200,40,40])
pygame.draw.polygon(tela,GREEN, [[420,200],[440,240],[400,240]])

#Atualizando tela
pygame.display.flip()

fonte = pygame.font.SysFont(None,55)
texto = fonte.render('Introdução', True, WHITE)
tela.blit(texto,[230,300])

time.sleep(3)

texto2 = fonte.render('a Programação', True, WHITE)
tela.blit(texto2,[200,350])

#Atualizando tela
pygame.display.flip()

time.sleep(1)

tela.fill(BLACK)
pygame.display.flip()
