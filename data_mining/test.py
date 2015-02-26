# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 23:37:53 2014

@author: sophie

Generating all dem maze solvers from scratch!
"""

import pygame
from pygame.locals import *


class Cell(object):
    def __init__(self, pos, size):
        self.rect = pygame.Rect(pos[0], pos[1], size, size)
        self.x = pos[0]
        self.y = pos[1]


class Model:
    """implements our maze solving alg"""
    def __init__ (self, screen_size):
        self.cells = []
        self.screen_size = screen_size

        self.grid = 10 #grid height

        self.grid_size = self.screen_size / 10
        self.construct_grid()
#        self.construct_environment()


    def construct_grid(self):
        grid_size = self.grid_size
        x = y = 0
        while x < self.screen_size:
            while y < self.screen_size:
                if x == (self.screen_size - grid_size) and y == (self.screen_size - grid_size):
                    self.end_rect = pygame.Rect(x, y, grid_size, grid_size)
                    return
                self.cells.append(Cell((x, y), grid_size))
                y += grid_size
            x += grid_size
            y = 0

class PyGameWindowView:
    """draws our pretty maze"""
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(255,255,255))
#        pygame.draw.rect(self.screen, pygame.Color(109, 109, 109), self.model.player.rect) #Player
        for cell in self.model.cells: #Draws each wall block
            pygame.draw.rect(screen, pygame.Color(0, 0, 0), cell.rect, 2) #only drawing the outline of the square
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    size = (500,500)
    screen = pygame.display.set_mode(size)
    model = AStar_Model(500)
    view = PyGameWindowView(model, screen)

    running = True
    book_similarities = check_book_similarity()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        view.draw()
    pygame.quit()