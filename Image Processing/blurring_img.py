from images import Image
from functools import reduce

image = Image("Image Processing/bird.gif")
image.draw()

def blur(image):
    def tripleSum(triple1, triple2):
        (r1, g1, b1) = triple1
        (r2, g2, b2) = triple2
        return (r1 + r2, g1 + g2, b1 + b2)

    new = image.clone()

    for y in range(1, image.getHeight() - 1):
        for x in range(1, image.getWidth() - 1):
            oldPixel = image.getPixel(x, y)
            left = image.getPixel(x - 1, y)
            right = image.getPixel(x + 1, y)
            top = image.getPixel(x, y - 1)
            bottom = image.getPixel(x, y + 1)
            sum = reduce(tripleSum, [oldPixel, left, right, top, bottom])
    avg = tuple(map(lambda x: x // 5, sum))
    new.setPixel(x, y, avg)
    return new
    

blur(image)
image.draw()