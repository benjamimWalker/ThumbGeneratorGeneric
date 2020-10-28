from typing import Tuple
from PIL import Image, ImageOps, ImageEnhance
import os
from random import choice
# Imports

colors: Tuple[str, str, str, str, str, str] = '#00ff00f', '#cc231b', '#1342eb', '#ff6f00', '#5c0ee3', '#00f4fc', '#e1ff00'
# Colors

input_file = 'path for importing image'
output_path = 'path for saving thumbnail'
# Your output

original = Image.open(input_file)
# The original image

ImageEnhance.Brightness(original).enhance(1.035).save('bright.png')
ImageEnhance.Color(Image.open('bright.png')).enhance(1.8).save('color.png')
ImageEnhance.Contrast(Image.open('color.png')).enhance(1.6).save('contrast.png')
ImageEnhance.Sharpness(Image.open('contrast.png')).enhance(3).save('all_enhanced.png')
# Better image

ImageOps.expand(Image.open('all_enhanced.png'), border=35, fill=choice(colors)).resize((1280, 720)).save(
    output_path + 'all_enhanced_border.png')
# Border & resize

os.remove('bright.png')
os.remove('color.png')
os.remove('contrast.png')
os.remove('all_enhanced.png')
# Removing garbage
