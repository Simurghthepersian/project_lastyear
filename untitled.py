import numpy as np
import cv2

image = cv2.imread('bottle.jpg')
original = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([22, 93, 0], dtype="uint8")
upper = np.array([45, 255, 255], dtype="uint8")
mask = cv2.inRange(image, lower, upper)

cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(original, (x, y), (x + w, y + h), (36,255,12), 2)

red_lower = np.array([0, 100, 20],dtype="uint8")
red_upper = np.array([10, 255, 255], dtype="uint8")
red_mask =cv2.inRange(image, red_lower, red_upper)

cnts_2 = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts_2 = cnts_2[0] if len(cnts_2) == 2 else cnts_2[1]


for c_2 in cnts_2:
    x,y,w,h = cv2.boundingRect(c_2)
    cv2.rectangle(original, (x, y), (x + w, y + h), (45, 255, 255), 2)
    

lower_white = np.array([0,0,255],dtype="uint8")
upper_white = np.array([255,255,255],dtype="uint8")
cnts_3 = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts_3 = cnts_3[0] if len(cnts_3) == 2 else cnts_3[1]


for c_3 in cnts_3:
    x,y,w,h = cv2.boundingRect(c_3)
    cv2.rectangle(original, (x, y), (x + w, y + h), (255, 255, 255), 2)
   
lower_green = np.array([40, 40,40],dtype="uint8")
upper_green = np.array([70, 255,255],dtype="uint8")
cnts_4 = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts_4 = cnts_4[0] if len(cnts_4) == 2 else cnts_4[1]


for c_4 in cnts_4:
    x,y,w,h = cv2.boundingRect(c_4)
    cv2.rectangle(original, (x, y), (x + w, y + h), (255, 255, 0), 2)
    

lower_black = np.array([0, 0,0],dtype="uint8")
upper_black = np.array([255, 255,0],dtype="uint8")
cnts_5 = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts_5 = cnts_5[0] if len(cnts_5) == 2 else cnts_5[1]


for c_5 in cnts_5:
    x,y,w,h = cv2.boundingRect(c_5)
    cv2.rectangle(original, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    
cv2.imshow('mask', mask)
cv2.imshow('original', original)

cv2.imwrite('bottle2.jpg', original)
cv2.waitKey()