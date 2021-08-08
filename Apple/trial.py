from typing import Text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import secrets
import string

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

b = webdriver.Chrome('D:\\Users\Stephen\Dev\Git\Python\chromedriver.exe', options=options)

#local variables
N=7
n=5
Nn=12
fnm = ''.join(secrets.choice(string.ascii_lowercase) for i in range(N))
lnm = ''.join(secrets.choice(string.ascii_lowercase) for i in range(n))
pas = ''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(Nn))
dob = '09092000'

def temp_mail():
    b.get('https://temp-mail.org/en/')
    global email
    global curr
    time.sleep(8)
    email = b.find_element_by_xpath('//*[@id="mail"]').get_attribute('value')
    b.execute_script("window.open('about:blank','secondtab');")
    b.switch_to.window("secondtab")

def card():
    b.get("https://namso-gen.net/")
    b.find_element_by_xpath('//*[@id="bin"]').send_keys(5543504508)
    b.find_element_by_xpath('//*[@id="quantity"]').send_keys(0)
    b.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/form/div[4]/button').click()
    cards = b.find_element_by_xpath('//*[@id="result"]').get_attribute('value')
    b.get('https://namso-gen.net/cc-checker/')
    b.find_element_by_xpath('//*[@id="cc"]').send_keys(cards)
    b.find_element_by_xpath('//*[@id="form"]/div[2]/div/button[1]').click()
    c='0'
    while c=='0' :
        live = b.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div[1]/h3/span').text
        if live >= '1':
            break
    b.find_element_by_xpath('//*[@id="stop"]').click()
    c_1 = b.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div[2]/div[1]').text
    print(c_1)
def tv_apple():
    b.get('https://tv.apple.com/in')
    time.sleep(5)
   
    b.find_element_by_xpath('//*[@id="ember6"]/div/div[1]/div[4]/button').click()
    time.sleep(5)
    b.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div[2]/button[1]/text()').click()
   
    b.find_element_by_xpath('//*[@id="app"]/div/div/div/main/div/div/main/div/div/div[5]/button').click()
    b.find_element_by_xpath('//*[@id="firstName"]').send_keys(fnm)
    b.find_element_by_xpath('//*[@id="lastName"]').send_keys(lnm)
    b.find_element_by_xpath('').send_keys(dob)
    b.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    b.find_element_by_xpath('//*[@id="acAccountPassword"]').send_keys(pas)
    b.find_element_by_xpath('//*[@id="agreedToTerms"]').click()
    b.find_element_by_xpath('//*[@id="app"]/div/div/div/main/div/div/div[2]/button').click()
    #for email verification
    #b.switch_to.window(b.window_handles[0])
def tv_app_2():
    b.get('https://tv.apple.com/in')
    time.sleep(3)
    b.find_element_by_xpath('//*[@id="ember6"]/div/div[1]/div[4]/button').click()
    #modal dialog problem
    time.sleep(10)
    b.switch_to_alert().accept()
    time.sleep(5)
    b.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div[2]/button[1]').click()
    
    
tv_app_2()

#//*[@id="app"]/div/div/main/div/div[2]/button[1]