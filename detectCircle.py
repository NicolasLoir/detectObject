import math
import numpy as np
import imutils
import cv2


img = cv2.imread(cv2.samples.findFile('createPanorama.jpg'))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1,
                           img.shape[0]/64, param1=50, param2=30, minRadius=20, maxRadius=30)

nb_circle = 1
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        x = i[0]
        y = i[1]
        r = i[2]
        print("center : "+str((x, y)))
        print("radius : " + str(r))

        rectX = (x - r)
        rectY = (y - r)

        crop_img = img[rectY:(rectY+2*r), rectX:(rectX+2*r)]

        cv2.imwrite('./pokeballs/pokeball' + str(nb_circle) + '.jpg', crop_img)
        # cv2.imshow("pokeball", crop_img)
        # cv2.waitKey(0)

        # dessiner le cercle decouvert
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)
        # dessiner le centre du cercle
        cv2.circle(img, (x, y), 2, (0, 0, 255), 3)
        nb_circle += 1


# cv2.imshow("ex3", img)
# cv2.waitKey(0)
cv2.imwrite('detectCircle.jpg', img)
