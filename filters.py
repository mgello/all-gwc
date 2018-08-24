from PIL import Image
import math

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

    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

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
#show_img(purpload)
show_img(obamicon(purpload))
#save_img(purpload, purp)

def grayscale(purp):
  pixels = purp.getdata()
  new_pixels = []
  
  for p in pixels:
    new_p = avg_pixel(p)
    new_pixels.append(new_p)

  newim = Image.new("RGB", purp.size)
  newim.putdata(new_pixels)
  return newim

# Return a grayscale tuple for a single pixel value.
def avg_pixel(pixel):
  avg = (pixel[0] + pixel[1] + pixel[2]) // 3 # Use // for int division.
  return (avg, avg, avg) # R = G = B will be a gray pixel!

purpload = load_img(purp)
show_img(grayscale(purpload))
#save_img(purpload, purp)








def invert(purp):
  pixels = purp.getdata()
  new_pixels = []
  
  for p in pixels:
    new_r = 255-p[0]
    new_g = 255-p[1]
    new_b = 255-p[2]
    new_pixels.append((new_r, new_g, new_b))

  newpurp = Image.new("RGB", purp.size)
  newpurp.putdata(new_pixels)
  return newpurp

purpload = load_img(purp)
show_img(invert(purpload))









def art(im, rgb_color, threshold):

  pixels = purp.getdata()
  new_pixels = []

  blue = (12, 132, 251)
  red = (52, 86, 89)
  yellow = (252, 228, 89)
  green = (117, 242, 89)


  for p in pixels:
      
        if p < (255, 255, 255):
            new_pixels.append(blue)
        elif p >= (255, 255, 255) and p < 364:
            new_pixels.append(red)
        elif p >= 364 and p < 546:
            new_pixels.append(yellow)
        elif p >= 546:
            new_pixels.append(green)
    
  # Save the filtered pixels as a new image
  newpurp = Image.new("RGB", purp.size)
  newpurp.putdata(new_pixels)
  return newpurp

purpload = load_img(purp)
show_img(art(purpload))



