import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

def main():
    print("Starting game...")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


    while True:
        # Event to allow exiting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # Full screen black with refresh
        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # Limit Framerate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
