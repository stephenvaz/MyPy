from typing import Text
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import secrets
import string

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument("--window-size=1920,1080")

options.add_argument('--log-level=1')
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_experimental_option ('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#cloudflare bypass
options.add_experimental_option('useAutomationExtension', False) 
options.add_argument("--disable-blink-features=AutomationControlled")
b = webdriver.Chrome('D:\\Users\Stephen\Dev\Git\Python\chromedriver.exe', options=options)

#local variables
N=7
n=5
Nn=16
sG = secrets.SystemRandom()
fnm = ''.join(secrets.choice(string.ascii_lowercase) for i in range(N))
lnm = ''.join(secrets.choice(string.ascii_lowercase) for i in range(n))
pas = ''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(Nn)) + '303'
date = sG.randint(1,29)
if date < 10 :
    date = '0' + str(date)
else :
    date =str(date)

month = sG.randint(1,12)
if month < 10 :
    month = '0' + str(month)
else :
    month = str(month)

year = str(sG.randint(1950,2002))

dob = date+month+year
street = ''.join(secrets.choice(string.ascii_lowercase) for i in range(8)) +' road'
apt = ''.join(secrets.choice(string.ascii_lowercase) for i in range(10)) +' building'
street2 = ''.join(secrets.choice(string.ascii_lowercase) for i in range(9)) +' road'
city = ''.join(secrets.choice(string.ascii_lowercase) for i in range(9))

pcode_suff = (sG.randint(1,100))

if pcode_suff < 10:
    pcode_suff = '00' + str(pcode_suff) 
elif pcode_suff >= 10 & pcode_suff < 100:
    pcode_suff = '0' + str(pcode_suff) 
else :
    pcode_suff = str(pcode_suff)
    
phone = sG.randint(8000000000,9000000000)
def temp_mail():
    b.get('https://temp-mail.org/en/')
    global email
    time.sleep(6)
    email = b.find_element_by_xpath('//*[@id="mail"]').get_attribute('value')
    print(email)
    print(pas)
    b.execute_script("window.open('about:blank','secondtab');")
    b.switch_to.window("secondtab")

def card(): #checker not working
    global cards
    b.get("https://namso-gen.com/")
    time.sleep(5)
    b.find_element_by_xpath('/html/body/div/div/div/main/div/div/div[3]/div[1]/form/div[1]/label/input').send_keys(5543504508)
    b.find_element_by_xpath('//*[@id="main"]/div/div/div[3]/div[1]/form/div[3]/div[3]/label/input').send_keys(0)
    b.find_element_by_xpath('//*[@id="main"]/div/div/div[3]/div[1]/form/div[5]/button').click()
    cards = b.find_element_by_xpath('//*[@id="result"]').get_attribute('value')
    print('cc1 done')


def cc_check():
    global card_no, exp, cvv
    time.sleep(3)
    b.get('https://www.mrchecker.net/card-checker/ccn2/')
    b.find_element_by_xpath('//*[@id="cc"]').send_keys(cards)
    b.find_element_by_xpath('//*[@id="form"]/div[2]/div/button[1]').click()
    c='0'
    while c=='0' :
        live = b.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div[1]/h3/span').text
        if live >= '1':
            break
    b.find_element_by_xpath('//*[@id="stop"]').click()
    c_1 = b.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div[2]/div[1]').text
    #print(c_1)
    card_no = c_1[7:23]
    print(card_no)
    exp = c_1[24:26] + c_1[27:31]
    print(exp)
    cvv = c_1[32:35]
    print(cvv)
    print('cc2done')

def tv_apple():
    b.get('https://tv.apple.com/includes/commerce/account/create/personal')
    time.sleep(15)
    b.find_element_by_xpath('//*[@id="firstName"]').send_keys(fnm)
    b.find_element_by_xpath('//*[@id="lastName"]').send_keys(lnm)
    b.find_element_by_xpath('//*[@id="birthday"]').send_keys('0')
    b.find_element_by_xpath('//*[@id="birthday"]').send_keys('1')
    b.find_element_by_xpath('//*[@id="birthday"]').send_keys('0')
    b.find_element_by_xpath('//*[@id="birthday"]').send_keys('1')
    b.find_element_by_xpath('//*[@id="birthday"]').send_keys('2')
    b.find_element_by_xpath('//*[@id="birthday"]').send_keys('0')
    b.find_element_by_xpath('//*[@id="birthday"]').send_keys('0')
    b.find_element_by_xpath('//*[@id="birthday"]').send_keys('0')
    b.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    b.find_element_by_xpath('//*[@id="acAccountPassword"]').send_keys(pas)
    b.find_element_by_xpath('//*[@id="agreedToTerms"]').click()
    b.find_element_by_xpath('//*[@id="app"]/div/div/div/main/div[1]/div/form/div[6]/button').click()
    time.sleep(2)
    b.switch_to.window(b.window_handles[0])
    print('ap1')

def ver():
    global code
    b.find_element_by_xpath('//*[@id="click-to-refresh"]').click()
    time.sleep(8)
    b.find_element_by_partial_link_text('Verify your Apple ID email address').click()
    time.sleep(5)
    code=b.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/p/b').text
    print(code)
    print('ver done')
    time.sleep(2)

    
def tv_apple_2():
    b.switch_to_window(b.window_handles[1])
    b.find_element_by_xpath('//*[@id="secretCode"]').send_keys(code)
    b.find_element_by_xpath('//*[@id="app"]/div/div/div/main/div[1]/div/form/div[2]/button[2]').click()
    print('ap2')

def tv_apple_3():
    #card_no = '5543504508647868'
    #exp = '022023'
    #cvv = '080'
    time.sleep(5)
    b.find_element_by_xpath('//*[@id="creditCardNumber"]').send_keys(card_no)
    b.find_element_by_xpath('//*[@id="expiration"]').click()
    b.find_element_by_xpath('//*[@id="expiration"]').send_keys(exp[0])
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="expiration"]').send_keys(exp[1])
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="expiration"]').send_keys(exp[2])
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="expiration"]').send_keys(exp[3])
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="expiration"]').send_keys(exp[4])
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="expiration"]').send_keys(exp[5])
    b.find_element_by_xpath('//*[@id="creditVerificationNumber"]').send_keys(cvv)
    b.find_element_by_xpath('//*[@id="addressOfficialLineFirst"]').send_keys(street)
    b.find_element_by_xpath('//*[@id="addressOfficialLineSecond"]').send_keys(apt)
    b.find_element_by_xpath('//*[@id="addressOfficialLineThird"]').send_keys(street2)
    b.find_element_by_xpath('//*[@id="addressOfficialCity"]').send_keys(city)
    b.find_element_by_xpath('//*[@id="addressOfficialPostalCode"]').send_keys(pcode)
    b.find_element_by_xpath('//*[@id="phoneOfficeNumber"]').send_keys(phone)
    b.find_element_by_xpath('//*[@id="addressOfficialStateProvince"]').click()
    b.find_element_by_css_selector('#addressOfficialStateProvince > option:nth-child(16)').click()
    b.find_element_by_xpath('//*[@id="app"]/div/div/div/main/div[1]/div/form/div[3]/button[2]').click()
    time.sleep(10)
    b.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div/div/div[2]/button[2]').click()
    print('Account created')
    

temp_mail() #done
card() #done
cc_check()
tv_apple()
ver()
tv_apple_2()
tv_apple_3()
