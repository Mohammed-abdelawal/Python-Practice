from time import sleep

import pytesseract
from PIL import Image
from selenium import webdriver

url='http://www.washwasha.org/alafdal2019/default.aspx'

def resolve(path):
    return  pytesseract.image_to_string(Image.open(path))


def start_b(l):

    i = l.find(':')
    proxy = l[:i]
    port = l[i+1:]

    profile = webdriver.FirefoxProfile('/home/mohammed/.mozilla/firefox/x91ziwkp.default-release')
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", proxy)
    profile.set_preference("network.proxy.http_port", port)
    profile.set_preference("network.proxy.ssl", proxy)
    profile.set_preference("network.proxy.ssl_port", port)

    driver = webdriver.Firefox( firefox_profile=profile)
    driver.get(url)

    print(l)

    text = ''
    while((not text.isdigit()) or (len(text) is not 5)):
        driver.get(url)

        sleep(.1)
        driver.execute_script("submitvote(7038,'', document.getElementById('hh7038'))")
        sleep(2)
        driver.execute_script("submitvote(7038,'', document.getElementById('hh7038'))")

        img = driver.find_element_by_id('CodeVerfiy1_imgCode')
        

        with open('c.png', 'wb') as file:
            file.write(img.screenshot_as_png)
            file.close()

        text = resolve('c.png')
        print(text)
    sleep(.8)
    inputElement = driver.find_element_by_id("CodeVerfiy1_txtCode") 
    sleep(.5)
    inputElement.send_keys(text)
    driver.execute_script("finalv()")
    sleep(.5)
    driver.quit()

a = open('ip_list.txt')

for l in a.readlines():
    start_b(l)
a.close()
