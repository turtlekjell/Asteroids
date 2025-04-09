import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot 

# 🔁 These need to be defined BEFORE any .containers assignments
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()


# ✅ Now safe to assign containers
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Track frame rate
    dt = 0  # Delta time

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exits the game loop

        screen.fill((0, 0, 0))  # RGB black
        
        #player.update(dt)
        #player.draw(screen)

        updatable.update(dt)
        
        
        for obj in drawable:
            obj.draw(screen)

        # Check for collisions after updating positions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return

        # Collision: player vs asteroid
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return

        # Collision: shots vs asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
                    break  # optional: skip checking other asteroids for this shot



        pygame.display.flip()

        # Tick the clock and get the time since last frame
        dt = clock.tick(60) / 1000  # Convert ms to seconds

if __name__ == "__main__":
    main()



