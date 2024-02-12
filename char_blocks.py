#!/usr/bin/env python3
#
# char_blocks.py

import random

CHARACTERS_AND_COLORS = [
    {"char": "⠿", "fg": "\033[38;5;82m", "bg": "\033[48;5;235m"},
    {"char": "⡿", "fg": "\033[38;5;136m", "bg": "\033[48;5;202m"},
    {"char": "⢿", "fg": "\033[38;5;196m", "bg": "\033[48;5;130m"},
    {"char": "⣧", "fg": "\033[38;5;221m", "bg": "\033[48;5;100m"},
    {"char": "⣏", "fg": "\033[38;5;127m", "bg": "\033[48;5;119m"},
    {"char": "⢯", "fg": "\033[38;5;171m", "bg": "\033[48;5;154m"},
    {"char": "⣟", "fg": "\033[38;5;203m", "bg": "\033[48;5;160m"},
    {"char": "⢽", "fg": "\033[38;5;149m", "bg": "\033[48;5;178m"},
    {"char": "⣷", "fg": "\033[38;5;210m", "bg": "\033[48;5;142m"},
    {"char": "⣌", "fg": "\033[38;5;125m", "bg": "\033[48;5;193m"},
    {"char": "⢿", "fg": "\033[38;5;196m", "bg": "\033[48;5;130m"},
    {"char": "⣿", "fg": "\033[38;5;244m", "bg": "\033[48;5;115m"},
    {"char": "⣍", "fg": "\033[38;5;241m", "bg": "\033[48;5;123m"},
    {"char": "⣛", "fg": "\033[38;5;227m", "bg": "\033[48;5;138m"},
    {"char": "⣝", "fg": "\033[38;5;218m", "bg": "\033[48;5;158m"},
    {"char": "⣞", "fg": "\033[38;5;209m", "bg": "\033[48;5;173m"},
    {"char": "⣟", "fg": "\033[38;5;203m", "bg": "\033[48;5;160m"},
    {"char": "⣷", "fg": "\033[38;5;210m", "bg": "\033[48;5;142m"},
    {"char": "⣻", "fg": "\033[38;5;187m", "bg": "\033[48;5;182m"},
    {"char": "⣿", "fg": "\033[38;5;244m", "bg": "\033[48;5;115m"},
    {"char": "⣦", "fg": "\033[38;5;236m", "bg": "\033[48;5;120m"},
    {"char": "⣄", "fg": "\033[38;5;240m", "bg": "\033[48;5;128m"}
]


def map_grayscale_to_blocks(image):
    width, height = image.size
    block_mapping = []

    for y in range(height):
        row = []
        for x in range(width):
            grayscale = image.getpixel((x, y))
            char_and_color = random.choice(CHARACTERS_AND_COLORS)
            row.append({"char": char_and_color["char"], "color": char_and_color["fg"] + chr(27) + "[48;5;" + str(grayscale) + "m" + " " + char_and_color["bg"]})
        block_mapping.append(row)

    return block_mapping

def map_blocks_to_console(block_mapping, width, height, cell_width, cell_height):
    for y in range(height):
        for x in range(width):
            if x % (cell_width) == 0 and y % (cell_height) == 0:
                sys.stdout.write(block_mapping[y][x]["color"] + block_mapping[y][x]["char"])
                sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()

def map_blocks_to_console(block_mapping, width, height, cell_width, cell_height):
    for y in range(height):
        for x in range(width):
            if x % (cell_width) == 0 and y % (cell_height) == 0:
                sys.stdout.write(block_mapping[y][x]["color"] + block_mapping[y][x]["char"])
                sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()

if __name__ == "__main__":
    image = Image.open("your_image.png").convert("L")

    cell_width = 5
    cell_height = 7

    block_mapping = map_grayscale_to_blocks(image)
    map_blocks_to_console(block_mapping, image.width, image.height, cell_width, cell_height)


