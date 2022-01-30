from imutils import paths
import numpy as np
import argparse
import imutils
import cv2


# Fusion d'images pour création d'un panorama
def pano(img_paths):
    # Création du tableau d'images
    images = []
    # On boucle sur notre liste de nom d'images pour les ajouters au tableau d'images
    for imagePath in img_paths:
        image = cv2.imread(imagePath)
        images.append(image)

    # Initialisation du stitcher et essai de panorama
    stitcher = cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)
    # if the status is '0', then OpenCV successfully performed image stitching
    if status == 0:
        return stitched
    # otherwise the stitching failed, likely due to not enough keypoints) being detected
    else:
        print("[INFO] image stitching failed ({})".format(status))
        return


# On utilise le chemin du dossier contenant les images pour initialiser une liste de nom de fichier
imagePaths = sorted(list(paths.list_images("./sliced/")))
# imagePaths = sorted(list(paths.list_images("sliced\\")))
img = pano(imagePaths)
cv2.imwrite("createPanorama.jpg", img)
