import sys, pygame
import numpy as np
from random import random
from particle import particle, random_particle 

pygame.init()

size = width, height = 1000, 1000
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

particles = []
for i in range(100):
    particles.append(random_particle(width, height, 10))

particles = set(particles)

while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    surface = pygame.Surface((1000,1000))
    for p in particles:
        pygame.draw.circle(surface, p.color, p.pos, p.radius)
        p.update_pos()
        p.check_colisions_walls(width, height)
    
    screen.blit(surface, (0, 0))
    pygame.display.flip()