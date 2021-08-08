from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_experimental_option ('excludeSwitches', ['enable-logging'])
#driver
w = webdriver.Chrome('D:\\Users\Stephen\Dev\Git\Python\chromedriver.exe',options=options)
#driver


def trial():
    w.get('https://finance.yahoo.com/cryptocurrencies/')
    x=0
    while x < 100 :
        x = x+1
        x_str= str(x)
        most_active='//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + x_str + ']'
        for element in w.find_elements_by_xpath(most_active):
            print (element.text)

        #(for going on next page)#w.find_element_by_xpath('//*[@id="scr-res-table"]/div[2]/button[3]/span/span').click()
    
def crypto():
    w.get('https://crypto.com/price/')
    time.sleep(5)
    x=0
    #while x<50 :
    #x = x+1
    x_str= '38'#str(x)
    name=w.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/main/div[3]/ul/li['+x_str+']/div/a/div/div[2]/div/div[2]/div[1]').text
    shrt_name=w.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/main/div[3]/ul/li['+x_str+']/div/a/div/div[2]/div/div[2]/div[2]').text
    price=w.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/main/div[3]/ul/li['+x_str+']/div/a/div/div[3]/div/div[1]').text
    perc=w.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/main/div[3]/ul/li['+x_str+']/div/a/div/div[4]/div').text
    print(name+shrt_name+price+perc)
    print(x)

def cryp2():
    w.get('https://coinmarketcap.com/currencies/bitcoin/')
    name=w.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/h2/text()').text
    shrt_name=w.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/h2/small').text
    print(name+shrt_name)
cryp2()

#//*[@id="gatsby-focus-wrapper"]/div/div[2]/main/div[3]/ul/li[1]/div/a/div/div[2]/div/div[2]/div[1]
#//*[@id="gatsby-focus-wrapper"]/div/div[2]/main/div[3]/ul/li[2]/div/a/div/div[2]/div/div[2]/div[1]