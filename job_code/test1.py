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

not_interested_roles = [ 'principal', 'Executive', 'staff', 'director', 'software', 'devops', 'manager']

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    # Walmart
    PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver" # Path to chromedriver
    driver=webdriver.Chrome(PATH)
    try:
        driver.get('https://careers.walmart.com/results?q=Data%20Analytics&page=1&sort=date&jobCategory=00000161-7bad'
                   '-da32-a37b-fbef5e390000,00000159-7627-d286-a3f9-7ea7d10c0000&expand=department,'
                   '0000015e-b97d-d143-af5e-bd7da8ca0000,00000159-7574-d286-a3f9-7ff45f640000,brand,type,'
                   'rate&type=jobs')  # opens the website
        time.sleep(3)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.search__results")))
        out_div = driver.find_elements(By.CSS_SELECTOR, 'div.search__results')
        in_ul = out_div[0].find_element(By.TAG_NAME,'ul')
        lis = in_ul.find_elements(By.TAG_NAME,'li')
        bot.send_message(message.chat.id, text='Walmart')

        for i in lis:
            date = i.find_element(By.CLASS_NAME,'job-listing__created').text
            days = str(today - datetime.strptime(date, "%m/%d/%y").date()).split(" ")[0]
            if days == '0:00:00':
                days = 0
            if int(days) < 2:
                link = i.find_element(By.CLASS_NAME,'job-listing__link').get_attribute('href')
                desc = i.find_element(By.CLASS_NAME,'job-listing__link').text.lower()
                bot.send_message(message.chat.id, text=link)
        time.sleep(end_delay)

        # driver.quit()
    except:
        bot.send_message(message.chat.id, text='No jobs in Walmart or Error')

    # Walmart Workday
    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        driver.get('https://walmart.wd5.myworkdayjobs.com/WalmartExternal?jobFamilyGroup'
                   '=e83ebdbd2a0a01af0185848948e94dc6&locationCountry=bc33aa3152ec42d4995f4791a106ed09'
                   '&Management_Level=3110e91abc930181e556e10099e7850c&Management_Level'
                   '=3110e91abc930151aec9d30399e7860c')

        bot.send_message(message.chat.id, text='Walmart Workday')
        time.sleep(end_delay)

        # driver.quit()
    except:
        bot.send_message(message.chat.id, text='No jobs in Walmart Workday or Error')
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
        garbage_links = ['https://www.ibm.com/careers/cn-zh/search/?filters=primary_country:CN,primary_country:HK,'
                         'primary_country:TW,department:Data%20%26%20Analytics,level:Entry%20Level',
                         'https://www.ibm.com/careers/br-pt/search/?filters=primary_country:AR,primary_country:BR,'
                         'primary_country:CL,primary_country:CO,primary_country:CR,primary_country:EC,'
                         'primary_country:MX,primary_country:PE,primary_country:UY,primary_country:VE,'
                         'department:Data%20%26%20Analytics,level:Entry%20Level',
                         'https://www.ibm.com/careers/ph-en/search/?filters=primary_country:AU,primary_country:ID,'
                         'primary_country:JP,primary_country:MY,primary_country:NZ,primary_country:PH,'
                         'primary_country:SG,primary_country:KR,primary_country:TH,primary_country:VN,'
                         'department:Data%20%26%20Analytics,level:Entry%20Level',
                         'https://www.ibm.com/careers/in-en/search/?filters=primary_country:BD,primary_country:IN,'
                         'primary_country:LK,department:Data%20%26%20Analytics,level:Entry%20Level',
                         'https://www.ibm.com/careers/us-en/search/?filters=primary_country:CA,primary_country:US,'
                         'department:Data%20%26%20Analytics,level:Entry%20Level',
                         'https://www.ibm.com/careers/uk-en/search/?filters=primary_country:DZ,primary_country:AT,'
                         'primary_country:BE,primary_country:BG,primary_country:HR,primary_country:CY,'
                         'primary_country:CZ,primary_country:DK,primary_country:EG,primary_country:FI,'
                         'primary_country:FR,primary_country:DE,primary_country:GH,primary_country:GR,'
                         'primary_country:HU,primary_country:IE,primary_country:IL,primary_country:IT,'
                         'primary_country:KE,primary_country:LV,primary_country:LT,primary_country:MA,'
                         'primary_country:NL,primary_country:NG,primary_country:NO,primary_country:PK,'
                         'primary_country:PL,primary_country:PT,primary_country:QA,primary_country:RO,'
                         'primary_country:SA,primary_country:RS,primary_country:SK,primary_country:SI,'
                         'primary_country:ZA,primary_country:ES,primary_country:SE,primary_country:CH,'
                         'primary_country:TN,primary_country:TR,primary_country:AE,primary_country:GB,'
                         'department:Data%20%26%20Analytics,level:Entry%20Level',
                         'https://www.ibm.com/careers/uk-en/search/?filters=primary_country:DZ,primary_country:AT,'
                         'primary_country:BE,primary_country:BG,primary_country:HR,primary_country:CY,'
                         'primary_country:CZ,primary_country:DK,primary_country:EG,primary_country:FI,'
                         'primary_country:FR,primary_country:DE,primary_country:GH,primary_country:GR,'
                         'primary_country:HU,primary_country:IE,primary_country:IL,primary_country:IT,'
                         'primary_country:KE,primary_country:LV,primary_country:LT,primary_country:MA,'
                         'primary_country:NL,primary_country:NG,primary_country:NO,primary_country:PK,'
                         'primary_country:PL,primary_country:PT,primary_country:QA,primary_country:RO,'
                         'primary_country:SA,primary_country:RS,primary_country:SK,primary_country:SI,'
                         'primary_country:ZA,primary_country:ES,primary_country:SE,primary_country:CH,'
                         'primary_country:TN,primary_country:TR,primary_country:AE,primary_country:GB',
                         'https://www.ibm.com/careers/ja-jp/search/?filters=primary_country:AU,primary_country:ID,'
                         'primary_country:JP,primary_country:MY,primary_country:NZ,primary_country:PH,'
                         'primary_country:SG,primary_country:KR,primary_country:TH,primary_country:VN,'
                         'department:Data%20%26%20Analytics,level:Entry%20Level '
                         ]
        if len(lis) > 0:
            for i in lis:
                link = i.find_element(By.XPATH, './div/a').get_attribute('href')
                if link not in garbage_links:
                    bot.send_message(message.chat.id, text=link)
                    # print(link)
        time.sleep(end_delay)

        # driver.quit()
    except:
        bot.send_message(message.chat.id, text='No jobs in IBM or Error')

    # Amazon
    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        # Software
        # driver.get('https://www.amazon.jobs/en/job_categories/software-development?offset=0&result_limit=10&sort=relevant&job_type%5B%5D=Full-Time&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&')
        # Data Science
        driver.get('https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&category%5B%5D=data'
                   '-science&category%5B%5D=database-administration&category%5B%5D=business-intelligence&category%5B'
                   '%5D=machine-learning-science&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude'
                   '=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&')
        bot.send_message(message.chat.id, text='Amazon')
        page_num = 1

        while True:
            time.sleep(2)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "job-tile")))
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[1]/div[3]/div/div/div["
                                                         "2]/content/div/div/div[2]/div[3]/div[1]/div/div")))

            page_out_div = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[3]/div/div/div['
                                                        '2]/content/div/div/div[2]/div[3]/div[1]/div/div')
            page_lis = page_out_div.find_elements(By.XPATH, './*')

            lis = driver.find_elements(By.CLASS_NAME, 'job-tile')

            if len(lis) > 0:
                for i in lis:
                    update = i.find_element(By.XPATH, './a/div/div[1]/div[2]/p').text
                    # print(update)
                    if 'day' in update.split(" "):
                        days = int(update.split(" ")[1])
                        if days < 3:
                            link = i.find_element(By.XPATH, './a').get_attribute('href')
                            bot.send_message(message.chat.id, text=link)
                            # print(link)
                    elif 'hours' in update.split(" "):
                        link = i.find_element(By.XPATH, './a').get_attribute('href')
                        bot.send_message(message.chat.id, text=link)
                        # print(link)

            flag = 0
            for x in page_lis:
                txt = x.text
                # print(txt)
                if (txt not in [""]):
                    if (int(txt) == page_num + 1):
                        x.click()
                        page_num = page_num + 1
                        flag = 1
                        break
            if flag == 0:
                break
        time.sleep(end_delay)

        # driver.quit()
    except:
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
                date = i.find_element(By.XPATH, './span[1]').text
                days = int(str(today - datetime.strptime(date, "%b %d, %Y").date()).split(" ")[0])
                if days < 3:
                    link = i.find_element(By.XPATH, './div/a').get_attribute('href')
                    bot.send_message(message.chat.id, text=link)
                    # print(link)
        time.sleep(end_delay)

        # driver.quit()
    except:
        bot.send_message(message.chat.id, text='No jobs in Bloomberg or Error')


    # Q2 Workday
    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        driver.get('https://q2ebanking.wd5.myworkdayjobs.com/Q2?locations=0da4bb96663010308829a8dfd4e91994&locations'
                   '=3b54c7e3a94801ec9b86115c1c017e76&jobFamilies=8b86f00a4a2a0161c8f6dbdc0288ab6a&jobFamilies'
                   '=8b86f00a4a2a01e03cacfbdc0288b96a&jobFamilies=54838d87026b0142d4a0dd78070250f5')

        bot.send_message(message.chat.id, text='Q2')

        links = workday(driver, message)

        time.sleep(end_delay)

        # driver.quit()
    except:
        bot.send_message(message.chat.id, text='No jobs in Q2 or Error')

    # Dell Workday
    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        driver.get('https://dell.wd1.myworkdayjobs.com/en-US/External?Location_Country=bc33aa3152ec42d4995f4791a106ed09')

        bot.send_message(message.chat.id, text='Dell')

        links = workday(driver,message)

        time.sleep(end_delay)

        # driver.quit()
    except:
        bot.send_message(message.chat.id, text='No jobs in Dell or Error')

    # Salesforce Workday
    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        driver.get('https://salesforce.wd1.myworkdayjobs.com/en-US/External_Career_Site?Location_Country' 
               '=bc33aa3152ec42d4995f4791a106ed09&jobFamilyGroup=79e9552bbdbe454a8e1dbdd652b00e38 ')

        bot.send_message(message.chat.id, text='Salesforce')
        links = workday(driver,message)
        time.sleep(end_delay)

        # driver.quit()
    except:
        bot.send_message(message.chat.id, text='No jobs in Salesforce or Error')

    # Fractal Analytics Workday
    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        driver.get(
            'https://fractal.wd1.myworkdayjobs.com/en-US/Careers?locations=4fedd31659ec01018833777a30190000&locations'
            '=4fedd31659ec0101883361ab95b30000&locations=4fedd31659ec010188338b7607d90000&locations'
            '=4fedd31659ec010188338394e39e0000&locations=4fedd31659ec0101883389a4705c0000&locations'
            '=4fedd31659ec0101883384cb0be80000')

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[4]/div/div/div[2]/section")))
        time.sleep(2)

        bot.send_message(message.chat.id, text='Fractal Analytics')

        page_out_div = driver.find_element(By.XPATH, '/html/body/div/div/div/div[4]/div/div/div[2]/section/div[2]')
        page_lis = page_out_div.find_elements(By.CLASS_NAME, 'css-1j096s0')
        page_num = 1

        while page_num <= len(page_lis):

            page_num_button = page_lis[page_num - 1].find_element(By.XPATH, './button')
            page_num_button.click()

            time.sleep(5)

            out_div = driver.find_element(By.XPATH, '/html/body/div/div/div/div[4]/div/div/div[2]/section')
            lis = out_div.find_elements(By.CLASS_NAME, 'css-1q2dra3')
            # print(lis)
            if len(lis) > 0:
                for i in lis:
                    days = i.find_element(By.XPATH, './div[3]/div/div/dl/dd').text.split(" ")[1]
                    if days == 'Today':
                        days = 0
                    elif days == 'Yesterday':
                        days = 1
                    if days != '30+':
                        days = int(days)
                        if days < 2:
                            link = i.find_element(By.XPATH, './div[1]/div/div/h3/a').get_attribute('href')
                            bot.send_message(message.chat.id, text=link)
                            # print(link)

            page_num = page_num + 1

        time.sleep(end_delay)

        # driver.quit()
    except:
        bot.send_message(message.chat.id, text='No jobs in Fractal Analytics or Error')

    # Tiger Analytics
    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        driver.get(
            'https://www.tigeranalytics.com/current-openings/#us')

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "whr-item")))

        bot.send_message(message.chat.id, text='Tiger Analytics')

        lis = driver.find_elements(By.CLASS_NAME, 'whr-item')

        for i in lis:
            date = i.find_element(By.CLASS_NAME, 'whr-date').text.split(" ")[2]
            days = int(str(today - datetime.strptime(date, "%Y-%m-%d").date()).split(" ")[0])
            # print(days)
            if days < 3:
                link = i.find_element(By.XPATH, './h3/a').get_attribute('href')
                bot.send_message(message.chat.id, text=link)
                # print(link)

        time.sleep(end_delay)

        # driver.quit()
    except:
        bot.send_message(message.chat.id, text='No jobs in Tiger Analytics or Error')

    # CVS

    try:

        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        # Open the website
        driver.get('https://jobs.cvshealth.com/job-search-results/?addtnl_categories[]=Analytics&addtnl_categories['
                   ']=Business%20Analyst&addtnl_categories[]=Data%20Engineering&addtnl_categories['
                   ']=Enterprise%20Analytics&addtnl_categories['
                   ']=Health%20Care%20Analytics&location=United%20States&country=US&radius=25')

        bot.send_message(message.chat.id, text='CVS') # Send the company name to bot

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pagination-li"))) # Wait till the page numbers load

        # click okay for the cokkie element
        cokkie_element = driver.find_element(By.CSS_SELECTOR, 'div.cookie-notice-container')
        cokkie_element.find_element(By.XPATH, './a').click()

        # Load the old job ids
        with open("cvs_job_id.txt") as f:
            old_job_id = f.readlines()
        old_job_id = [x.strip() for x in old_job_id]  # remove new line characters
        # print(old_job_id)
        # old_job_id = []

        new_job_id = []
        page_num = 1
        # Iterate through pages
        while True:
            time.sleep(2)
            # Waits for loading page numbers and job list
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/main/div/section/div/div/div[2]/div/div[2]/div/div/div[1]/div[5]/div[2]")))
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pagination-li")))

            # Load the page numbers
            page_lis = driver.find_elements(By.CLASS_NAME, 'pagination-li')

            # Load the job list
            out_div = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/main/div/section/div/div/div[2]/div/div[2]/div/div/div[1]/div[5]/div[2]')
            lis = out_div.find_elements(By.XPATH, './div/*')

            for i in lis:
                job_id = i.find_element(By.XPATH, "./div/div[2]").text
                # print(job_id)
                new_job_id.append(job_id)
                if job_id not in old_job_id:
                    link = i.find_element(By.XPATH, './div/span[5]/a').get_attribute('href')
                    bot.send_message(message.chat.id, text=link)
                    # print(link)

            # Iterate through the pages
            flag = 0
            for x in page_lis:
                txt = x.find_element(By.XPATH, './a').text
                # print(txt)
                if (txt not in ["<<", "<", ">", ">>"]):
                    if (int(txt) == page_num + 1):
                        x.find_element(By.XPATH, './a').click()
                        page_num = page_num + 1
                        flag = 1
                        break
            if flag == 0:
                break

        # open file to write the new job ids
        with open(r'cvs_job_id.txt', 'w') as fp:
            for item in new_job_id:
                # write each item on a new line
                fp.write("%s\n" % item)

        time.sleep(end_delay) # end delay
        # driver.quit()

    except:
        bot.send_message(message.chat.id, text='No jobs in CVS or Error')

    # Fidelity

    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        # Opens the website
        driver.get('https://jobs.fidelity.com/job-search-results/?parent_category['
                   ']=Business%20Analysis%20%26%20Project%20Management&parent_category[]=Technology')

        bot.send_message(message.chat.id, text='Fidelity') # Sends the comapny name to bot

        page_num = 1
        days = 0

        # Iterate through the pages untill the jobs are less than 2 days old
        while int(days) < 3:
            time.sleep(2)
            # Waits for loading page numbers and job llist
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/main/div/section/div/div/div/div"
                                                         "/div[2]/div/div[2]/div[1]/div[5]/div[2]")))
            page_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pagination-li")))

            # Load the page numbers
            page_lis = driver.find_elements(By.CLASS_NAME, 'pagination-li')
            # Loads the job list
            out_div = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/main/div/section/div/div/div/div/div['
                                                   '2]/div/div[2]/div[1]/div[5]/div[2]')
            in_div = out_div.find_element(By.XPATH, './div')
            lis = in_div.find_elements(By.XPATH, './*')

            # iterate through the jobs
            if len(lis) > 0:
                for i in lis:
                    date = i.find_element(By.XPATH, './div/div[4]').text
                    days = str(today - datetime.strptime(date, "%m/%d/%Y").date()).split(" ")[0]
                    if days == '0:00:00':
                        days = 0
                    if int(days) < 2:
                        link = i.find_element(By.XPATH, './div/div[1]/div[2]/a').get_attribute('href')
                        bot.send_message(message.chat.id, text=link)
                        # print(link)

            # Iterate through the pages
            flag = 0
            for x in page_lis:
                txt = x.text
                # print(txt)
                if (txt not in ["<<", "<", ">", ">>"]):
                    if (int(txt) == page_num + 1):
                        x.click()
                        page_num = page_num + 1
                        flag = 1
                        break
            if flag == 0:
                break

        time.sleep(end_delay) # End delay

        # driver.quit()

    except:
        bot.send_message(message.chat.id, text='No jobs in Fidelity or Error')

    # Veeva systems

    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        # Opens the website
        driver.get('https://careers.veeva.com/job-search-results/?primary_category[]=Engineering&primary_category['
                   ']=Analytics&store_id[]=USA')

        bot.send_message(message.chat.id, text='Veeva Systems') # Sends company name to bot

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/main/div/section/div/div/div["
                                                     "2]/div/div[2]/div/div[2]/div[1]/div[5]/div[2]")))
        time.sleep(2)

        # Loading the list
        out_div = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/main/div/section/div/div/div[2]/div/div['
                                               '2]/div/div[2]/div[1]/div[5]/div[2]')
        in_div = out_div.find_element(By.XPATH, './div')
        lis = in_div.find_elements(By.XPATH, './*')

        # not interested roles in veeva
        not_interested_roles_veeva = not_interested_roles + ["ui architect", "performance engineer"]

        if len(lis) > 0:
            for i in lis:
                link = i.find_element(By.XPATH, './div/div[1]/div[2]/a').get_attribute('href')
                desc = i.find_element(By.XPATH, './div/div[1]/div[2]/a').text
                desc_flag = [True for x in not_interested_roles_veeva if x in desc.lower()]
                if not desc_flag:
                    bot.send_message(message.chat.id, text=link)
                    # print(link)
        time.sleep(end_delay)  # End delay

        # driver.quit()

    except:
        bot.send_message(message.chat.id, text='No jobs in Veeva Systems or Error')

    # HP Workday
    try:
        # PATH = r"/Users/dheeraj/Desktop/jobs/chromedriver"  # Path to chromedriver
        # driver = webdriver.Chrome(PATH)

        driver.get('https://hp.wd5.myworkdayjobs.com/en-US/ExternalCareerSite?jobFamilyGroup'
                   '=80667f5f2da3010ee8417a74cf4b0000&primaryLocation=336ea9b27e9910b218bde597c1cae4b1'
                   '&primaryLocation=336ea9b27e9910b21b37a49ec9e0725f&primaryLocation'
                   '=336ea9b27e9910b217ab53dd5681a42e&primaryLocation=336ea9b27e9910b217693377d05b94b1'
                   '&primaryLocation=b13b454d0dd401d06042e8aee55606df&primaryLocation'
                   '=336ea9b27e9910b2181a3b76b70ec00d&primaryLocation=336ea9b27e9910b2183d59b62c3bc71f'
                   '&primaryLocation=336ea9b27e9910b217873cdbde859b4d&primaryLocation'
                   '=336ea9b27e9910b2174ae17110848eed&primaryLocation=5d264c5c066b01738fcee5d220195366'
                   '&primaryLocation=5d264c5c066b012403c58bd220194566&primaryLocation'
                   '=5d264c5c066b01cbe077a3d02019d565&primaryLocation=5d264c5c066b019422065fcd20191a65')

        bot.send_message(message.chat.id, text='HP')
        links = workday(driver, message)
        time.sleep(end_delay)

        driver.quit()
    except:
        bot.send_message(message.chat.id, text='No jobs in HP or Error')
        driver.quit()


def workday(driver,message):

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[2]/section")))
    time.sleep(2)

    page_out_div = driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/div/div/div[2]/section/div[2]')
    page_lis = page_out_div.find_elements(By.CLASS_NAME, 'css-1j096s0')
    page_num = 1

    while page_num <= len(page_lis):

        page_num_button = page_lis[page_num - 1].find_element(By.XPATH, './button')
        page_num_button.click()

        time.sleep(5)

        out_div = driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/div/div/div[2]/section')
        lis = out_div.find_elements(By.CLASS_NAME, 'css-1q2dra3')
        links = []
        if len(lis) > 0:
            for i in lis:
                days = i.find_element(By.XPATH, './div[3]/div/div/dl/dd').text.split(" ")[1]
                if days == 'Today':
                    days = 0
                elif days == 'Yesterday':
                    days = 1
                if days != '30+':
                    days = int(days)
                    if days < 3:
                        link = i.find_element(By.XPATH, './div[1]/div/div/h3/a').get_attribute('href')
                        bot.send_message(message.chat.id, text=link)
                        # print(link)

        page_num = page_num + 1


bot.infinity_polling()