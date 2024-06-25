# import pygame
# from pygame.locals import *
# import time
# import random

# pygame.init()

# red = (171, 28, 28)
# blue = (24, 109, 152)
# green = (22, 101, 17)
# yellow = (255, 255, 0)


# width = 600
# height = 400
# window = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Snake Game")

# time.sleep(2)

# snake = 10
# snakespeed = 15

# clock = pygame.time.Clock()

# fontstyle = pygame.font.SysFont('arialblack',26)
# scorefont =  pygame.font.SysFont('segoemdl2assets',30)



# def user_score(score):
#     number = scorefont.render("Score:",score ,True,red )
#     window.blit(number[0,0])

# def game_snake(snake,snake_length_list):
#     for x in snake_length_list:
#         pygame.draw.rect(window,yellow,[x[0], x[1], snake])
#     pass

# def message(msg):
#     msg = fontstyle.render(msg,True,red)
#     window.blit(msg[width/6, height/3])


# def game_loop():
#     gameOver = False
#     gameClose = True

#     x1 = width/2
#     y1 = height/2

#     x1_change = 0
#     y1_change = 0

#     snake_length_list = []
#     snake_length = 1
    
#     foodx = round(random.randrange(0,width-snake)/10.0)*10.0    
#     foody = round(random.randrange(0,height-snake)/10.0)*10.0    

#     while gameClose == True:
#         window.fill(blue)
#         message("You lost, Press Q to play again and X to Quit")

#         user_score(snake_length-1)
#         pygame.display.update()

#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_q:
#                     gameOver = True
#                     gameClose = True

#                 if event.key == pygame.K_p:
#                     game_loop()

        
#         for event in pygame.event.get():           
#             if event.type == pygame.KEYDOWN:
#                 if event.key == K_LEFT:
#                     x1_change= -snake
#                     y1_change= 0
                    
#                 if event.key == K_RIGHT:
#                     x1_change= snake
#                     y1_change= 0

#                 if event.key == K_UP:
#                     x1_change= 0
#                     y1_change= -snake

#                 if event.key == K_DOWN:
#                     x1_change= 0
#                     y1_change= snake


#             if x1 > width or x1 <0  or y1 > height or y1<0:
#                 gameClose = True

#             x1 += x1_change
#             y1 += y1_change
#             window.fill(green)
#             pygame.draw.rect(window,yellow,[foodx,foody,snake,snake])

#             snake_size = []
#             snake_size.append(x1)
#             snake_size.append(y1)

#             snake_length_list.append(snake_size)
#             if len(snake_length_list) > snake_length:
#                 del snake_length_list[0]

#             game_snake(snake,snake_length_list)
#             user_score(snake_length - 1)

#             pygame.display.update()

#             if x1 == foodx and y1 == foody:
#                 foodx = round(random.randrange(0,width-snake)/10.0)*10.0    
#                 foody = round(random.randrange(0,height-snake)/10.0)*10.0 
#                 snake_length +=1

#             clock.tick(snakespeed)

#     pygame.quit()
#     quit

# game_loop()












import pygame
from pygame.locals import *
import time
import random

pygame.init()

# Define colors
red = (171, 28, 28)
blue = (24, 109, 152)
green = (22, 101, 17)
yellow = (255, 255, 0)

# Set up the display
width = 600
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Snake settings
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

# Font settings
font_style = pygame.font.SysFont('arialblack', 26)
score_font = pygame.font.SysFont('segoemdl2assets', 30)

# Function to display the score
def user_score(score):
    value = score_font.render(f"Score: {score}", True, red)
    window.blit(value, [0, 0])

# Function to draw the snake
def game_snake(snake_block, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, yellow, [x[0], x[1], snake_block, snake_block])

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(blue)
            message("You lost, Press Q to Quit or C to Play Again", red)
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(green)
        pygame.draw.rect(window, yellow, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_length_list.append(snake_head)
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        for x in snake_length_list[:-1]:
            if x == snake_head:
                game_close = True

        game_snake(snake_block, snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()


