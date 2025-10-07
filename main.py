# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from asteroid import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)

    asteroid_field = AsteroidField()

    Shots = pygame.sprite.Group()
    Shot.containers = (updateable, drawable, Shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        updateable.update(dt)
        
        for asteroid in asteroids:
            for shot in Shots:
                if shot.is_colliding(asteroid):
                    asteroid.kill()
                    shot.kill()
                    
            if player.is_colliding(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()
        
        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(120) / 1000.0

    pygame.quit()
    
    




if __name__ == "__main__":
    main()
