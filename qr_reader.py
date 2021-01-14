import cv2 as cv
import numpy as np
from PIL import ImageGrab
import datetime


# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv.line(im, tuple(bbox[j][0]), tuple(bbox[(j + 1) % n][0]), (255, 0, 0), 3)

    # Display results
    cv.imshow("Results", im)


while True:
    screen = ImageGrab.grab()
    img = np.array(screen.getdata(), dtype='uint8')
    img = img.reshape((screen.size[1], screen.size[0], 3))
    w, h = screen.size
    w = int(w / 2)
    h = int(h / 2)
    img = cv.resize(img, (w, h))
    # cv.imshow('window', cv.cvtColor(img, cv.CV_32F))

    qrDecoder = cv.QRCodeDetector()

    # Detect and decode the qrcode
    data, bbox, rectifiedImage = qrDecoder.detectAndDecode(img)
    if len(data) > 0:
        ts = datetime.datetime.now()
        print("Decoded Time : {}".format(data))
        print("Current Time : {}".format(ts))
        # display(img, bbox)
        # rectifiedImage = np.uint8(rectifiedImage)
        # cv.imshow("Rectified QRCode", rectifiedImage)
    else:
        print("QR Code not detected")
        # cv.imshow("Results", img)
