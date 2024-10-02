import pygame  # type: ignore
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.rect = pygame.Rect(x - SHOT_RADIUS, y - SHOT_RADIUS, SHOT_RADIUS * 2, SHOT_RADIUS * 2)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position