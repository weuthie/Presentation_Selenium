from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.get("https://www.google.com")
codesour = driver.page_source
page = BeautifulSoup(codesour,'html.parser')
print(" ######################Page 1:",page.find('title').getText())
driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('ouzediop1234@gmail.com')
codesour1 = driver.page_source
page1 = BeautifulSoup(codesour1,'html.parser')
print(" ######################Page 2:",page1.find('title').getText())
driver.quit()
