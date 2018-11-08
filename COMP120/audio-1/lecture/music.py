import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_mode((250, 250), 0, 32)

pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1, 0.0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()