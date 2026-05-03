import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from Player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
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
        
        pygame.display.flip()
    
    


if __name__ == "__main__":
    main()
