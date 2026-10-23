import cv2 as cv
import os
import matplotlib.pyplot as mp
import numpy as np

def readImage():
    root = os.getcwd()
    imgPath = os.path.join(root, "demoimages", "moggerpick.jpeg")
    img = cv.imread(imgPath)
    cv.imshow("img",img)
    cv.waitKey(0)



if __name__ == "__main__":
    readImage()
    