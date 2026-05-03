import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots,updatable,drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable,)
    
    asteroid_field = AsteroidField()
    
    
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True :
        log_state()
        amount_time = clock.tick(60)
        dt = amount_time/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        screen.fill("black")
        for dr in drawable:
            dr.draw(screen)
        for astroid in asteroids:
            if player.collides_with(astroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for astroid in asteroids:
            for shot in shots:
                if astroid.collides_with(shot):
                    log_event("asteroid_shot")
                    astroid.kill()
                    shot.kill()
        
        pygame.display.flip()
    
    


if __name__ == "__main__":
    main()
