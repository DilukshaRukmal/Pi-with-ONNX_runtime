import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0) #default camera
cap.set(3,500)
cap.set(4,500)

# capture image from camera
ret, frame = cap.read()
frame = cv.flip(frame, -1) # Flip camera vertically
cv.imwrite('test.jpg', frame)
 
while(True):
    ret, frame = cap.read()
    frame = cv.flip(frame, -1) # Flip camera vertically
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow('frame', frame)
    cv.imshow('gray', gray)
    
    k = cv.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv.destroyAllWindows()