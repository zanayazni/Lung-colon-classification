import cv2
import numpy as np

IMAGE_SIZE = (128, 128)

def preprocess_image(img):
    img = cv2.resize(img, IMAGE_SIZE)

    img = cv2.medianBlur(img, 3)
    img = cv2.GaussianBlur(img, (5, 5), 0)

    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    img = cv2.cvtColor(img_yuv, cv2.COLOR_YCrCb2BGR)

    return img

def extract_features(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    texture = cv2.createCLAHE().apply(gray)
    texture_mean = np.mean(texture)
    texture_std = np.std(texture)
    moments = cv2.moments(gray)
    hu_moments = cv2.HuMoments(moments).flatten()
    return [texture_mean, texture_std] + list(hu_moments)
