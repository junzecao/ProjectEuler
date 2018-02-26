#!/bin/python

import sys


grid = []

def add_grid(grid):
    new_grid = []
    for i in xrange(20):
        new_grid.append([0,0,0] + grid[i] + [0,0,0])
    for i in xrange(3):
        new_grid.append([0] * 26)
    return new_grid

def find_max(new_grid):
    max_ = 0
    for i in xrange(0,20):
        for j in xrange(3,23):
            horizontal = new_grid[i][j]*new_grid[i+1][j]*new_grid[i+2][j]*new_grid[i+3][j]
            vertical = new_grid[i][j]*new_grid[i][j+1]*new_grid[i][j+2]*new_grid[i][j+3]
            diagonal1 = new_grid[i][j]*new_grid[i+1][j+1]*new_grid[i+2][j+2]*new_grid[i+3][j+3]
            diagonal2 = new_grid[i][j]*new_grid[i+1][j-1]*new_grid[i+2][j-2]*new_grid[i+3][j-3]
            if max(horizontal,vertical,diagonal1,diagonal2)>max_:
                max_ = max(horizontal,vertical,diagonal1,diagonal2)
    return max_

for grid_i in xrange(20):
    grid_temp = map(int,raw_input().strip().split(' '))
    grid.append(grid_temp)

new_grid = add_grid(grid)
print find_max(new_grid)
