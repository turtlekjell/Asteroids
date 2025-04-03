import pygame
from constants import *
from player import Player



updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

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


        pygame.display.flip()

        # Tick the clock and get the time since last frame
        dt = clock.tick(60) / 1000  # Convert ms to seconds

if __name__ == "__main__":
    main()



