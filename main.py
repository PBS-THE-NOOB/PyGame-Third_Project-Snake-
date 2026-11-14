import pygame,sys
from settings.constants import SCREEN_SIZE,CHARCOAL
from Game.fruit import FRUIT
from Game.snake import SNAKE


pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
pygame.display.set_caption('Snake_2D')
clock = pygame.time.Clock()

fruit = FRUIT(screen)
snake = SNAKE(screen)
snake_move = pygame.USEREVENT + 1 
pygame.time.set_timer(snake_move,250)
run = True

def game_quit():
    pygame.quit()
    sys.exit()

while run:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False 
        if event.type == snake_move :
            snake.move_snake()

    screen.fill(CHARCOAL)

    # fruit 
    fruit.draw_fruit()

    #snake 
    snake.draw_snake()
    snake.update()

    pygame.display.update()
    clock.tick(60)

game_quit()

    