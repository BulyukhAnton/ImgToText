# This is fun cod. It's my first project so i hope you like it. Enjoy yourself :)

from PIL import Image

im = Image.open('img.jpg')
im = im.convert('1')
im.save('img.jpg')
image = Image.open('img.jpg')
width, height = image.size
counter = 0



for px in image.getdata(): # getting all the pi


    if px >= 127: # if pixel is light it must be white
        print(' ', end='')
    else: # else it must be dark
        print("@", end='')
    counter += 1
    if counter == width:
        counter = 0
        print('\n', end='')
