import cv2 as cv
import numpy as np
from PIL import ImageGrab
import matplotlib.pyplot as plt
import datetime
import time


# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv.line(im, tuple(bbox[j][0]), tuple(bbox[(j + 1) % n][0]), (255, 0, 0), 3)

    # Display results
    cv.imshow("Results", im)


while True:
    img = ImageGrab.grab()
    img_np = np.array(img)
    img = cv.cvtColor(img_np, cv.COLOR_BGR2GRAY)
    # cv.imshow('window', img)

    qrDecoder = cv.QRCodeDetector()

    # Detect and decode the qrcode
    data, bbox, rectifiedImage = qrDecoder.detectAndDecode(img)
    if len(data) > 0:
        ts = time.time()
        # print("Decoded Time : {}".format(data))
        # print("Current Time : {}".format(ts))
        diff = abs(round(float(ts) - float(data) - 0.2, 1))
        print("Diff : {}".format(diff))
        # display(img, bbox)
        # rectifiedImage = np.uint8(rectifiedImage)
        # cv.imshow("Rectified QRCode", rectifiedImage)
    else:
        print("QR Code not detected")
        # cv.imshow("Results", img)
