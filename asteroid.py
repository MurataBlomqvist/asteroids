import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # if the smallest type of asteroid was shot
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # compute new angle the asteroids will split out in
            new_angle = random.uniform(20, 50)
            first_vector = pygame.math.Vector2.rotate(self.velocity, new_angle)
            second_vector = pygame.math.Vector2.rotate(self.velocity, -new_angle)
            # new radius for the asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # first asteroind splitting
            split1_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            split1_asteroid.velocity += first_vector * 1.2
            # second asteroid splitting
            split2_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            split2_asteroid.velocity += second_vector * 1.2