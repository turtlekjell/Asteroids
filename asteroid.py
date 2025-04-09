import pygame
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        from constants import ASTEROID_MIN_RADIUS  # Avoid circular imports

        self.kill()  # Always remove the current asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Small asteroid—just disappear

        # Calculate new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        # Create two new velocity vectors
        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2

        # Spawn the two smaller asteroids
        Asteroid(self.position.x, self.position.y, new_radius).velocity = v1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = v2

