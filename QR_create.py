import qrcode
import os, tkinter, PIL

data = input("Your Data or Link: ")
img = qrcode.make(data)
filename = "qrcode.png"
img.save(filename)
image = PIL.Image.open(filename)
width, height = image.size
root = tkinter.Tk()
root.geometry(f'{width}x{height}')
# root.maxsize()
root.wm_title(f"QRCODE - {data}")
canvas = tkinter.Canvas(root, width = width, height = height)      
canvas.pack(side='left')      
img = tkinter.PhotoImage(file=filename)      
canvas.create_image(0,0, anchor='nw',image=img)  
root.mainloop()
image.close()
os.system(f"del {filename}")



   

