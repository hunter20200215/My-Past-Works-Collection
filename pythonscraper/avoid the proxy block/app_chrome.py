import argparse
import time
import pickle

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display


def play_playlist(playlist):
    display = Display(visible=0, size=(1920, 1080))
    display.start()

    chrome_options = Options()
    chrome_options.add_argument("window-size=1920,1080")
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.spotify.com")

    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in pickle.load(open("cookies.pkl", "rb")):
        if 'expiry' in cookie:
            del cookie['expiry']

        driver.add_cookie(cookie)

    driver.get("https://open.spotify.com/")

    print('Loaded the cookies and logging in')

    time.sleep(3)

    library_link = driver.find_element_by_xpath("//span[text()='Your Library']/../..")
    library_link.click()

    time.sleep(3)

    playlist_link = driver.find_element_by_xpath(f"//span[text()='{playlist}']/..")
    playlist_link.click()

    time.sleep(3)

    print(f'Playing playlist {playlist}')
    play_button = driver.find_element_by_xpath("//button[text()='PLAY']")
    play_button.click()

    time.sleep(3)

    try:
        shuffle_button = driver.find_element_by_xpath("//button[@title='Enable shuffle']")
        shuffle_button.click()
        print('Enabled shuffle')
    except:
        print('Shuffle was probably already enabled')
        pass

    for i in range(1, 480):
        try:
            progress_time_list = driver.find_elements_by_class_name("playback-bar__progress-time")
            print(f'Current play time: {progress_time_list[0].text}')
        except:
            print(f'Been playing {i} seconds but song time off the screen')
            pass
        time.sleep(1)

    driver.close()
    display.stop()


if __name__ == '__main__':
    print('Starting the magical machine')
    parser = argparse.ArgumentParser(description='Make cookies')
    parser.add_argument('--playlist', required=True)
    args = parser.parse_args()
    play_playlist(args.playlist)
    print('The magic show is over')

