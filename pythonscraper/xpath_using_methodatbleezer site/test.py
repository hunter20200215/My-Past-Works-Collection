import time
import pickle
import selenium.webdriver 
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from flask import jsonify
import json
import requests

default_timeout = 50

driver = selenium.webdriver.Chrome()
driver.get("https://www.deezer.com")



driver.implicitly_wait(default_timeout)

def write_cookie(username, cookie):
    # cookie = base64.b64encode(json.dumps(cookie))
    # data=f'''{{
    #     "user": "{username}",
    #     "cookie": "{cookie}"
    # }}
    # '''
    data = {"user": username, "cookie": cookie}
    api_endpoint = 'http://127.0.0.1:5000/api/cookie/update'
    response = requests.post(api_endpoint, data=data)
    return True
    

def get_login_data():
    
    data='''{

    }
    '''
    api_endpoint = 'http://127.0.0.1:5000/api/user/random'
    response = requests.get(api_endpoint, data=data)
    data = json.load(response.text)
    data.cookie =  json.load(base64.b64decode(data.cookie))

loginData = get_login_data()

user_name = loginData.username
user_pwd = loginData.password
cookie_file = loginData.cookie

# load cookie {
try:
    cookies = pickle.load(open(cookie_file, "rb"))
except:
    cookies = []

for cookie in cookies:
    # print(cookie)
    if 'expiry' in cookie:
        del cookie['expiry']
    driver.add_cookie(cookie)

#return True if not logged in
def is_loggedin():
    ret = True
    driver.get("https://www.deezer.com/en")
    try:
        driver.implicitly_wait(50)
        driver.find_element_by_id('page_topbar')
        print ("you have login cookie now,so you don't need to login again")
    except:
        ret = False
    driver.implicitly_wait(default_timeout)
    return ret

# } end of cookie load


#test if logged in

if not is_loggedin() :

    
    driver.find_element_by_id('topbar-login-button').click()
        # driver.get("https://www.deezer.com/us/login")
    driver.implicitly_wait(5)
    login_email=driver.find_element_by_id('login_mail')
    login_email.send_keys(username)
    login_password=driver.find_element_by_id('login_password')
    login_password.send_keys("password215")

    driver.find_element_by_id('login_form_submit').click()
    print ("logging in...")
    driver.implicitly_wait(100)
    driver.find_element_by_id('page_topbar')
    driver.implicitly_wait(default_timeout)
    # save cookie
    # pickle.dump( driver.get_cookies() , open(cookie_file,"wb"))
    cookie = json.dumps(driver.get_cookies())
    write_cookie(user_name, cookie)

print('now you are logged in')


#=============================   =================
search_box = driver.find_element_by_css_selector('input.topbar-search-input')
with open('playlist.csv', 'r') as csvfile:
    # reader = csv.reader(file)
    obj = csv.reader(csvfile, skipinitialspace=True)
    # obj = csv.reader(file)
    next(obj)
    print(obj)
    my_playlist_name="New_Play_List_For_Me"
    #Create playlist name
    Create_play_list_name=driver.find_element_by_xpath('//*[@id="page_sidebar"]/div[2]/div[3]/ul/li[5]/a')
    Create_play_list_name.click()
    Create_play_list_name_click=driver.find_element_by_xpath('//*[@id="page_profile"]/div[2]/div/div/section/div[2]/ul/li[1]/button')
    Create_play_list_name_click.click()
    Add_playlist_createnew_Title=driver.find_element_by_xpath('//*[@id="modal_playlist_assistant"]/div/div[2]/div[1]/div/input')
    driver.execute_script("arguments[0].click();", Add_playlist_createnew_Title)
    Add_playlist_createnew_Title.send_keys(Keys.CONTROL, "a")
    Add_playlist_createnew_Title.send_keys(my_playlist_name)
    # driver.execute_script("arguments[0].click();", Add_playlist_createnew_Title)
    time.sleep(5)
    #run submit
    Add_playlist_createnew_Title=driver.find_element_by_xpath('//*[@id="modal_playlist_assistant_submit"]/span')
    driver.execute_script("arguments[0].click();", Add_playlist_createnew_Title)
    time.sleep(5)







    for row in obj:
        if len(row[0])==0:
            continue
        art_name = row[0] #"Paul Mumford"
        abm_name=row[1] #"sunrise"
        driver.implicitly_wait(15)
        search_box = driver.find_element_by_css_selector('input.topbar-search-input')
        search_box.send_keys(art_name+' '+abm_name)
        search_box.send_keys(Keys.ENTER)
        driver.implicitly_wait(50)
        el = driver.find_element_by_css_selector('.picture.picture-link.no-background')
        driver.execute_script("arguments[0].click();", el, 10)    #alert(arguments[1])
        #wait for ajax
        time.sleep(10)
        Add_playlist_1=driver.find_element_by_css_selector('input.checkbox-input')
        driver.execute_script("arguments[0].click();", Add_playlist_1)
        # 1. save something  or enlist to playst
        # 2. sleep(3)
        # goto search again
        time.sleep(8)
        Add_playlist_2=driver.find_element_by_xpath('//*[@id="page_naboo_album"]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/button/span[2]')

        # Add_playlist_2=driver.find_element_by_css_selector('button.c031 c0310')[3]
        driver.execute_script("arguments[0].click();", Add_playlist_2)
        time.sleep(15)



        #click the add the list
        search_results=driver.find_elements_by_css_selector('button.menu-item')[4]
        driver.execute_script("arguments[0].click();", search_results)
        time.sleep(18)
        


#        driver.implicitly_wait(150)

    print("done")