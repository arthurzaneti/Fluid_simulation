import random
import numpy as np

class particle():
    def __init__(self, pos, speed, color):
        self.pos = pos
        self.speed = speed
        self.color = color
        self.radius = 10
    
    def update_pos(self):
        self.speed[1] += 0.2
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
    
    def check_colisions_walls(self, width, height):
        if(self.pos[0] - self.radius < 0 or self.pos[0] + self.radius > width):
            self.speed[0] *= -0.8 
        if(self.pos[1] + self.radius < 0 or self.pos[1] > height - self.radius):
            self.speed[1] *= -0.8
    
    def check_colisions(self, particles):
        for particle in particles:
            if particle == self:
                continue
            else:
                dist = self.distance(particle)
                if dist < self.radius + particle.radius:
                    self.resolve_colision(particle)
        

    def resolve_colision(self, particle):
        pass           
    
    def distance(self, particle):
        return(self.sqrt((self.pos[0] - particle.pos[0])**2 + 
                         (self.pos[1] - particle.pos[1])**2))
                
                




def random_particle(width, height, speed_cap):
    p = particle(pos = np.array([random.randint(0, width), 
                           random.randint(0, height)]),
                speed = np.random.rand(2) *speed_cap,
                color = np.random.randint(256, size = 3))
    return(p)       