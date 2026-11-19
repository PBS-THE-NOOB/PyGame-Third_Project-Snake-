import pygame
from pygame.math import Vector2
from settings.constants import SQUARE_WIDTH,SQUARE_NUMBER,GREEN

class SNAKE():
    def __init__(self,screen):
        self.screen = screen
        self.position = [Vector2(7,3),Vector2(6,3),Vector2(5,3)] #initial snake position
        self.right = Vector2(1,0)
        self.up = Vector2(0,-1)
        self.direction = self.right
        self.delete = Vector2(5,3)
        self.image_orentation_list = [pygame.transform.scale(pygame.image.load('Graphics/Snake/Body/snake-body-hori.png').convert_alpha(),(SQUARE_WIDTH,SQUARE_WIDTH))
                                      ,pygame.transform.scale(pygame.image.load('Graphics/Snake/Body/snake-body-vert.png').convert_alpha(),(SQUARE_WIDTH,SQUARE_WIDTH))]
        self.image_turning_dict = self.corner_images = {
    'left-up': pygame.transform.scale(pygame.image.load('Graphics/Snake/move/left-up.png').convert_alpha(),(SQUARE_WIDTH, SQUARE_WIDTH)),
    'right-up': pygame.transform.scale(pygame.image.load('Graphics/Snake/move/right-up.png').convert_alpha(),(SQUARE_WIDTH, SQUARE_WIDTH)),
    'up-left': pygame.transform.scale(pygame.image.load('Graphics/Snake/move/up-left.png').convert_alpha(),(SQUARE_WIDTH, SQUARE_WIDTH)),
    'up-right': (pygame.transform.scale(pygame.image.load('Graphics/Snake/move/up-right.png').convert_alpha(),(SQUARE_WIDTH, SQUARE_WIDTH))),
    'left-down':pygame.transform.flip(pygame.transform.scale(pygame.image.load('Graphics/Snake/move/left-up.png').convert_alpha(),(SQUARE_WIDTH, SQUARE_WIDTH)),True,True),
    'right-down': pygame.transform.flip(pygame.transform.scale(pygame.image.load('Graphics/Snake/move/right-up.png').convert_alpha(),(SQUARE_WIDTH, SQUARE_WIDTH)),True,True),
    'down-left': pygame.transform.flip(pygame.transform.scale(pygame.image.load('Graphics/Snake/move/up-left.png').convert_alpha(),(SQUARE_WIDTH, SQUARE_WIDTH)),True,True),
    'down-right': pygame.transform.flip(pygame.transform.scale(pygame.image.load('Graphics/Snake/move/up-right.png').convert_alpha(),(SQUARE_WIDTH, SQUARE_WIDTH)),True,True)
    }
        self.image = self.image_orentation_list[0]
        self.currnet_direction = Vector2(1,0)
        self.direction_before = self.currnet_direction

    def draw_snake(self):
        for num , i in enumerate(self.position) :
            rect = pygame.Rect(i.x * SQUARE_WIDTH,i.y * SQUARE_WIDTH,SQUARE_WIDTH,SQUARE_WIDTH)
            if self.assign_image(num , i) :
                self.screen.blit(self.image,rect)
            
            else : pygame.draw.rect(self.screen,GREEN,rect)
    
    def movement_handeling(self):
        keys =  pygame.key.get_pressed()
        if keys[pygame.K_a] and self.direction != self.right: 
            self.direction = -self.right
        elif keys[pygame.K_d] and self.direction != -self.right:
            self.direction = self.right
        elif keys[pygame.K_w] and self.direction != -self.up:
            self.direction = self.up
        elif keys[pygame.K_s] and self.direction != self.up:
            self.direction = -self.up
            

    def move_snake(self):
        self.movement_handeling()
        head = self.position[0] + self.direction
        self.position.insert(0,head) 
        self.delete = self.position.pop()
        self.assign_pos()

    def check_boundries(self) : 
        head = self.position[0]
        if head.x < 0 : return 'left'
        elif  head.x >= SQUARE_NUMBER : return 'right'
        if head.y < 0 : return 'up' 
        elif head.y >= SQUARE_NUMBER : return 'down'
        return None

    def assign_pos(self) :
        off_boundry  = self.check_boundries()
        if off_boundry == 'left' : 
            self.position[0].x += SQUARE_NUMBER
        elif off_boundry == 'right' :
            self.position[0].x -= SQUARE_NUMBER
        if off_boundry == 'up' : 
            self.position[0].y += SQUARE_NUMBER
        elif off_boundry == 'down' :
            self.position[0].y -= SQUARE_NUMBER

    def reset(self):
        self.position = [Vector2(7,3),Vector2(6,3),Vector2(5,3)]
        self.direction = self.right
        self.delete = Vector2(5,3)

    # def assign_image(self,num, i) :
    #     if num not in (0,len(self.position) - 1) :
    #         if  self.currnet_direction == self.direction_before :
    #             self.currnet_direction = self.position[num - 1] -  self.position [num]
    #             orentation = self.check_body_angle(self.currnet_direction)
    #             if orentation == 'horizontal' : 
    #                 self.image = self.image_orentation_list[0]
    #             else :  self.image = self.image_orentation_list[1]
    #             self.direction_before = self.position[num] -  self.position[num + 1]
    #             if len(self.position) <= num + 2 : self.direction_twice_before = self.position[num + 1] 
    #             else : self.direction_twice_before = self.position[num + 1] - self.position[num + 2]
    #             return True 
            
    #         elif self.currnet_direction != self.direction_before :
    #             movement = self.turning_body()
    #             if movement != 'no change' : self.image = self.image_turning_dict[movement]
    #             self.currnet_direction = self.position[num - 1] -  self.position [num]
    #             if len(self.position) <= num + 2 : self.direction_twice_before = self.position[num + 1] 
    #             else : self.direction_twice_before = self.position[num + 1] - self.position[num + 2]
    #             self.direction_before = self.position[num] -  self.position[num + 1]
    #             return True

    # def check_body_angle(self,segment : Vector2) :
    #     if segment.dot(self.right) == 0 : 
    #         return 'vertical'
    #     return 'horizontal'

    # def turning_body(self) :
    #     if self.check_body_angle(self.currnet_direction) == 'vertical' and self.check_body_angle(self.direction_before) == 'horizontal': 
    #         if self.currnet_direction . y < self.direction_before . y  :  
    #             # moving up
    #             if self.direction_before . x > self.direction_twice_before . x :
    #                 #moving right
    #                 return 'right-up'
    #             elif  self.direction_before . x < self.direction_twice_before . x  : 
    #                 return 'left-up'
    #             else :
    #                 return 'no change'
    #         else : 
    #             # moving down
    #             if self.direction_before . x < self.direction_twice_before . x :
    #                 #moving left
    #                 return 'left-down'
    #             elif self.direction_before . x > self.direction_twice_before . x :
    #                 return 'right-down'
    #             else : 
    #                 return 'no change'
    #     return 'no change'