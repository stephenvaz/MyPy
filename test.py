from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_experimental_option ('excludeSwitches', ['enable-logging'])
#driver
browser = webdriver.Chrome('D:\\Users\Stephen\Dev\Git\Python\chromedriver.exe',options=options)
#driver

def switch():
    x=0
    while x<7:
        browser.execute_script("window.open()")
        time.sleep(2)
        browser.switch_to.window(browser.window_handles[x])
        x=x+1
switch()