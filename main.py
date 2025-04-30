from PIL import Image, ImageFilter
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('image_name', help='filename of the image you are filtering')
parser.add_argument('--filter_to_edge', default=False, action='store_true', help='filters an image to only show edges')
parser.add_argument('--invert_color', default=False, action='store_true', help='Inverts the color code of each pixel')
parser.add_argument('--save_to', default=None, help='output_file. Include.png')

args = parser.parse_args()

image = Image.open(args.image_name)
image_copy = image

if args.filter_to_edge:
    image = image.convert('L')

    image = image.filter(ImageFilter.FIND_EDGES)

    image.show()

if args.invert_color:
    