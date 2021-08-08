from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
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
d = webdriver.Chrome('D:\\Users\Stephen\Dev\Git\Python\chromedriver.exe',options=options)

def res():
    f = open("D:\\Users\Stephen\Dev\Git\Python\\text.txt","r")
    content = f.readlines()
    s = 0
    m = 1
    t = 1
    while s<13 :
        sno = content[s]
        mname = content[m]
        d.get('https://msbshse.co.in/') #//*[@id="SEAT_NO"]
        d.find_element_by_xpath('//*[@id="SEAT_NO"]').send_keys(sno)
        d.find_element_by_xpath('//*[@id="MOTHER_NAME"]').send_keys(mname)
        d.execute_script("window.open('https://msbshse.co.in/')")
        d.switch_to.window(d.window_handles[t])
        s = s + 2
        m = m + 2
        t = t + 1


def result1():
    d.get('https://mh-ssc.ac.in/home/index')
    d.find_element_by_xpath('//*[@id="seat"]').send_keys('M068812')
    d.find_element_by_xpath('//*[@id="mother"]').send_keys('LORENE')
    time.sleep(1)
    d.find_element_by_xpath('//*[@id="btnSubmit"]').click()



#result1()
res()