from PIL import Image

name = ""
width = 0
height = 0
pis_name = ""

name = str(input("Enter the full filepath of the image (only .png): "))
width = int(input("Enter the width of the image in pixels: "))
height = int(input("Enter the height of the image in pixels: "))
pis_name = str(input("Enter the filepath you want to give the converted image (include '.pis' extension): "))

width = width / 100
height = height / 100

im = Image.open(name)
px = im.load()
#print(pixels[0, 0])

pixels = [""] * 10000
counter = 0

def scan_pixel(x_f, y_f, counter_f, pixels_f):
    #print(counter)
    pixels_f[counter_f] = (px[x_f, y_f])[0:3]

    counter_f = counter_f + 1

    return pixels_f, counter_f

for y_axis in range(100):
    for x_axis in range(100):
        pixels, counter = scan_pixel(x_axis * width, y_axis * width, counter, pixels) #scans the image into a 100x100 pixel image. Make sure the x and y axes are multiples of ten and adjust numbers on this line accordingly

    #print(counter)
    #print(pixels)

final_pixels = ""

for loop in range(10000):
    spec_tuple = pixels[loop]
    
    r = spec_tuple[0]
    g = spec_tuple[1]
    b = spec_tuple[2]

    modified = ""
    modified = modified + str(r) + ","
    modified = modified + str(g) + ","
    modified = modified + str(b) + ";"

    final_pixels = final_pixels + modified

file = open(pis_name + pis_name, "w")
file.write(final_pixels)
file.close()
