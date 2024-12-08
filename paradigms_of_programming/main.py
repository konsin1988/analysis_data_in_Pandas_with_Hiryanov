import pygame
from pygame.locals import *
from math import *

RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (0, 0, 255)
CYAN_COLOR = (0, 255, 255)
BROWN_COLOR = (100, 100, 0)
BLACK_COLOR = (0, 0, 0)

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Draw me a house!')

def draw_image(window):
    """
            Draw image with hause
            window -- PyGame library object
    """
    width, height = window.get_size()
    house_x, house_y = width // 2, height * 2 // 3
    house_width = width // 3
    house_height = 4 * house_width // 3

    draw_background(window, width, height)
    draw_house(window, house_x, house_y, house_width, house_height)

def draw_background(window, width, height):
    pass

def draw_house(window, house_x, house_y, house_width, house_height):
    pass


draw_image(window)

pygame.display.update()
going_to_quit = False
while not going_to_quit:
    for event in pygame.event.get():
        if(event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE):
            going_to_quit = True
pygame.quit()
