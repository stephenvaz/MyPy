#tbd
#also add file writing to save username pass in a file



#working completely(Last Checked 02-02-2021, 19:04)



from typing import Text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import secrets
import string

N = 9
usr = ''.join(secrets.choice(string.ascii_lowercase)
                                                  for i in range(N))
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--log-level=1') #low level logging (clean terminal)
#general bypass
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_experimental_option ('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#cloudflare bypass
options.add_experimental_option('useAutomationExtension', False) 
options.add_argument("--disable-blink-features=AutomationControlled")
w = webdriver.Chrome('D:\\Users\Stephen\Dev\Git\Python\chromedriver.exe',options=options)

#............TBD: Randomize ............
#temp variables
cpm = 'waysxrips' #company name
fsnm = 'ksadhjlkj' #first name
lsnm = 'jdsxknfskd' #last name


def temp_mail():
    w.get('https://temp-mail.org/en/')
    global t1
    t1=w.current_window_handle
    global email, password
    time.sleep(5)
    email = w.find_element_by_xpath('//*[@id="mail"]').get_attribute('value')
    password = "qwerty123"
    print (email,password)
    w.execute_script("window.open('about:blank','secondtab');")
    w.switch_to.window("secondtab")

def wayscript():
#wayscript account creation
    w.get('https://wayscript.com/')
    w.find_element_by_xpath('//*[@id="marketing_scroll"]/div[1]/div[1]/div/a').click()
    w.find_element_by_xpath('//*[@id="username"]').send_keys(usr)
    print(usr)
    w.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    w.find_element_by_xpath('//*[@id="first_name"]').send_keys(fsnm)
    w.find_element_by_xpath('//*[@id="last_name"]').send_keys(lsnm)
    w.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    w.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(password)
    print(password)
    w.find_element_by_xpath('//*[@id="submit_button"]').click()
    time.sleep(6)
#wayscript complete your account
    w.find_element_by_xpath('//*[@id="company"]').send_keys(cpm)
    w.find_element_by_xpath('//*[@id="co_size"]/option[2]').click()
    w.find_element_by_xpath('//*[@id="role"]/option[4]').click()
    w.find_element_by_xpath('//*[@id="referral"]/option[4]').click()
    w.find_element_by_xpath('//*[@id="submit_button"]').click()
    w.switch_to.window(t1)
#wayscript verify
    time.sleep(5)
    w.find_element_by_partial_link_text('Welcome. Please confirm your email address.').click()
    time.sleep(3)
    w.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr[2]/td/a[1]/button').click()

    w.quit()
temp_mail()
wayscript()


