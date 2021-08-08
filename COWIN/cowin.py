from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument("--disable-gpu")
#options.add_argument("-enable-webgl")
#options.add_argument('--disable-dev-shm-usage')
options.add_argument("--log-level=3")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option ('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
d = webdriver.Chrome('D:\\Users\Stephen\Dev\Git\Python\chromedriver.exe',options=options)


def find():
    #pin=input("Pincode:")
    d.get('https://www.cowin.gov.in/home')
    pin_elem=d.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys('400068')#pin
    d.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/div[1]/div/div/button').click()
    time.sleep(2)
    c_name = d.find_element_by_xpath('//*[@id="Search-Vaccination-Center"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[5]/div[3]/div/div/div/div/div/div/div[1]/div').text
    print(c_name)



find()