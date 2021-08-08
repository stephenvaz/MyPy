from selenium import webdriver
import time
d = webdriver.Chrome('D:\\Users\Stephen\Dev\Git\Python\chromedriver.exe')

d.get('https://google.com')
d.execute_script("window.open('about:blank','secondtab');") 
d.switch_to.window("secondtab")
time.sleep(5)
d.switch_to.window(d.window_handles[0])