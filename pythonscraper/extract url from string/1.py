  
import csv
import sys
import re
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import InvalidArgumentException

from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver

import requests
from bs4 import BeautifulSoup



import time

output_file = 'Apartments_Information.csv'


def add_csv_head():
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Price', 'Description', 'Value_Bathrooms', 'Valuse_Bedrooms', 'Parking', 'Image_1', 'Image_2', 'Image_3'])

def add_csv_row(title, price, description, bathrooms, bedrooms, parking, img_1, img_2, img_3):
    # print("-----33--------")
    # print(jobs_category)
    with open(output_file, 'a', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([title, price, description, bathrooms, bedrooms, parking, img_1, img_2, img_3])

# def setUpChrome():
#     global driver
#     # Using Chrome
#     chrome_options = webdriver.ChromeOptions()
#     #prefs = {"profile.managed_default_content_settings.images": 2}
#     #chrome_options.add_experimental_option("prefs", prefs)
#     chrome_options.add_argument('--ignore-certificate-errors')
#     chrome_options.add_argument('--ignore-ssl-errors')
#     #chrome_options.add_argument('headless')

#     scriptpath = os.path.realpath(__file__)
#     foldername = os.path.basename(scriptpath)
#     scriptpath = scriptpath[:scriptpath.find(foldername)]

#     scriptpath += 'chromedriver'

#     driver = webdriver.Chrome(scriptpath, chrome_options=chrome_options)
#     return driver

add_csv_head()
driver = selenium.webdriver.Chrome()
# driver.maximize_window()
base_url = 'https://www.olx.com.gt/departamentos-casas-en-venta_c367#loginemailcreatepassword'




# driver = setUpChrome()

driver.get(base_url)
time.sleep(5)
driver.implicitly_wait(50)
i = 1
while i < 1:
    driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]').click()
    i += 1
    
    driver.implicitly_wait(50)
    time.sleep(3)

# page1 = requests.get(base_url)


# soup1 = BeautifulSoup(page1.content, 'html.parser')



urls=driver.find_elements_by_xpath('//*[@data-aut-id="itemBox"]/a[@href]')
time.sleep(5)
driver.implicitly_wait(20)
# print(urls)
stored_urls = [];
for url in urls:

    
    # time.sleep(1)

    # print(b.get_attribute("href"))
    
    b_url=url.get_attribute('href')
    stored_urls.append(b_url)
    # time.sleep(1)

for url_var in stored_urls:

    driver.get(url_var)
    
    print(url_var)
    # time.sleep(9)

    driver.implicitly_wait(50)
    time.sleep(8)
    title_pre=driver.find_element_by_xpath("//*[@data-aut-id='itemTitle']").text
    title = title_pre.replace(',', '')

    price_pre=driver.find_element_by_xpath("//*[@data-aut-id='itemPrice']").text
    price = price_pre.replace(',', '')
    description_pre=driver.find_element_by_xpath('//div[@data-aut-id="itemDescriptionContent"]').text
    description = description_pre.replace(',', '')
    bathrooms=driver.find_element_by_xpath('//span[@data-aut-id="value_bathrooms"]').text
    time.sleep(1)
    bedrooms=driver.find_element_by_xpath('//span[@data-aut-id="value_bedrooms"]').text
    parking=driver.find_element_by_xpath('//span[@data-aut-id="value_parking"]').text
    time.sleep(1)
    image1=driver.find_elements_by_xpath('//div[@class="_2YABR"]/button')[1]
    img1_src=image1.get_attribute("style")
    img_1=re.search("(?P<url>https?://[^\s\;]+)", img1_src).group("url")
    print(img_1)
    # img_1 = img_1[1]
    
    # img_1=img1_src.replace("'","")
    try:
        image2=driver.find_elements_by_xpath('//div[@class="_2YABR"]/button')[2]
        img2_src=image2.get_attribute("style")
        img_2=re.search("(?P<url>https?://[^\s\;]+)", img2_src).group("url")
    except:
        img_2="N/A"
        # img_2 = img_2[1]
    
    try:
        image3=driver.find_elements_by_xpath('//div[@class="_2YABR"]/button')[3]
        img3_src=image2.get_attribute("style")
        img_3=re.search("(?P<url>https?://[^\s\;]+)", img3_src).group("url")
    except:
        img_3="N/A"
    # img_2 = img_2[1]
    

    # image4=driver.find_elements_by_xpath('//div[@class="_2YABR"]/button')[4]
    # img4_src=image4.get_attribute("style")
    # img_4=re.search("(?P<url>https?://[^\s\;]+)", img4_src).group("url")
    # # img_2 = img_2[1]
    


    # image5=driver.find_elements_by_xpath('//div[@class="_2YABR"]/button')[5]
    # img5_src=image5.get_attribute("style")
    # img_5=re.search("(?P<url>https?://[^\s\;]+)", img5_src).group("url")
    #     # img_2 = img_2[1]
        
        # img_srcs=[]
        # for insert in images:
        #     img_src=insert.get_attribute("src")
        #     pp
        #     img_srcs.append(img_src)
        #     print(img_srcs)
        
        





    add_csv_row(title, price, description, bathrooms, bedrooms, parking, img_1, img_2, img_3)
    
        



print("done")