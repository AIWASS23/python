from vpython import *

scene.width = scene.height = 600
L = 50
scene.center = vec(0.05 * L,0.2 * L,0)
scene.range = 1.3 * L
#scene.caption = ( f(x,y,t) = 0.7+0.2\\sin{(10x)}\\cos{(10y)}\\cos{(2t)} \\)
scene.caption = 'Clique para alternar entre pausar ou executar.'

class plot3D:
    def __init__(self, f, xmin, xmax, ymin, ymax, zmin, zmax):
        self.f = f
        if not xmin: self.xmin = 0
        else: self.xmin = xmin
        if not xmax: self.xmax = 1
        else: self.xmax = xmax
        if not ymin: self.ymin = 0
        else: self.ymin = ymin
        if not ymax: self.ymax = 1
        else: self.ymax = ymax
        if not zmin: self.zmin = 0
        else: self.zmin = zmin
        if not zmax: self.zmax = 1
        else: self.zmax = zmax
        
        R = L/100
        d = L-2
        xaxis = cylinder(pos = vec(0,0,0), axis = vec(0,0,d), radius = R, color = color.yellow)
        yaxis = cylinder(pos = vec(0,0,0), axis = vec(d,0,0), radius = R, color = color.yellow)
        zaxis = cylinder(pos = vec(0,0,0), axis = vec(0,d,0), radius = R, color = color.yellow)
        k = 1.02
        h = 0.05 * L
        text(pos = xaxis.pos + k * xaxis.axis, text = 'x', height = h, align = 'center', billboard = True, emissive = True)
        text(pos = yaxis.pos + k * yaxis.axis, text = 'y', height = h, align = 'center', billboard = True, emissive = True)
        text(pos = zaxis.pos + k * zaxis.axis, text = 'z', height = h, align = 'center', billboard = True, emissive = True)
    
        self.vertices = []
        for x in range(L):
            for y in range(L):
                val = self.evaluate(x,y)
                self.vertices.append(self.make_vertex( x, y, val ))
        
        self.make_quads()
        self.make_normals()
        
    def evaluate(self, x, y):
        d = L - 2
        return (d / (self.zmax - self.zmin)) * (self.f(self.xmin + x * (self.xmax - self.xmin) / d, self.ymin + y * (self.ymax - self.ymin) / d) - self.zmin)
    
    def make_quads(self):
        for x in range(L - 2):
            for y in range(L - 2):
                v0 = self.get_vertex(x,y)
                v1 = self.get_vertex(x+1,y)
                v2 = self.get_vertex(x+1, y+1)
                v3 = self.get_vertex(x, y+1)
                quad(vs=[v0, v1, v2, v3])
        
    def make_normals(self):
        for i in range(L * L):
            x = int(i / L)
            y = i % L

            if x == L - 1 or y == L - 1: 
                continue
            
            v = self.vertices[i]
            a = self.vertices[i+L].pos - v.pos
            b = self.vertices[i+1].pos - v.pos
            v.normal = cross(a,b)
    
    def replot(self):
        for i in range(L * L):
            x = int(i / L)
            y = i % L
            v = self.vertices[i]
            v.pos.y = self.evaluate(x,y)
        self.make_normals()
                
    def make_vertex(self,x,y,value):
        return vertex(pos = vec(y,value,x), color = color.cyan, normal = vec(0,1,0))
        
    def get_vertex(self,x,y):
        return self.vertices[x * L + y]
        
    def get_pos(self,x,y):
        return self.get_vertex(x,y).pos

t = 0
dt = 0.02
def f(x, y):
    return 0.7 + 0.2 * sin(10 * x) * cos(10 * y) * sin(5 * t)

p = plot3D(f, 0, 1, 0, 1, 0, 1)

run = True
def running(ev):
    global run
    run = not run

scene.bind('mousedown', running)
scene.forward = vec(-0.7,-0.5,-1)

while True:
    rate(30)
    if run:
        p.replot()
        t += dt
