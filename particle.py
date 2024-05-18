import random
import numpy as np

class particle():
    def __init__(self, pos, speed, color):
        self.pos = pos
        self.speed = speed
        self.color = color
    
    def update_pos(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
    
    def check_colisions(self, width, height):
        print(self.pos)
        if(self.pos[0] <= 0 or self.pos[0] >= width):
            self.speed[0] *= -1
        if(self.pos[1] <= 0 or self.pos[1] >= height):
            self.speed[1] *= -1

def random_particle(width, height, speed_cap):
    p = particle(pos = np.array([random.randint(0, width), 
                           random.randint(0, height)]),
                speed = np.random.randint(1, speed_cap, size = 2),
                color = np.random.randint(256, size = 3))
    return(p)       