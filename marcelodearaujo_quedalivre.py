from vpython import *
#GlowScript 3.2 VPython

bola = sphere(pos = vector(0,15,0), radius = 0.5, color = color.yellow)
solo = box(pos = vector(0,0,0), size = vector(30,0.1,30))

g = vector(0,-10,0)
bola.v = vector(0,0,0)
t = 0
dt = 0.001

while bola.pos.y >= 0:
    rate(500)
    bola.v = bola.v + (g * dt)
    bola.pos = bola.pos + (bola.v * dt)
    t = t + dt

print(t)