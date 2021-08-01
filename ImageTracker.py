import cv2 

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('Test.avi')

_, img = cap.read()

cv2.imshow("ROI selector", img)
box = cv2.selectROI(img, False)
cv2.destroyWindow('ROI selector')
        

tracker = cv2.TrackerMIL_create()
tracker.init(img, box)

run = True
while run:
    _, img = cap.read()
    # cv2.imwrite("img.png", img)
    
    # img = cv2.imread('img.png')
    working, box = tracker.update(img)

    if working:
        x, y = (int(box[0]), int(box[1]))
        w, h = (int(x + box[2]), int(y + box[3]))
        cv2.rectangle(img, (x, y), (w, h), (0,0,255), 2, 1)  
        cv2.putText(img, "Tracking", (x , y+10), 1, 1, (0, 255, 0), 2)
        
        cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        run = False


