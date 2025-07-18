# this allows us to use code from 
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # create two groups and set both groups as containers for player 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x = SCREEN_WIDTH/2, y= SCREEN_HEIGHT/2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable, )
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        updatable.update(dt)
        # collision check for player hitting asteroids
        for a in asteroids:
            if player.collision_check(a) == True:
                print("Game over!")
                sys.exit(1)
        # add collision check for bullets hitting asteroids
            for s in shots:
                if s.collision_check(a) == True:
                    s.kill()
                    a.split()
        for r in drawable:
            r.draw(screen)
        pygame.display.flip()

        # add clock tick method - pause the loop every 1/60th second
        # return .tick as seconds to dt variable
        dt = clock.tick(60) / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
