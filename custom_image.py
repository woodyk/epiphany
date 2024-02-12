#!/usr/bin/env python3
#
# custom_image.py

import sys
import os
import json
import yaml
from PIL import Image

config = """width: 32
height: 32
palette:
  - r: 255
    g: 0
    b: 0
    label: red
  - r: 0
    g: 255
    b: 0
    label: green
  - r: 0
    g: 0
    b: 255
    label: blue
"""

header = '{"char": "#", "fg": "\033[38;5;16m", "bg": "\033[48;5;235m"}'

def read_epiphany_image(file_name):
    magic_number = b'EPIP'
    fmt = '<4siib'
    max_colors = 0

    with open(file_name, 'rb') as fd:
        buf = fd.read(4)
        if buf != magic_number:
            raise ValueError('File does not conform to EPIP format')

        buf = fd.read(8)
        width, height = struct.unpack(fmt, buf)

        buf = fd.read(1)
        max_colors = struct.unpack(fmt, buf)[0]

        pixel_array = []
        while True:
            buf = fd.read(3)
            if not buf:
                break
            pixel_array.append(struct.unpack(fmt, buf))

    return np.array(pixel_array).reshape((height, width, 3))

def save_custom_image(filename, image):
    width, height = image.size
    img_data = []

    for y in range(height):
        row = []
        for x in range(width):
            grayscale = image.getpixel((x, y))
            char_and_color = random.choice(CHARACTERS_AND_COLORS)
            row.append({"char": char_and_color["char"], "color": char_and_color["fg"] + chr(27) + "[48;5;" + str(grayscale) + "m" + " " + char_and_color["bg"]})
        img_data.append(row)

    header = {
        "width": width,
        "height": height,
        "palette": [{
            "r": 0,
            "g": 0,
            "b": 0,
            "label": "black"
        }] + [{"r": 255, "g": 255, "b": 255, "label": "white"}]
    }

    with open(filename, "w") as fp:
        yaml.dump(header, fp)
        json.dump(img_data, fp)

def load_custom_image(filename):
    ext = os.path.splitext(filename)[-1]
    #assert ext == ".txtcc", f"Invalid file extension '{ext}', expected .txtcc"

    with open(filename, "r") as fp:
        header = yaml.safe_load(fp)
        img_data = json.load(fp)

    width, height = header["width"], header["height"]
    img = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            char_obj = img_data[y][x]
            img.putpixel((x, y), (char_obj['color'].strip().split()[1].split(";")[-1], char_obj['color'].strip().split()[2].split(";")[-1], char_obj['color'].strip().split()[3].split(";")[-1]))

    return img

filename = sys.argv[1]
img = load_custom_image(filename)
save_custom_image(img)
