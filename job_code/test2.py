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

driver.get('https://q2ebanking.wd5.myworkdayjobs.com/Q2?locations=0da4bb96663010308829a8dfd4e91994&locations'
           '=3b54c7e3a94801ec9b86115c1c017e76&jobFamilies=8b86f00a4a2a0161c8f6dbdc0288ab6a&jobFamilies'
           '=8b86f00a4a2a01e03cacfbdc0288b96a&jobFamilies=54838d87026b0142d4a0dd78070250f5')
#driver.get('https://www.amazon.jobs/en/job_categories/data-science?offset=0&result_limit=10&sort=relevant&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&')

# element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/main/div/div[3]/div/div/div/div[2]/div[2]")))
# print('netx')
time.sleep(4)

out_div = driver.find_element(By.XPATH,'/html/body/div/div/div/div[3]/div/div/div[2]/section')
lis = out_div.find_elements(By.CLASS_NAME,'css-1q2dra3')

# /html/body/div[7]/main/div/div[3]/div/div/div/div[2]/div[2]
# /html/body/div[7]/main/div/div[3]/div/div/div/div[2]/div[2]/div[1]/span[1]
#bot.send_message(message.chat.id, text='IBM')
if(len(lis)>0):
    for i in lis:
        days = (i.find_element(By.XPATH,'./div[3]/div/div/dl/dd').text).split(" ")[1]
        if days != '30+':
            days = int(days)
            print(days)

            if(days < 16):
                link = i.find_element(By.XPATH,'./div[1]/div/div/h3/a').get_attribute('href')
                #bot.send_message(message.chat.id, text=link)
                print(link)
time.sleep(5)
driver.quit()

