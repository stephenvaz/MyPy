from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('D:\\Users\\Stephen\\Dev\\Git\\Python\\chromedriver.exe')
driver.get("https://freesearchigrservice.maharashtra.gov.in/")
options = webdriver.ChromeOptions()


def init():
    cl=driver.find_element_by_partial_link_text("Close").click()
    dn=driver.find_element_by_xpath('//*[@id="mnuSearchTypen1"]/table').click()

def index():
    reg_type=driver.find_element_by_xpath('//*[@id="rblDocType"]/tbody/tr/td[3]/label').click()
    dis=driver.find_element_by_id("ddldistrictfordoc").click()
    dis_sel=driver.find_element_by_xpath('//*[@id="ddldistrictfordoc"]/option[31]').click()
    
    
init()
index()