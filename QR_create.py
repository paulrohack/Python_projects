import qrcode
import os

data = input("Your Data or Link: ")
img = qrcode.make(data)

save = input("Name of The QR-code: ")

dirName = 'Qr_Images'
try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
    img.save(f'Qr_Images/{save}.jpg')
    print("QR saved")
 
except FileExistsError:
    img.save(f'Qr_Images/{save}.jpg')
    print("QR saved")
   

