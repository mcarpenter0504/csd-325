"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Tags: short, bext, simulation"""

# Modified even more by Scott Anderson, Madilyn Carpenter, Kimberly Orozco. We added a lake in the middle :D
# Module 6 Assignment: Forest Fire Simulation: Program and Revised Flowchart
# July 3rd, 2025 

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # New constant for water

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5

# Coordinates for lake area 
LAKE_START_X = 18
LAKE_END_X = 46
LAKE_START_Y = 9
LAKE_END_Y = 14


def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        nextForest = {'width': forest['width'], 
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue

                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER  # Water won't ever change, like it will stay in the same spot
                elif ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = (x + ix, y + iy)
                            if forest.get(neighbor) == TREE:
                                if forest.get(neighbor) != WATER:  # No fire through water
                                    nextForest[neighbor] = FIRE
                    nextForest[(x, y)] = EMPTY
                else:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure, with lake added."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if LAKE_START_X <= x <= LAKE_END_X and LAKE_START_Y <= y <= LAKE_END_Y:
                forest[(x, y)] = WATER  # Place water
            elif (random.random() <= INITIAL_TREE_DENSITY):
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            tile = forest[(x, y)] #put it to tile so then we dont have to write forest[(x, y)] over and over ;3;
            if tile == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif tile == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif tile == WATER:
                bext.fg('blue')
                print(WATER, end='')
            elif tile == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()