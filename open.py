"""
    Chris Jakins
"""

from PIL import Image
import numpy as np
import os

def averageRGB( filename ) :
    im = Image.open( filename )
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
    return result



#
# Effective "main"
#

sampleRGB = []
filenames = []

path = os.getcwd() + "/testImage/"
for filename in os.listdir(path) :
    filenames.append("./testImage/" + filename)
    sampleRGB.append( averageRGB("./testImage/" + filename) )



#
# showcasing
#

#print(pix[100, 100])

#pix[100, 100] = (210, 210, 210)

#im.save("final.png")

#
# end
#

