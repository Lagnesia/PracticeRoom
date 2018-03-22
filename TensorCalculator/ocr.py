import sys
import numpy as np
import cv2

#이미지 로드 및 전처리
img = cv2.imread('numbers.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

#윤곽선 추출
contours = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

#윤곽선 반복 처리
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    red = (0, 0, 255)
    cv2.rectangle(img, (x, y), (x+w,y+h), red, 2)

cv2.imwrite('contour_numbers.png',img)