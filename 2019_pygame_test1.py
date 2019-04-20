import pygame, sys
from pygame.locals import * #skip the modulename. portion and simply use functionname()
p = pygame
p.init()
dis = p.display.set_mode((400, 400))
p.display.set_caption("hello world!")
while True:
    p.display.update()

