# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
#     # Display the resulting frame
#     cv2.imshow('frame',frame)
#     cv2.imshow('gray',gray)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()

# import cv2
# from cv2 import aruco

# # Verify if DetectorParameters_create exists
# if hasattr(aruco, 'DetectorParameters_create'):
#     print("DetectorParameters_create is available!")
# else:
#     print("DetectorParameters_create is not found.")

import cv2
from cv2 import aruco
print(dir(aruco))

