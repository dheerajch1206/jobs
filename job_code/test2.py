# Required Libraries
import telebot
import requests
import time
# import pyttsx3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import telebot
from datetime import date
from datetime import datetime

today = date.today() # today date

API_KEY='5871654163:AAHK5FAF8cDT8IYejZVaLzEadnFb1p8L4RE'
bot=telebot.TeleBot(API_KEY)

PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver

driver = webdriver.Chrome(PATH)

driver.get('https://careers.bloomberg.com/job/search?el=Students+and+Recent+Graduates&lc=New+York')
#driver.get('https://www.amazon.jobs/en/job_categories/data-science?offset=0&result_limit=10&sort=relevant&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&')

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/main/div/div[3]/div/div/div/div[2]/div[2]")))
print('netx')
out_div = driver.find_element(By.XPATH,'/html/body/div[7]/main/div/div[3]/div/div/div/div[2]/div[2]')
lis = out_div.find_elements(By.CLASS_NAME,'job-results-section')
print(lis)
# /html/body/div[7]/main/div/div[3]/div/div/div/div[2]/div[2]
# /html/body/div[7]/main/div/div[3]/div/div/div/div[2]/div[2]/div[1]/span[1]
#bot.send_message(message.chat.id, text='IBM')
if(len(lis)>0):
    for i in lis:
        days = int(str(today - datetime.strptime('Aug 17, 2022', "%b %d, %Y").date()).split(" ")[0])
        if(days < 3):
            link = i.find_element(By.XPATH,'./div/a').get_attribute('href')
            #bot.send_message(message.chat.id, text=link)
            print(link)
time.sleep(20)
driver.quit()

