from images import Image

image = Image("Image Processing/bird.gif")


def blackWhite(image):
    black = (0, 0, 0)
    white = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            avg = (r + g + b) // 3
            if avg < 128:
                image.setPixel(x, y, black)
            else:
                image.setPixel(x, y, white)


blackWhite(image)
image.draw()
image.save("Image Processing/bw.gif")