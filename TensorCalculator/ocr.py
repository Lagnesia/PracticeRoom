import sys
import numpy as np
import cv2
import recog

#모델 불러오기
mnist = recog.build_model()
mnist.load_weights('mnist.hdf5')

#이미지 로드 및 전처리
img = cv2.imread('numbers.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
cv2.imwrite('numbers_thresh.png')
contours = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

#추출한 사각형 정렬
rect=[]
im_width = img.shape[1]
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w<10 or h<10: continue
    if w>im_width/5: continue
    y2 =  round(y/10)*10
    index = y2*im_width+x
    rects.append((index,x,y,w,h))
rects = sorted(rects,key=lambda x:x[0])

x=[]
for r in rects:
    index,x,y,w,h = r
    


#예측
ans='123456789650912374392+-=5+42='
answer = list(ans)
right=0
