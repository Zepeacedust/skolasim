import random
import math


def perlin_noise(height, width):
    grid = []
    for y in range(height):
        current_line = []
        for x in range(width):
            current_line.append(random.uniform(0, math.tau))
        grid.append(current_line)
    noisemap = []
    for x in range(height):
        current_line = []
        for y in range(width):
            current_line.append(0)
        noisemap.append(current_line)
    for y in range(height):
        for x in range(width):
            current_angle = grid[y][x]
            x_displacement = math.sin((grid[y])[x])
            y_displacement = math.cos((grid[height - 1])[width - 1])
            x_maps_to = round(random.uniform(1, 3) * x_displacement + x) % width
            y_maps_to = round(random.uniform(1, 3) * y_displacement + y) % height
            noisemap[y_maps_to][x_maps_to] += 1
    return noisemap


def scan_neighborhood(self, y, x):# for use with cellular automata
    population = 0
    for Y in (y - 1, y, y + 1):
        for X in (x - 1, x, x + 1):
            if self[Y % len(self)][X % len(self)] == 1 and not (X == x and Y == y):
                population += 1
    return population# returnar hversu mörg cells eru í 3*3 area centred á tile


def cellular_automata(height, width):
    grid = []
    for Y in range(height):
        current_line = []
        for X in range(width):
            current_line.append(random.randint(0, 1))# gera height*width grid af 1 eða 0
        grid.append(current_line)
    for length in range(1):
        newgrid = []
        for x in range(height):
            current_line = []
            for y in range(width):
                current_line.append(0)
            newgrid.append(current_line)
        for y in range(height):
            for x in range(width):
                neighbors = scan_neighborhood(grid, y, x)
                if neighbors == 4:
                    newgrid[y][x] = 1
                elif not neighbors == 5:
                    newgrid[y][x] = 0
        grid = newgrid
    return grid


def mapgen(height, width):
    map = []
    for y in range(height):
        curlist = []
        for x in range(width):
            1+1#placeholder
