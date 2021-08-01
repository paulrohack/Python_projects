import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2

np.set_printoptions(suppress=True)
p = ["Mask", "No Mask"]
nn = 0
pn = 0
n = 0
cap = cv2.VideoCapture(0)
model = tensorflow.keras.models.load_model('Mask_Detection\High_keras_model.model')
# model = tensorflow.keras.models.load_model('MaskDetection\keras_model.h5')

path = 'Mask_Detection\img.jpg'
size = (224, 224)
text = '.......'

while True:
    _, img = cap.read()
    img = cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("HELLO", img)
    
    cv2.imwrite(path, img)
    # img = cv2.resize(img, size)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(path)

    # image = Image.fromarray(img)
    # image.show()

    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.int64) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    mask = prediction[0,0]
    nomask = prediction[0,1]
    maxp = max(mask, nomask)
    pn = n

    if  maxp == mask:
        n = 0
        nn = 0
    else:
        n = 1
        nn = 1
    if pn != nn and int((maxp)*100) > 75:
        text = (f'{p[n]} >>> ConfidenceLevel: {int((maxp)*100)}%')        
    elif int((maxp)*100) < 50:
        text = 'Not So Sure'
    if cv2.waitKey(1) & 0xff == ord('q'):        
        break

        


