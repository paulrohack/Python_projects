from selenium import webdriver
import json




book = input("Book:  ").upper()
chapter = (input("Chapter (Defaults to Chapter 1):  "))
verse_no = (input("Verses (Can leave if want to read the Whole Chapter):  "))

if not chapter:
    chapter = 1

if not verse_no:
    verse_no = f''
else:
    verse_no = f'.{verse_no}'

if book:
    file = json.load(open('BibleAutomation\Chapters_id.json', 'r'))
    for n in file['items']:
        if book == n['Book'].upper():
            book_id = n['id']
            break
        else:
            book_id = None

    if book_id != None:
        pass
        NKJV = 114
        URL = f'https://www.bible.com/bible/{NKJV}/{book_id}.{chapter}{verse_no}'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(URL)
if verse_no:
    driver.implicitly_wait(1)
    print('')
    head = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/h1')[0].text
    verse = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div[1]').text
    driver.quit()
    print(head)
    print(verse)
