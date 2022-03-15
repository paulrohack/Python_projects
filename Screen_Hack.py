from email.charset import QP
import rotatescreen, time
import subprocess, os

screen = rotatescreen.get_primary_display()
start_pos = screen.current_orientation
#
for i in range(0, 13):
    pos = abs((start_pos - i*90) % 360)
    screen.rotate_to(pos)
    time.sleep(0.5)
#
with open("HACKED!!_LOL.txt", '+w') as f:
	f.write("Your system is hacked \nYour system is gonna shutdown \nSYSTEM GO BURRRRRR")
subprocess.Popen(["notepad.exe","HACKED!!_LOL.txt"])
# time.sleep(5)
# os.popen("shutdown /l")






















