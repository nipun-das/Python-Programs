from images import Image

image = Image(150,150)
image.draw()

blue = (0,0,255)
y = image.getHeight()//2

for x in range(image.getWidth()):
    image.setPixel(x,y-1,blue)
    image.setPixel(x,y,blue)
    image.setPixel(x,y+1,blue)
image.draw()
image.save("Image Processing/horiz.gif")