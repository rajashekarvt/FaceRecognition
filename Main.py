import dlib
import cv2
from cv2 import COLOR_BGR2RGB
import face_recognition



img=cv2.imread("image.jpg")
rgb_img=cv2.cvtColor(img,COLOR_BGR2RGB)
img_encoding=face_recognition.face_encodings(rgb_img)[0]


img2=cv2.imread("KSI.jpg")
rgb_img2=cv2.cvtColor(img,COLOR_BGR2RGB)
img_encoding2=face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding],img_encoding2)
print("Result:",result)







cv2.imshow("Img",img)
cv2.imshow("Img 2",img2)
cv2.waitKey(0)