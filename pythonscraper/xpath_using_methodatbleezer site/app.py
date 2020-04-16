import time
import pickle

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.deezer.com")

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in pickle.load(open("cookies.pkl", "rb")):
    if 'expiry' in cookie:
        del cookie['expiry']

    driver.add_cookie(cookie)

driver.get("https://www.deezer.com/en")

time.sleep(5)

stupid_modal = driver.find_element_by_xpath('//*[@id="modal-close"]')
stupid_modal.click()

stupid_popup = driver.find_element_by_xpath('//*[@id="dzr-app"]/div/div[1]/div/div/div[2]/div[2]/button')
stupid_popup.click()

search_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div/form/input')
search_box.send_keys('paul mumford')
time.sleep(1)
search_box.send_keys(Keys.RETURN)

time.sleep(2)
pauly_paul = driver.find_elements_by_link_text("Paul Mumford")
pauly_paul[0].click()

time.sleep(2)
songy_song = driver.find_element_by_xpath("//span[text()='Down Underwater']/..")
driver.execute_script("arguments[0].scrollIntoView();", songy_song)
time.sleep(2)

songy_song = driver.find_element_by_xpath("//span[text()='Afternoon Sun']/..")
songy_song.click()

# actions = ActionChains(driver)
# actions.move_to_element(songy_song).perform()
# time.sleep(2)



# driver.get("https://www.deezer.com/login")
# time.sleep(1)
# cookie_agree_button = driver.find_element_by_xpath('//*[@id="react-cookie"]/div/div[2]/button[1]')
# cookie_agree_button.click()
#
# login_email = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div[1]/input')
# login_email.send_keys('nick@grant.direct')
#
# login_password = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div[2]/input')
# login_password.send_keys('sadnap01')
#
# login_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/button')
# login_button.click()
#
# time.sleep(180)
#
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
#
# div_elem = driver.find_element_by_class_name("t-label-0-2-2")
# if div_elem.text == "I agree":
#     div_elem.parent.click()
# elem = div_elem.find_element_by_class_name("t-root-0-2-1 t-containedPrimary-0-2-9 t-isFullWidth-0-2-25 consent-accept")
# elem.click()
time.sleep(33)
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()

print('Job Done!\n')