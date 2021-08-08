from selenium import webdriver
import time

#o = webdriver.ChromeOptions()

b = webdriver.Chrome('D:\\Users\Stephen\Dev\Git\Python\chromedriver.exe')

def temp_mail():
    b.get('https://temp-mail.org/en/')
    global email
    global curr
    time.sleep(8)
    email = b.find_element_by_xpath('//*[@id="mail"]').get_attribute('value')
    b.execute_script("window.open('about:blank','secondtab');")
    b.switch_to.window("secondtab")

temp_mail()