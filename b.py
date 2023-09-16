import cv2
import sys
import numpy as np



src = cv2.imread('tkalfk.jpg')
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

src = cv2.imread('tkalfk.jpg', cv2.IMREAD_GRAYSCALE)
blr = cv2.GaussianBlur(src, (0, 0), 2)

def on_trackbar(pos):
    alpha = cv2.getTrackbarPos('alpha x 10', 'dst')
     
    dst = np.clip((1.0+alpha/10)*src - alpha/10*blr, 0, 255).astype(np.uint8)
    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('alpha x 10', 'dst', 0, 10, on_trackbar)
on_trackbar(0)
cv2.waitKey()
cv2.destroyAllWindows()

# 실수 형태로 연산(float32)
src_f = src_ycrcb[:, :, 0].astype(np.float32)
blr = cv2.GaussianBlur(src_f, (0, 0), 2.0)
# 최종 결과는 정수로(uint8)
src_ycrcb[:, :, 0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8)

dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)
