import serial
#
run = True
try:
    s = serial.Serial('COM5', 9600, timeout=1)
except:
    print('ERROR COMMUNICATING WITH THE BOARD')
    run = False
while run:
    if input() == 'o':
        s.write(b'H')
    if input() == 'f':
        s.write(b'L')
