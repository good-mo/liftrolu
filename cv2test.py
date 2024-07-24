import cv2
import numpy as np
import os
# print(os.path)
# if not os.path.exists('test.png'):
#     print('Image file not found')
# # 加载图像
img = cv2.imread('/root/liftrolu/test.png')

# 将图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 对图像进行边缘检测
edges = cv2.Canny(gray, 100, 200)

# 找到轮廓
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 找到最大的轮廓
max_contour = max(contours, key=cv2.contourArea)

# 计算轮廓的周长
perimeter = cv2.arcLength(max_contour, True)

# 计算腰围
waist = perimeter / 2

# 在图像上绘制轮廓和腰围
cv2.drawContours(img, [max_contour], -1, (0, 255, 0), 2)
cv2.putText(img, 'Waist: {:.2f} cm'.format(waist), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# 显示图像
cv2.imshow('Waist Measurement', img)
cv2.waitKey(0)
cv2.destroyAllWindows()