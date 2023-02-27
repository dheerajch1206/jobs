# Required Libraries


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import telebot

from datetime import date
from datetime import datetime
# Required Variables

API_KEY='5871654163:AAHK5FAF8cDT8IYejZVaLzEadnFb1p8L4RE'
bot=telebot.TeleBot(API_KEY)

today = date.today() # today date
d3 = today.strftime("%m/%d/%y")

end_delay = 5

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    # Walmart
    PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver" # Path to chromedriver
    driver=webdriver.Chrome(PATH)
    try:
        driver.get('https://careers.walmart.com/results?q=&page=1&sort=date&jobCategory=00000161-7bad-da32-a37b'
                   '-fbef5e390000&expand=department,brand,type,rate&type=jobs')  # opens the website

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.search__results")))

        out_div = driver.find_elements(By.CSS_SELECTOR, 'div.search__results')
        in_ul = out_div[0].find_element(By.TAG_NAME,'ul')
        lis = in_ul.find_elements(By.TAG_NAME,'li')
        bot.send_message(message.chat.id, text='Walmart')
        for i in lis:
            date = i.find_element(By.CLASS_NAME,'job-listing__created').text
            if(int(str(today - datetime.strptime(date, "%m/%d/%y").date()).split(" ")[0])<3):
                link = i.find_element(By.CLASS_NAME,'job-listing__link').get_attribute('href')
                bot.send_message(message.chat.id, text=link)
        time.sleep(end_delay)

        # driver.quit()
    finally:
        bot.send_message(message.chat.id, text='No jobs in Walmart or Error')
    #
    # IBM
    #
    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)
        #
        # Data Science
        driver.get('https://www.ibm.com/careers/us-en/search/?filters=department:Data%20%26%20Analytics,level:Entry%20Level,primary_country:US')
        # Software
        # driver.get'https://www.ibm.com/careers/us-en/search/?filters=department:Software%20Engineering,level:Entry%20Level,primary_country:US')

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "bx--card__wrapper")))
        lis = driver.find_elements(By.CLASS_NAME, 'bx--card__wrapper')
        bot.send_message(message.chat.id, text='IBM')
        garbage_links = ['https://www.ibm.com/careers/uk-en/search/?filters=primary_country:DZ,primary_country:AT,'
                         'primary_country:BE,primary_country:BG,primary_country:HR,primary_country:CY,primary_country:CZ,'
                         'primary_country:DK,primary_country:EG,primary_country:FI,primary_country:FR,primary_country:DE,'
                         'primary_country:GH,primary_country:GR,primary_country:HU,primary_country:IE,primary_country:IL,'
                         'primary_country:IT,primary_country:KE,primary_country:LV,primary_country:LT,primary_country:MA,'
                         'primary_country:NL,primary_country:NG,primary_country:NO,primary_country:PK,primary_country:PL,'
                         'primary_country:PT,primary_country:QA,primary_country:RO,primary_country:SA,primary_country:RS,'
                         'primary_country:SK,primary_country:SI,primary_country:ZA,primary_country:ES,primary_country:SE,'
                         'primary_country:CH,primary_country:TN,primary_country:TR,primary_country:AE,primary_country:GB,'
                         'department:Data%20%26%20Analytics,level:Entry%20Level',
                         'https://www.ibm.com/careers/cn-zh/search/?filters=primary_country:CN,primary_country:HK,'
                         'primary_country:TW,department:Data%20%26%20Analytics,level:Entry%20Level',
                         'https://www.ibm.com/careers/br-pt/search/?filters=primary_country:AR,primary_country:BR,'
                         'primary_country:CL,primary_country:CO,primary_country:CR,primary_country:EC,primary_country:MX,'
                         'primary_country:PE,primary_country:UY,primary_country:VE,department:Data%20%26%20Analytics,'
                         'level:Entry%20Level',
                         'https://www.ibm.com/careers/ph-en/search/?filters=primary_country:AU,primary_country:ID,'
                         'primary_country:JP,primary_country:MY,primary_country:NZ,primary_country:PH,primary_country:SG,'
                         'primary_country:KR,primary_country:TH,primary_country:VN,department:Data%20%26%20Analytics,'
                         'level:Entry%20Level',
                         'https://www.ibm.com/careers/in-en/search/?filters=primary_country:BD,primary_country:IN,'
                         'primary_country:LK,department:Data%20%26%20Analytics,level:Entry%20Level',
                         'https://www.ibm.com/careers/us-en/search/?filters=primary_country:CA,primary_country:US,'
                         'department:Data%20%26%20Analytics,level:Entry%20Level']
        if len(lis) > 0:
            for i in lis:
                link = i.find_element(By.XPATH, './div/a').get_attribute('href')
                if link not in garbage_links:
                    bot.send_message(message.chat.id, text=link)
                    # print(link)
        time.sleep(end_delay)

        # driver.quit()
    finally:
        bot.send_message(message.chat.id, text='No jobs in IBM or Error')

    # Amazon
    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        # Software
        # driver.get('https://www.amazon.jobs/en/job_categories/software-development?offset=0&result_limit=10&sort=relevant&job_type%5B%5D=Full-Time&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&')
        # Data Science
        driver.get('https://www.amazon.jobs/en/job_categories/data-science?offset=0&result_limit=10&sort=relevant'
                   '&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query'
                   '=&base_query=&city=&country=&region=&county=&query_options=&')

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "job-tile")))
        lis = driver.find_elements(By.CLASS_NAME, 'job-tile')

        bot.send_message(message.chat.id, text='Amazon')
        if len(lis) > 0:
            for i in lis:
                update = i.find_element(By.XPATH, './a/div/div[1]/div[2]/p').text
                if 'days' in update.split(" "):
                    days = int(update.split(" ")[1])
                    if days < 3:
                        link = i.find_element(By.XPATH, './a').get_attribute('href')
                        bot.send_message(message.chat.id, text=link)
                        # print(link)
        time.sleep(end_delay)

        # driver.quit()
    finally:
        bot.send_message(message.chat.id, text='No jobs in Amazon or Error')

    # Bloomberg
    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        driver.get('https://careers.bloomberg.com/job/search?el=Students+and+Recent+Graduates&lc=New+York')

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/main/div/div[3]/div/div/div/div[2]/div[2]")))

        out_div = driver.find_element(By.XPATH, '/html/body/div[7]/main/div/div[3]/div/div/div/div[2]/div[2]')
        lis = out_div.find_elements(By.CLASS_NAME, 'job-results-section')

        bot.send_message(message.chat.id, text='Bloomberg')
        if len(lis) > 0:
            for i in lis:
                days = int(str(today - datetime.strptime('Aug 17, 2022', "%b %d, %Y").date()).split(" ")[0])
                if days < 3:
                    link = i.find_element(By.XPATH, './div/a').get_attribute('href')
                    bot.send_message(message.chat.id, text=link)
                    # print(link)
        time.sleep(end_delay)

        driver.quit()
    finally:
        bot.send_message(message.chat.id, text='No jobs in Bloomberg or Error')
        driver.quit()


bot.infinity_polling()