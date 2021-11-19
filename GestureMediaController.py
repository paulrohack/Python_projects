from pynput.keyboard import Key,Controller
import time
import cvzone.HandTrackingModule as detector
import  cv2

keyboard = Controller()
def volumeup(t):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        if t != 0:
            time.sleep(t)
def volumedown(t):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        if t != 0:
            time.sleep(t)

cap = cv2.VideoCapture(0)
hand_detector = detector.HandDetector(maxHands=1, detectionCon=0.5)


debug = True
while True:
    _, img = cap.read()
    img = cv2.flip(img, 90)
    # img, detected = hand_detector.findHands(img, False)
    # box = hand_detector.findPosition(img, 0, False)
    # if detected:
    #     finger = box[0]

    #     thumbfinger = finger[4]
    #     indexfinger = finger[8]

    #     distance, _, _ = hand_detector.findDistance(thumbfinger, indexfinger, img, debug)
    #     d = round(distance/100, 2)
    #     if d > 2.0:
    #         volumeup(0)
    #     elif d > 1.0:
    #         volumeup(0.3)
    #     elif d > 0.5:
    #         volumedown(0.3)
    #     else:
    #         volumedown(0)
    if debug:
        cv2.imshow("Window", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break