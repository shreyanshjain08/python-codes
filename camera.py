import cv2
cap = cv2.VideoCapture(0)
status , photo = cap.read()
cv2.imshow("Shre Photo", photo[100:250, 200:350]) # for crop and colouring filtering
cv2.waitKey() # sec in milisec to wait photo
cv2.destroyAllWindows()