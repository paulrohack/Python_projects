import face_recognition
import cv2
image_file = "G:\Pictures\Camera Roll\paul.jpg"
k_image = cv2.imread(image_file)
k_f = [face_recognition.face_encodings(k_image)[0]]
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    u_f = face_recognition.face_encodings(img)
    if u_f != []:
        results = face_recognition.compare_faces(k_f, u_f[0])
        print(results[0])   
    else:
        print(False)
    cv2.imshow("Window", img)
    cv2.waitKey(1)     
