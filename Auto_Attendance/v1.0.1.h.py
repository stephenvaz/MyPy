#v1.0.1.h (h-->headless mode)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

#Date-time
x = datetime.datetime.now()
print(x)
print(x.strftime("%A"))
#attendance program will only work when the time's correct

#menu
menu=input("1.CS-1 \n2.CS-2 \n3.English\n")
id=input("Enter Username:")
pwd=input("Enter Password:")
#id-pw

#browser(chrome)-options
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('C:\\Program Files (x86)\chromedriver.exe',chrome_options=options)

#functions(subjects for attendance)
def cs1():
    driver.get("https://www.edusol.colscol.com/mod/attendance/view.php?id=652")
    #login
    id_in=driver.find_element_by_xpath('//*[@id="username"]')
    id_in.send_keys(id)
    pwd_in=driver.find_element_by_xpath('//*[@id="password"]')
    pwd_in.send_keys(pwd)
    #button
    login_button=driver.find_element_by_xpath('//*[@id="loginbtn"]').click()    
    #attendance(submit_your_attendance)
    submit_link = driver.find_elements_by_partial_link_text("Submit")[0].click()
    #present_button
    pr_button=driver.find_element_by_name('status').click()
    #save attendance
    save_changes_button =driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
    #logout
    logout_1=driver.find_element_by_xpath('//*[@id="dropdown-1"]/span/span/span/img').click()
    logout_2=driver.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[6]').click()
    print('Done!')

def cs2():
    driver.get("https://www.edusol.colscol.com/mod/attendance/view.php?id=651")
    #login
    id_in=driver.find_element_by_xpath('//*[@id="username"]')
    id_in.send_keys(id)
    pwd_in=driver.find_element_by_xpath('//*[@id="password"]')
    pwd_in.send_keys(pwd)
    #button
    login_button=driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
    #attendance(submit_your_attendance)
    submit_link = driver.find_elements_by_partial_link_text("Submit")[0].click()
    #present_button
    pr_button=driver.find_element_by_name('status').click()
    #save attendance
    save_button =driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
    #logout
    logout_1=driver.find_element_by_xpath('//*[@id="dropdown-1"]/span/span/span/img').click() #
    logout_2=driver.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[6]').click()
    print('Done!')

def eng():
    driver.get("https://www.edusol.colscol.com/mod/attendance/view.php?id=1630")
    #login
    id_in=driver.find_element_by_xpath('//*[@id="username"]')
    id_in.send_keys(id)
    pwd_in=driver.find_element_by_xpath('//*[@id="password"]')
    pwd_in.send_keys(pwd)
    #button
    login_button=driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
    #attendance(submit_your_attendance)
    link = driver.find_elements_by_partial_link_text('Submit')[0].click() #might need change
    #present_button
    pr_button=driver.find_element_by_name('status').click() 
    #save attendance
    save_button =driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
    #logout
    logout_1=driver.find_element_by_xpath('//*[@id="dropdown-1"]/span/span/span/img').click() #
    logout_2=driver.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[6]').click()
    print('Done!')

#menu
if menu=='1':
    cs1()
elif menu=='2':
    cs2()
elif menu=='3':
    eng()

input()
