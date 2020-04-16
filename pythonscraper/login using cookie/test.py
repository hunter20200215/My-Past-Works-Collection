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

def write_cookie(username, cookie):

    data = {"user": username, "cookie": cookie}
    # print(json.dumps(data))
    api_endpoint = 'http://127.0.0.1:5000/api/cookie/update'
    # response = requests.post(api_endpoint, data=data_in_string, headers = {'content-type': 'application/json'})
    # response = requests.post(api_endpoint, data=data, headers = {'Content-Type': 'application/json'})
    response = requests.post(api_endpoint, json=data)
    print(response.text)
    return True
    


def get_login_data():
    
    data='''{

    }
    '''
    api_endpoint = 'http://127.0.0.1:5000/api/user/random'
    response = requests.get(api_endpoint, data=data)
    return response.json()

loginData = get_login_data()

user_name = loginData['username']
user_pwd = loginData['password']
cookies = loginData['cookie']
playlist = loginData['playlist']
Time_to_play = loginData['time_to_play_for']
print(playlist)
print(Time_to_play)



driver = selenium.webdriver.Chrome()
driver.get("https://www.deezer.com")
driver.implicitly_wait(default_timeout)

for cookie in cookies:
    # print(cookie)
    if 'expiry' in cookie:
        del cookie['expiry']
    try:
        driver.add_cookie(cookie)
    except:
        a =1
#return True if not logged in
def is_loggedin():
    ret = True
    driver.get("https://www.deezer.com/en")
    try:
        driver.implicitly_wait(15)
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
    login_email.send_keys(user_name)
    login_password=driver.find_element_by_id('login_password')
    login_password.send_keys(user_pwd)

    driver.find_element_by_id('login_form_submit').click()
    print ("logging in...")
    driver.implicitly_wait(100)
    driver.find_element_by_id('page_topbar')
    driver.implicitly_wait(default_timeout)
    # save cookie
    # pickle.dump( driver.get_cookies() , open(cookie_file,"wb"))
    cookie = driver.get_cookies()
    write_cookie(user_name, cookie)

print('now you are logged in')


#=============================   =================


while True:

    playlists = driver.find_element_by_xpath("//span[text()='Playlists']")
    playlists.click()
    time.sleep(15)
    search_box = driver.find_element_by_css_selector('input.form-control')
    search_box.send_keys(playlist)
    time.sleep(5)
    go_to=driver.find_element_by_xpath(f"//img[@alt='{playlist}']")
    driver.execute_script("arguments[0].click();", go_to)
    time.sleep(15)
    button_listen=driver.find_element_by_css_selector('span.states-button-label')
    driver.execute_script("arguments[0].click();", button_listen)
    #Wait time_to_play_for playlist
    time.sleep(Time_to_play)
    #stop the play
    button_stop=driver.find_element_by_css_selector('span.states-button-label')
    driver.execute_script("arguments[0].click();", button_stop)


