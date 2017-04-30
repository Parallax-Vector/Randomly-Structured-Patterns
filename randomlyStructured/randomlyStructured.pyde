import stamp
import math

#CONSTANTS
POINTS = 8
RADIUS = 380
NUMERATOR = 3
DENOMINATOR = 4

vertices = []
pointer = None

def setup():
    global pointer
    fullScreen()
    frameRate(100)
    background(51)
    pointer = stamp.Stamp(weight=2)
    translate(width/2, height/2)
    strokeWeight(5)
    stroke(255,255,255)
    for p in range(POINTS):
        angle = ((2 * PI) / POINTS * p) - PI / 4
        x = cos(angle) * RADIUS
        y = sin(angle) * RADIUS
        vertices.append((x,y))
        point(x,y)
    return

def draw():
    direction = int(math.floor(random(POINTS)))
    dX = (vertices[direction][0] - pointer.pos['x']) / DENOMINATOR * NUMERATOR
    dY = (vertices[direction][1] - pointer.pos['y']) / DENOMINATOR * NUMERATOR
    pointer.move(dX,dY)
    pointer.stamp()
    return