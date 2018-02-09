#coding:utf-8
from __future__ import print_function
from PIL import Image
from colorama import Fore,Back,Style
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('file')  
parser.add_argument('-o', '--output')  
parser.add_argument('--width', type = int, default = 30) 
parser.add_argument('--height', type = int, default = 30) 

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

COLORS = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
COLORS_RGB = [(0,0,0), (255,0,0), (0, 255,0), (255,255,0), (0,0,255), (255,0,255), (0,255,255), (255,255,255)]
ASSIIC_CHAR = list("12q$e@x ")

def i2(r, g, b):
    color_len = []
    for i in COLORS_RGB:
        temp = (i[0] - r)*(i[0] - r) + (i[1] - g)*(i[1] - g) + (i[2] - b)*(i[2] - b)
        color_len.append(temp)
    return color_len.index(min(color_len))

def get_char(r, g, b, a=256):
    i = i2(r, g, b)
    return ASSIIC_CHAR[i], i

if __name__ == '__main__':
    pic = Image.open(IMG)
    pic = pic.resize((WIDTH, HEIGHT), Image.NEAREST)
    pic.show()
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            ch, w = get_char(*pic.getpixel((j, i)))
            print(COLORS[w]+ch*3, end='')
            txt += ch
        print('\n')
        txt += '\n'

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)