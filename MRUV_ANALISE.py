from vpython import *
#GlowScript 3.2 VPython

objeto = box(pos = vector(-250,1,0), size = vector(5,1,5), color = color.yellow)
legenda_objeto = label(pos = objeto.pos, text = 'OBJETO', xoffset = -30, yoffset = 30, box = False, heigth = 15)
solo = box(pos = vector(0,0,0), size = vector(500,0.5,3), color = color.red)
legenda_solo = label(pos = solo.pos, text = 'SOLO', xoffset = -30, yoffset = 60, box = False, heigth = 15)

grafico = graph(title = "MRUV", xtitle = "TEMPO[s]", ytitle = "DESLOCAMENTO[m]")
grafico1 = gcurve(label = "POSIÇÃO", color = color.black)
grafico2 = gcurve(label =  "VELOCIDADE", color = color.green)

tempo = 0
d_tempo = 0.01
objeto.velocidade = vector(1,0,0)
objeto.aceleração = vector(3.8,0,0)

while objeto.pos.x < (solo.size.x) / 2 :
    rate(200)
    tempo = tempo + d_tempo
    objeto.velocidade = objeto.velocidade + (objeto.aceleração * d_tempo)
    objeto.pos = objeto.pos + (objeto.velocidade * d_tempo)
    legenda_objeto.pos = objeto.pos
    grafico1.plot(tempo, objeto.pos.x)
    grafico2.plot(tempo, objeto.velocidade.x)