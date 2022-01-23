from vpython import *

objeto = sphere(pos = vector(0,1,0), radius = 1, color = color.blue)
solo = box(pos = vector(0,0,0), size = vector(200,0.5,3), color = color.red)

tempo = 0
d_tempo = 0.01
objeto.velocidade = vector(5,0,0)

while True :
    rate(300)
    tempo = tempo + d_tempo
    objeto.pos = objeto.pos + (objeto.velocidade * d_tempo)

