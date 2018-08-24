from PIL import Image
purp = "purp_dog.png"

def load_img(filename):
    load = Image.open(filename)
    return load

def show_img(load):
    load.show()

def save_img(load, filename):
    load.save(filename, "PNG")
    show_img(load)



def obamicon(purp):
    pixels = purp.getdata()
    new_pixels = []

    #s aredefining what hues in each color
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    #to process each and every single pixel. gonna run through each and
    #apply the change
    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)
        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightBlue)
        elif intensity >= 546:
            new_pixels.append(yellow)

    
    newim = Image.new("RGB", purp.size)
    newim.putdata(new_pixels)
    return newim

purpload = load_img(purp)
show_img(purpload)
show_img(obamicon(purpload))
save_img(purpload, purp)


