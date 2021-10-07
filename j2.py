import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
velocidade = 1

velocidade_x = velocidade
velocidade_y = velocidade

velocidade_x2 = velocidade*-1
velocidade_y2 = velocidade*-1

#Inicializando pygame
pygame.init()
#definindo tamanho da tela
tela = pygame.display.set_mode((640,480))
posicao_x = 300
posicao_y = 200

posicao_x2 = 100
posicao_y2 = 100

while True:
    evento = pygame.event.poll()
    if evento.type == pygame.QUIT:
        break
    
    #mover a bola
    posicao_x += velocidade_x
    posicao_y += velocidade_y

    posicao_x2 += velocidade_x2
    posicao_y2 += velocidade_y2

    #restrição bola vermelha
    if posicao_x>600:
        velocidade_x = velocidade_x*-1
    elif posicao_x<0:
        velocidade_x = velocidade_x*-1

    if posicao_y>440:
        velocidade_y = velocidade_y*-1
    elif posicao_y<0:
        velocidade_y = velocidade_y*-1

    #restrição bola azul
    if posicao_x2>600:
        velocidade_x2 = velocidade_x2*-1
    elif posicao_x2<0:
        velocidade_x2 = velocidade_x2*-1

    if posicao_y2>440:
        velocidade_y2 = velocidade_y2*-1
    elif posicao_y2<0:
        velocidade_y2 = velocidade_y2*-1
    
    #Desenho da bola
    tela.fill(BLACK)
    pygame.draw.ellipse(tela,RED,[posicao_x,posicao_y,40,40])

    pygame.draw.ellipse(tela,BLUE,[posicao_x2,posicao_y2,40,40])
    
    pygame.display.flip()

