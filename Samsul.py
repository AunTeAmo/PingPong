import pygame, sys
import random


def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def recenter():
    if ball.colliderect(wall_right) or ball.colliderect(wall_left):
        ball_restart()


       

def player_animation():
    player.y += player_speed
    if player.top <= 0:
       player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height 

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= screen_height:
            opponent.bottom = screen_height
def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Samsul')

ball = pygame.Rect(screen_width /2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70,10,140)
wall_right = pygame.Rect(screen_width - 5, 0, 5, screen_height)
wall_left = pygame.Rect(0, 0, 5, screen_height)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 255, 255)

ball_speed_x = 2 * random.choice((1, -1))
ball_speed_y = 2 * random.choice((1, -1))
player_speed = 3
opponent_speed = 100



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:          
            if event.key == pygame.K_w:
                player_speed -= 3
            if event.key == pygame.K_s:
                player_speed += 3
        

            



    ball.x += ball_speed_x
    ball.y += ball_speed_y

    ball_animation()
    player_animation()
    opponent_ai()
    recenter()
    
       

    
    screen.fill(bg_color)
    pygame.draw.rect(screen, blue, player)
    pygame.draw.rect(screen, red, opponent)
    pygame.draw.ellipse(screen, yellow, ball)
    pygame.draw.rect(screen, light_grey, wall_left)
    pygame.draw.rect(screen, light_grey, wall_right)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))    
    pygame.display.flip()
    clock.tick(60)

   