#!/usr/bin/env python3
from numpy.random import choice

tiles = {
    'clear':                {'score': 80},
    'hole':                 {'score':  5},
    'conveyor-1':           {'score': 20},
    'conveyor-1-turnleft':  {'score': 10},
    'conveyor-1-turnright': {'score': 10},
    'conveyor-2':           {'score': 20},
    'conveyor-2-turnleft':  {'score': 10},
    'conveyor-2-turnright': {'score': 10},
    'laser-1':              {'score':  5},
    'laser-1-start':        {'score':  5},
    'wall-1':               {'score':  5},
    'wall-2':               {'score':  2},
    'wrench':               {'score':  4},
    'hammer-wrench':        {'score':  4},
}

def tileSrc(tileName):
    return "../tiles/tile-%s.png" % (tileName,)

#    'conveyor-1-threeway': 'tile-conveyor-1-threeway-1.png',
#    'conveyor-1-threeway-2': 'tile-conveyor-1-threeway-2.png'
#    'conveyor-2-threeway-1': 'tile-conveyor-2-threeway-1.png',
#    'conveyor-2-threeway-2': 'tile-conveyor-2-threeway-2.png',
#    'laser-1-overlay': 'tile-laser-1-overlay.png',
#    'laser-1-start-overlay': 'tile-laser-1-start-overlay.png',

clearTile = {
    'tileName': 'clear',
    'rotation': 0,
}

def randomTile(grid, x, y):
    legalTiles = tiles

    totalScore = 0
    for tileName, tile in legalTiles.items():
        totalScore += tile['score']

    choices = []
    probabilities = []
    for tileName, tile in legalTiles.items():
        choices.append(tileName)
        probabilities.append(1.0 * tile['score'] / totalScore)

    return {
        'tileName': choice(choices, p=probabilities),
        'rotation': choice([0, 90, 180, 270]),
    }

def neal(width=8, height=8):

    print("<html><body>")

    grid = [[clearTile] * width] * height
    for y in range(height):
        for x in range(width):
            tile = grid[y][x] = randomTile(grid, x, y)
            print("""    <div style="display: inline-block;
                                     width: 144px;
                                     height: 144px;
                                     transform: rotate({:d}deg);"><img src="{:s}"></div>"""
                  .format(tile['rotation'], tileSrc(tile['tileName'])))
        print("    <br>")

    print("</body></html>")

if __name__ == "__main__":
    neal()
