from vpython import *
#GlowScript 3.2 VPython

objeto = box(pos = vector(-250,1,0), size = vector(3,3,3), color = color.yellow)
solo = box(pos = vector(0,0,0), size = vector(500,0.5,3), color = color.red)

grafico1 = gcurve(color = color.blue)
grafico2 = gcurve(color = color.red)
grafico3 = gcurve(color = color.yellow)

tempo = 0
d_tempo = 0.01
objeto.velocidade = vector(1,0,0)
objeto.aceleração = vector(3.8,0,0)

while objeto.pos.x < (solo.size.x) / 2 :
    rate(200)
    tempo = tempo + d_tempo
    objeto.velocidade = objeto.velocidade + (objeto.aceleração * d_tempo)
    objeto.pos = objeto.pos + (objeto.velocidade * d_tempo)
    grafico1.plot(tempo, objeto.pos.x)
    grafico2.plot(tempo, objeto.velocidade.x)
    grafico3.plot(tempo, objeto.aceleração.x)