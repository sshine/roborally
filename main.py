#!/usr/bin/env python3

import pygame
import sys

# Set up the display
WIDTH, HEIGHT = 640, 640
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tiles
TILES = {
    'clear': 'tiles/tile-clear.png',
    'wall-side': 'tiles/tile-wall-1.png',
    'wall-corner': 'tiles/tile-wall-2.png',
}

def load_tile_images(tiles_dict, square_size=None):
    loaded_tiles = {}

    for tile_name, file_path in tiles_dict.items():
        try:
            # Load the image
            image = pygame.image.load(file_path)

            # Scale if square_size is provided
            if square_size is not None:
                image = pygame.transform.scale(image, (square_size, square_size))

            # Convert for better performance
            image = image.convert_alpha()

            # Add to our dictionary
            loaded_tiles[tile_name] = image

        except pygame.error as e:
            print(f"Error loading image {file_path}: {e}")
            # Add a placeholder or None for failed loads
            loaded_tiles[tile_name] = None

    return loaded_tiles

def draw_roborally_board(screen, tiles):
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            pix_x = x * SQUARE_SIZE
            pix_y = y * SQUARE_SIZE
            pix_pos = (pix_x, pix_y)
            # screen.blit(tiles['clear'], pix_pos)
            if is_corner(x, y):
                draw_roborally_tile(screen, pix_pos, tiles['wall-corner'], corner_wall_angle(x, y))
            elif is_side(x, y):
                draw_roborally_tile(screen, pix_pos, tiles['wall-side'], side_wall_angle(x, y))
            else:
                draw_roborally_tile(screen, pix_pos, tiles['clear'])

def is_corner(x, y):
    a = (x == 0 or x == BOARD_SIZE-1)
    b = (y == 0 or y == BOARD_SIZE-1)
    return (a and b)

def is_side(x, y):
    return (x == 0 or y == 0 or x == BOARD_SIZE-1 or y == BOARD_SIZE-1)

def corner_wall_angle(x, y):
    if x == 0 and y == 0:
        return 90
    if x == BOARD_SIZE-1 and y == 0:
        return 0
    if x == 0 and y == BOARD_SIZE-1:
        return 180
    if x == BOARD_SIZE-1 and y == BOARD_SIZE-1:
        return 270
    return 0

def side_wall_angle(x, y):
    if y == BOARD_SIZE-1:
        return 0
    if y == 0:
        return 180
    if x == 0:
        return 270
    if x == BOARD_SIZE-1:
        return 90 
    return 0

def draw_roborally_tile(screen, pix_pos, tile, degrees=0):
    pix_x, pix_y = pix_pos

    if degrees != 0:
        rotated_tile = pygame.transform.rotate(tile, degrees)

        # Get the rect of the rotated image to ensure it's centered properly
        rect = rotated_tile.get_rect(center=tile.get_rect(topleft=pix_pos).center)

        screen.blit(rotated_tile, rect.topleft)
    else:
        screen.blit(tile, pix_pos)

def draw_chessboard():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Determine color of square
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK

            # Draw square
            pygame.draw.rect(
                screen, 
                color, 
                (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            )

# Main game loop
def main(screen, tiles):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Draw the chessboard
        # draw_chessboard()
        draw_roborally_board(screen, tiles)

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    tiles = load_tile_images(TILES, SQUARE_SIZE)
    pygame.display.set_caption('RoboRally')
    main(screen, tiles)
