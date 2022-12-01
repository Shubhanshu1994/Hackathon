import cv2


cap = cv2.VideoCapture('depositphotos_228860866-stock-video-plastic-garbage-on-a-conveyor.mp4')

while(True):
  ret, frame = cap.read()
  if not ret:
    print(frame)
    break
  cv2.imshow('Frame',frame)
  cv2.waitKey(25)
cap.release()
cv2.destroyAllWindows()