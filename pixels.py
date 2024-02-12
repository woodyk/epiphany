#!/usr/bin/env python3
#
# pixels.py

import sys
import math
import pygame
from pygame.locals import *

PIXEL_SIZE = 2
window_size = (800 // PIEXEL_SIZE, 600 // PIEXEL_SIZE)
screen = pygame.display.set_mode(window_size)

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

def center_text(surface, msg, font, anchor=(0.5, 0.5)):
    rect = font.render(msg, True, (255, 255, 255)).get_rect()
    rect.center = surface.get_rect().center
    surface.blit(font.render(msg, True, (255, 255, 255)), rect)

def distance(pos1, pos2):
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    return math.sqrt(dx * dx + dy * dy)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    mouse_position = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))

    radius = min(100, distance(mouse_position, (400, 300)))
    pygame.draw.circle(screen, (255, 255, 255), (400, 300), radius)

    center_text(screen, f'Distance: {radius:.2f}', pygame.font.SysFont('Consolas', 18))

    pygame.display.update()

pygame.quit()
sys.exit()
