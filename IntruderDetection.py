from cvzone.PoseModule import PoseDetector
import cv2
import serial, time, os
try:
    os.mkdir('Images')
except:
    pass
run = True
# try:
#     s = serial.Serial('COM5', 9600, timeout=1)
# except:
#     print("ERROR COMMUNICATION WITH BOARD")
#     run = False
    
if run:
    cap = cv2.VideoCapture(1)
    detector = PoseDetector()
while run:
    success, img = cap.read()
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img)
    print(lmList)
    if (lmList[0]) != []:
        # s.write(b'H')
        text = f"Intruder_Found_at_{round(time.time())}"
        cv2.imwrite(f'H:\Python\Images\{text}.jpg', img)
    else:
        # s.write(b'L')
        pass
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xff == ord('q'):        
        break
