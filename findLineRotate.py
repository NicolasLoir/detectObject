import math
import numpy as np
import imutils
import cv2

img = cv2.imread(cv2.samples.findFile('createPanorama.jpg'))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


pixel_removed = 15
scale_percent = 100  # Si besoin de dézoomer votre image plus tard
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
crop_img = img[pixel_removed:height-pixel_removed,
               pixel_removed:width-pixel_removed]
# crop_img = img

edges = cv2.Canny(crop_img, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

line = lines[3]

print(line)
rho, theta = line[0]
a = np.cos(theta)
b = np.sin(theta)
x0 = a*rho
y0 = b*rho
x1 = int(x0 + 1000*(-b))
y1 = int(y0 + 1000*(a))
x2 = int(x0 - 1000*(-b))
y2 = int(y0 - 1000*(a))
cv2.line(crop_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# print(lines[0][0])

# print(math.degrees(rho))
# print(math.degrees(theta))

# rho, theta = lines[0][0]
# rotated = imutils.rotate(crop_img, math.degrees(rho), scale=1)

rotated = imutils.rotate(crop_img, 180 * theta / math.pi - 90, scale=1)

cv2.imwrite('findLineRotate.jpg', rotated)
