from images import Image

image = Image("Image Processing/bird.gif")


def grayscale(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            sum = r + g + b
            image.setPixel(x, y, (sum, sum, sum))


grayscale(image)
image.draw()
image.save("Image Processing/gs.gif")