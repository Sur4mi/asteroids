import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.shot_radius = SHOT_RADIUS
        self.velocity = velocity

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt
        pass
