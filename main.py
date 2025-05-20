import pygame
from constants import *
from player import Player

def main():
    print("Starting game...")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        # Event to allow exiting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Full screen black with refresh
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        
        player.update(dt)
        # Limit Framerate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
