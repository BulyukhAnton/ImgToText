# This is fun cod. It's my first project so i hope you like it.

from PIL import Image

im = Image.open("img.jpg")
im = im.convert("1")
im.save("img.jpg")
image = Image.open("img.jpg")
width, height = image.size
counter = 0


for px in image.getdata():
    if px == 255:
        print(" ", end="")
    else:
        print("@", end="")
    counter += 1

    if counter == width:  # when the line ended
        counter = 0
        print("\n", end="")


