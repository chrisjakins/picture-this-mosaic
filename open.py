"""
    Chris Jakins
"""

from PIL import Image
import numpy as np

im = Image.open("./testImages/test1.jpg")
width, height = im.size
pix = im.load()

result = np.array([0, 0, 0])
for x in range(0, width) :
    for y in range(0, height) :
        pixel = pix[x, y]
        result[0] += pixel[0]
        result[1] += pixel[1]
        result[2] += pixel[2]

result = np.divide(result, width * height)
print(result)

#
# showcasing
#

#print(pix[100, 100])

#pix[100, 100] = (210, 210, 210)

#im.save("final.png")

#
# end
#

