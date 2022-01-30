import numpy as np
import imutils
import cv2

img = cv2.imread(cv2.samples.findFile('Capture.PNG'))
img_rgb = cv2.medianBlur(img, 5)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# cv2.imshow("ex4", img_gray)
# cv2.waitKey(0)

# Ouvrir le template et recuperer ses dimensions
template = cv2.imread(cv2.samples.findFile('./pokeballs/pokeball3.jpg'))
template = cv2.medianBlur(template, 5)
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
cv2.imshow("pokebal", template)
# cv2.waitKey(0)
# cv2.imshow("ex4", template)
# cv2.waitKey(0)

# si erreur ici, possible de mettre w, h, _ = ...
w, h = template.shape[::-1]
resultat = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# Definir notre limite de detection (threshold)
threshold = 0.85
position = np.where(resultat >= threshold)
# En utilisant les données des template detecter, nous les marquons sur notre image dans un rectangle
for point in zip(*position[::-1]):
    cv2.rectangle(img_rgb, point, (point[0] + w, point[1] + h), (0, 0, 255), 2)
    cv2.imshow("templateMatching", img_rgb)
    cv2.waitKey(0)
cv2.imwrite('templateMatching.jpg', img_rgb)
