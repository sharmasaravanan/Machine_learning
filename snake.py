import random
import sys
import time

import pygame

check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initilization error...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame successfully started!")

# window
surface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game!!!')

# colour
r = pygame.Color(255, 0, 0)  # game over
g = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
w = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # food

# FPS
fpsc0ntrol = pygame.time.Clock()

# variables
snakepos = [100, 50]
snakebody = [[100, 50], [90, 50], [80, 50]]
foodpos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodspawn = True

direction = 'RIGHT'
changeto = direction
score = 0


def gameover():
    myfont = pygame.font.SysFont('monaco', 72)
    gosurf = myfont.render('Game Over!!!', True, r)
    gorect = gosurf.get_rect()
    gorect.midtop = (360, 15)
    surface.blit(gosurf, gorect)
    myfont1 = pygame.font.SysFont('arial', 20)
    gosurf1 = myfont1.render('Created by Sharma S', True, black)
    gorect1 = gosurf1.get_rect()
    gorect1.midtop = (640, 435)
    surface.blit(gosurf1, gorect1)
    scoreboard(2)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


def scoreboard(choice=1):
    sfont = pygame.font.SysFont('monaco', 34)
    ssurf = sfont.render('Score : {0}!!'.format(score), True, black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (80, 10)
    else:
        srect.midtop = (360, 120)
    surface.blit(ssurf, srect)
    # pygame.display.flip()


# main game
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    # moving
    if direction == 'RIGHT':
        snakepos[0] += 10
    if direction == 'LEFT':
        snakepos[0] -= 10
    if direction == 'UP':
        snakepos[1] -= 10
    if direction == 'DOWN':
        snakepos[1] += 10

    # body

    snakebody.insert(0, list(snakepos))
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
        score += 1
        foodspawn = False
    else:
        snakebody.pop()

    if foodspawn == False:
        foodpos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodspawn = True

    surface.fill(w)
    for pos in snakebody:
        pygame.draw.rect(surface, g, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(surface, brown, pygame.Rect(foodpos[0], foodpos[1], 10, 10))

    if snakepos[0] > 710 or snakepos[0] < 0:
        gameover()
    if snakepos[1] > 450 or snakepos[1] < 0:
        gameover()

    for block in snakebody[1:]:
        if snakepos[0] == block[0] and snakepos[1] == block[1]:
            gameover()

    scoreboard()
    pygame.display.flip()
    fpsc0ntrol.tick(10)
