class Stamp():
    def __init__(self,weight=5,colour=(255,255,255)):
        self.weight = weight
        self.r = colour[0];self.g = colour[1];self.b = colour[2]
        self.pos = {'x': 0, 'y': 0}
        return
    
    def move(self,x,y):
        self.pos['x'] += x
        self.pos['y'] += y
        return
    
    def stamp(self):
        strokeWeight(self.weight)
        stroke(self.r,self.g,self.b)
        translate(width / 2, height / 2)
        point(self.pos['x'],self.pos['y'])
        return