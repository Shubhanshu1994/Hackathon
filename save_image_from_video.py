import os
import cv2


cap = cv2.VideoCapture('depositphotos_228860866-stock-video-plastic-garbage-on-a-conveyor.mp4')
i = 0
save_dir_name = "images"
while(True):
  ret, frame = cap.read()
  if not ret:
    print(frame)
    break
  imagename = f"img_{i}.jpg"
  cv2.imwrite(os.path.join(save_dir_name, imagename), frame)
  cv2.imshow('Frame',frame)
  cv2.waitKey(25)
  i += 1
cap.release()
cv2.destroyAllWindows()