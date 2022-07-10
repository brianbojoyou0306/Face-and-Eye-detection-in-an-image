#FACE AND EYE RECOGNITION

import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('abc.jpg') #reading the image



faces = face_cascade.detectMultiScale(img,scaleFactor = 1.1,minNeighbors =9)
eyes = eye_cascade.detectMultiScale(img,scaleFactor = 1.1,minNeighbors =20)


for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('FACE RECOGNITION',img)
    #w and h are height and width

for x,y,w,h in eyes:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.imshow('FACE RECOGNITION',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
