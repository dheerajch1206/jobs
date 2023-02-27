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


driver.get('https://q2ebanking.wd5.myworkdayjobs.com/Q2')

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[2]/section")))
time.sleep(2)

out_div = driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/div/div/div[2]/section')
lis = out_div.find_elements(By.CLASS_NAME, 'css-1q2dra3')

page_out_div = driver.find_element(By.XPATH,'/html/body/div/div/div/div[3]/div/div/div[2]/section/div[2]')
page_lis = page_out_div.find_elements(By.CLASS_NAME,'css-1j096s0')
page_num = 1


# bot.send_message(message.chat.id, text='Q2')

while page_num <= len(page_lis):

    page_num_button = page_lis[page_num - 1].find_element(By.XPATH, './button')
    page_num_button.click()

    time.sleep(5)

    out_div = driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/div/div/div[2]/section')
    lis = out_div.find_elements(By.CLASS_NAME, 'css-1q2dra3')

    # bot.send_message(message.chat.id, text='Dell')
    if len(lis) > 0:
        for i in lis:
            days = i.find_element(By.XPATH, './div[3]/div/div/dl/dd').text.split(" ")[1]
            if days == 'Today':
                days = 0
            if days != '30+':
                days = int(days)
                if days < 30:
                    link = i.find_element(By.XPATH, './div[1]/div/div/h3/a').get_attribute('href')
                    # bot.send_message(message.chat.id, text=link)
                    print(link)
    page_num = page_num + 1


time.sleep(5)
driver.quit()

