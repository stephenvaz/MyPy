from selenium import webdriver
import time
menu=input("1.CS-1 \n2.CS-2 \n3.English\n")
driver = webdriver.Chrome('D:\\Users\Stephen\Dev\Git\Python\chromedriver.exe')

def cs1():
    #input
    id=input()
    pwd=input()
    #cs1 website
    driver.get("https://www.edusol.colscol.com/mod/attendance/view.php?id=652")
    #login
    id_in=driver.find_element_by_xpath('//*[@id="username"]')
    id_in.send_keys(id) 
    pwd_in=driver.find_element_by_xpath('//*[@id="password"]')  
    pwd_in.send_keys(pwd)
    #button
    login_button=driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
    time.sleep(2)
    login_check=driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div/div/div[2]/div[2]/div/div[2]/div')
    if login_check:
        print('Incorrect ID/Password!')
        input()   
    else:
        time.sleep(2)
        #attendance(submit_your_attendance)
        submit_link = driver.find_element_by_link_text("Submit attendance").click()
        #present_button
        pr_button=driver.find_element_by_name('status').click()
        #save attendance
        save_changes_button =driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
        #logout
        logout_1=driver.find_element_by_xpath('//*[@id="dropdown-1"]/span/span/span/img').click()
        logout_2=driver.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[6]').click()
        print('Done!')

def cs2():
    #input
    id=input()
    pwd=input()
    driver.get("https://www.edusol.colscol.com/mod/attendance/view.php?id=651")
    #login
    id_in=driver.find_element_by_xpath('//*[@id="username"]')
    id_in.send_keys(id)
    pwd_in=driver.find_element_by_xpath('//*[@id="password"]')
    pwd_in.send_keys(pwd)
    #button
    login_button=driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
    time.sleep(2)
    #login check
    login_check=driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div/div/div[2]/div[2]/div/div[2]/div')
    if login_check:
        print('Incorrect ID/Password!')
        input()   
    else:
        time.sleep(2)
        #attendance(submit_your_attendance)
        submit_link = driver.find_element_by_link_text("Submit attendance").click()
        #present_button
        pr_button=driver.find_element_by_name('status').click()
        #save attendance
        save_changes_button =driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
        #logout
        logout_1=driver.find_element_by_xpath('//*[@id="dropdown-1"]/span/span/span/img').click()
        logout_2=driver.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[6]').click()
        print('Done!')

def eng():
    #input
    id=input()
    pwd=input()
    driver.get("https://www.edusol.colscol.com/mod/attendance/view.php?id=1630")
    #login
    id_in=driver.find_element_by_xpath('//*[@id="username"]')
    id_in.send_keys(id)
    pwd_in=driver.find_element_by_xpath('//*[@id="password"]')
    pwd_in.send_keys(pwd)
    #button
    login_button=driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
    time.sleep(2)
    #login check
    login_check=driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div/div/div[2]/div[2]/div/div[2]/div')
    if login_check==driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div/div/div[2]/div[2]/div/div[2]/div'):
        print('Incorrect ID/Password!')
        input()
    elif login_check!=driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div/div/div[2]/div[2]/div/div[2]/div'):
       #attendance(submit_your_attendance)
        submit_link = driver.find_element_by_xpath('//*[@id="region-main"]/div/div[1]/table[1]/tbody/tr[6]/td[3]/a')
        #present_button
        pr_button=driver.find_element_by_name('status').click()
        #save attendance
        save_changes_button =driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
        #logout
        logout_1=driver.find_element_by_xpath('//*[@id="dropdown-1"]/span/span/span/img').click()
        logout_2=driver.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[6]').click()
        print('Done!')

    
        
    
if menu=='1':
    cs1()
elif menu=='2':
    cs2()
elif menu=='3':
    eng()
