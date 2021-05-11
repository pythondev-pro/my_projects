import os
import sys

from PIL import Image

# grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]

# check if /new exists, if not create it
if not os.path.exists(directory):
    os.makedirs(directory)

# Loop through the folder
for filename in os.listdir(path):
    # separate the name from its extension
    clean_name = os.path.splitext(filename)[0]
    # open the file
    img = Image.open(
        f'{path}{filename}')  # added the / in case user doesn't enter it. You may want to check for this and add or remove it.
    # save the file as 'png'
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')
