from selenium import webdriver
from tkinter import *
from PIL import ImageTk,Image


URL = 'https://www.bible.com/verse-of-the-day'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(URL)
driver.minimize_window()
driver.implicitly_wait(1)
verse = driver.find_element_by_xpath('//*[@id="votd_wrapper"]/div/div/div[1]/div[1]').text
# print(verse)
img_web = driver.find_element_by_xpath('//*[@id="votd_wrapper"]/div/div/div[1]/amp-carousel/div[1]/div[1]/div/a/amp-img/img').get_attribute('src')
driver.get(img_web)
file = "VerseoftheDay.png"
driver.save_screenshot(file)
driver.quit()

root = Tk()
root.title('Verse Of the Day')
root.geometry('600x700')
root.minsize(width=600, height=700)
root.maxsize(width=600, height=800)

Font = ("Comic Sans MS", 15, "bold")

canvas = Canvas(root, width = 600, height = 600, bg='#0e0e0e')
text = Text(root, wrap=WORD, padx=10, fg='white', bg='#0e0e0e',font=Font)
text.insert(INSERT, verse)

canvas.pack()
text.pack()
f = open(file, "rb")
img = Image.open(f)
img = ImageTk.PhotoImage(img)
canvas.create_image(300, 300, anchor='center', image=img)
root.mainloop()

 
