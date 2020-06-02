import sys
import os
from PIL import Image

input_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
	os.makedirs(output_folder)
	for filename in os.listdir(input_folder):
		image = Image.open(f'{input_folder}{filename}')
		clean_name = os.path.splitext(filename)[0]
		image.save(f'{output_folder}{clean_name}.png','png')
	print("all done!!")


