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



driver.get('https://jobs.fidelity.com/job-search-results/?parent_category[]=Technology')

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/main/div/section/div/div/div/div/div[2]/div/div[2]/div[1]/div[5]")))
time.sleep(2)

out_div = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/section/div/div/div/div/div[2]/div/div[2]/div[1]/div[5]')
inner_div = out_div.find_element(By.XPATH,'./div[2]/div')
lis = inner_div.find_elements(By.XPATH, './/*')
#/html/body/div[1]/div[2]/main/div/section/div/div/div/div/div[2]/div/div[2]/div[1]/div[5]/div[2]/div/div[1]
#/html/body/div[1]/div[2]/main/div/section/div/div/div/div/div[2]/div/div[2]/div[1]/div[5]/div[2]/div/div[1]/div/div[1]/div[2]/a

print(lis)
for i in lis:
    link = i.find_element(By.XPATH,'./div/div[1]/div[2]/a').get_attribute('href')
    print(link)

time.sleep(5)
driver.quit()