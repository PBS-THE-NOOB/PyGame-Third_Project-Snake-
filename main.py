import pygame,sys
from settings.constants import SCREEN_SIZE,CHARCOAL
from Game.fruit import FRUIT
from Game.snake import SNAKE


pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
pygame.display.set_caption('Snake_2D')
clock = pygame.time.Clock()
fruit = FRUIT(screen)
run = True

def game_quit():
    pygame.quit()
    sys.exit()

while run:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False 

    screen.fill(CHARCOAL)

    # fruit 
    fruit.draw_fruit()

    pygame.display.update()
    clock.tick(60)

game_quit()

    