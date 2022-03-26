from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pprint import pprint
from io import StringIO

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://bus.go.kr/searchResult6.jsp")
#driver.implicitly_wait(3)
element = driver.find_element(By.XPATH, "//*[@id=\"searchname\"]")
#driver.implicitly_wait(3)
element.send_keys("11245")
#driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//*[@id=\"left\"]/div[1]/div/button").click()

first = driver.find_element(By.XPATH, "//*[@id=\"left\"]/div[2]/div/table/tbody/tr[5]/td[2]/div[2]")
second = driver.find_element(By.XPATH, "//*[@id=\"left\"]/div[2]/div/table/tbody/tr[5]/td[2]/div[4]")

print('First: ' + first.text)
print('Second: ' + second.text)

while(True):
    pass