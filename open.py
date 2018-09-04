"""
    Chris Jakins
"""

#
# Imports
#

from PIL import Image
import numpy as np
import os

#
# Globals
#

DOT = "."
SLASH = "/"
sampleImageDirectory = "testImage/"

#
# Math methods
#

def averageRGB( filename ) :
    im = Image.open( filename )
    width, height = im.size
    pix = im.load()

    # could possibly optimize this
    result = np.array([0, 0, 0])
    for x in range(0, width) :
        for y in range(0, height) :
            pixel = pix[x, y]
            result[0] += pixel[0]
            result[1] += pixel[1]
            result[2] += pixel[2]

    result = np.divide(result, width * height)
    return result


def twoNorm(x):
    return np.linalg.norm(x, ord = 2)


def cauchyShwarz(x, y):
    

# something like this, check docuentation for min
def getMin(arr):
    return np.min(arr)
#
# Effective "main"
#

sampleRGBAverages = []
cauchyShwarzSimil = []
filenames = []
sampleCount = 0

path = os.getcwd() + SLASH + sampleImageDirectory
for filename in os.listdir(path) :
    filenames.append(DOT + SLASH + sampleImageDirectory + filename)
    sampleRGBAverages.append(filenames[sampleCount])
    sampleCount += 1

for i in range(0, sampleCount):
    cauchyShwarzSimil.append(cauchyShwarz(sampleRBGAverages[i], finalRGBAverage)
    # find min_element

#
# showcasing
#

#print(pix[100, 100])

#pix[100, 100] = (210, 210, 210)

#im.save("final.png")

#
# end
#

