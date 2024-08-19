import cv2 
cap = cv2.VideoCapture(0)
while True :
    status , photo = cap.read()
    cv2.imshow("Shre Photo " , photo)
    if cv2.waitKey(100) ==13 :
        break
    
cap.release()
cv2.destoryAllWindows()