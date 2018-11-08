import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_mode((250, 250), 0, 32)
sound = pygame.mixer.Sound('sample.wav')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == ord('p'):
                sound.play()