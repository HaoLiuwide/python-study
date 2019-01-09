import pygame
import sys
import random
from pygame.locals import *

# food’s  color
redColor = pygame.Color(255, 0, 0)
# snake’s  color
whiteColor = pygame.Color(255, 255, 255)
# background’s  color
blackColor = pygame.Color(0, 0, 0)
# game over


def gameover():
    pygame.quit()
    sys.exit()


class Snake:
    def __init__(self):
        self.snakearray = [[int(random.randrange(1, 50)*20), int(random.randrange(1, 30)*20)]]
        self.direction = 'right'
        self.keyvalue = ''
        self.food_position = [int(random.randrange(1, 50)*20), int(random.randrange(1, 30)*20)]
        self.eaten_flag = '1'

    def move(self):
        self.eaten_flag = 1
        if self.direction == 'right':
            if self.snakearray[0][0] == 980:
                pos = [0, self.snakearray[0][1]]
            else:
                pos = [self.snakearray[0][0] + 20, self.snakearray[0][1]]
        if self.direction == 'left':
            if self.snakearray[0][0] == 0:
                pos = [980, self.snakearray[0][1]]
            else:
                pos = [self.snakearray[0][0] - 20, self.snakearray[0][1]]
        if self.direction == 'up':
            if self.snakearray[0][1] == 0:
                pos = [self.snakearray[0][0], 580]
            else:
                pos = [self.snakearray[0][0], self.snakearray[0][1] - 20]
        if self.direction == 'down':
            if self.snakearray[0][1] == 580:
                pos = [self.snakearray[0][0], 0]
            else:
                pos = [self.snakearray[0][0], self.snakearray[0][1] + 20]
        self.snakearray.insert(0, list(pos))
        if one.food_position[0] == one.snakearray[0][0] and one.food_position[1] == one.snakearray[0][1]:
            self.eaten_flag = 0
            self.food()
        else:
            self.snakearray.pop()

    def food(self):
        x = random.randrange(1, 50)
        y = random.randrange(1, 30)
        self.food_position = [int(x*20), int(y*20)]

    def keyboard_monitor(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    gameover()
                elif event.key == K_RIGHT:
                    self.keyvalue = 'right'
                elif event.key == K_LEFT:
                    self.keyvalue = 'left'
                elif event.key == K_UP:
                    self.keyvalue = 'up'
                elif event.key == K_DOWN:
                    self.keyvalue = 'down'
        if self.keyvalue == 'right' and not self.direction == 'left':
            self.direction = self.keyvalue
        if self.keyvalue == 'left' and not self.direction == 'right':
            self.direction = self.keyvalue
        if self.keyvalue == 'up' and not self.direction == 'down':
            self.direction = self.keyvalue
        if self.keyvalue == 'down' and not self.direction == 'up':
            self.direction = self.keyvalue


pygame.init()
playsurface = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('The Snake')
fps_clock = pygame.time.Clock()
one = Snake()
while True:
    one.keyboard_monitor()
    playsurface.fill(blackColor)
    for position in one.snakearray:
        pygame.draw.rect(playsurface, whiteColor, Rect(position[0], position[1], 20, 20))
        pygame.draw.rect(playsurface, redColor, Rect(one.food_position[0], one.food_position[1], 20, 20))
    one.move()
    pygame.display.flip()
    fps_clock.tick(10*len(one.snakearray))


# def gameover():
#     pygame.quit()
#     sys.exit()
#
#
# def main():
#     pygame.init()
#     fpsclock = pygame.time.Clock()
#     playsurface = pygame.display.set_mode((640, 630))
#     pygame.display.set_caption('The snake')
#     snakeposition = [100, 100]
#     snakebody = [[100, 100], [80, 100], [60, 100]]
#     targetposition = [300, 300]
#     targetflag = 1
#     direction = 'right'
#     changeddirection = direction
#     while True:
#
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 gameover()
#             elif event.type == KEYDOWN:
#                 if event.key == K_RIGHT:
#                     changeddirection = 'right'
#                 if event.key == K_LEFT:
#                     changeddirection = 'left'
#                 if event.key == K_UP:
#                     changeddirection = 'up'
#                 if event.key == K_DOWN:
#                     changeddirection = 'down'
#         direction = changeddirection
#         # if changeddirection == 'left' and not direction == 'right':
#         #     direction == changeddirection
#         # if changeddirection == 'right' and not direction == 'left':
#         #     direction == changeddirection
#         # if changeddirection == 'up' and not direction == 'down':
#         #     direction == changeddirection
#         # if changeddirection == 'down' and not direction == 'up':
#         #     direction == changeddirection
#         if direction == 'right':
#             snakeposition[0] += 20
#         if direction == 'left':
#             snakeposition[0] -= 20
#         if direction == 'up':
#             snakeposition[1] -= 20
#         if direction == 'down':
#             snakeposition[1] += 20
#         snakebody.insert(0, list(snakeposition))
#         if snakeposition[0] == targetposition[0] and snakeposition[1] == targetposition[1]:
#             targetflag = 0
#         else:
#             snakebody.pop()
#         if targetflag == 0:
#             x = random.randrange(1, 32)
#             y = random.randrange(1, 24)
#             targetposition = [int(x*20), int(y*20)]
#         playsurface.fill(blackColor)
#         for position in snakebody:
#             pygame.draw.rect(playsurface, white, Rect(position[0], position[1], 20, 20))
#             pygame.draw.rect(playsurface, redColor, Rect(targetposition[0], targetposition[1], 20, 20))
#         pygame.display.flip()
#         if snakeposition[0] > 620 or snakeposition[0] < 0:
#             gameover()
#         elif snakeposition[1] > 460 or snakeposition[1] < 0:
#             gameover()
#         fpsclock.tick(5)
#
#
# if __name__ == '__main__':
#     main()
