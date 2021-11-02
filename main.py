import random
from PIL import Image

def get_file():
    global my_image
    try:
        filename = input("please say lobster.jpeg or widesaak.png")
        my_image = Image.open(filename)
    except:
        print("give me a file name")
        get_file()
get_file()


#random_int = random.randint(0,10)
#my_image = Image.new(mode="RGB", size=(10, 10), color=(0, 0, 0))
def My_image():
    rows = my_image.size[0]
    cols = my_image.size[1]
    print(rows, cols)

    px = my_image.load()
    #px[9, 9] = (0, 0, 0)

    for i in range(0, rows):
        start = random.randint(0, rows)
        end = random.randint(0, cols)
        nub = random.randint(1, 10)

        if i % 2 == 0:
            start = 0
        else:
            start = 1

        for j in range(start, cols, nub):
            red = random.randint(0, 0)
            green = random.randint(0, 0)
            blue = random.randint(0, 0)
            if j % 2 == 0:
                red = 0
                green = 0
                blue = 0
            else:
                red = 255
                green = 255
                blue = 255

            px[i, j] = (red, green, blue)

    my_image.show()