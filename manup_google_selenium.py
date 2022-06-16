from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.get("https://www.google.com")
codesour = driver.page_source
page = BeautifulSoup(codesour,'html.parser')
print(page.find('title').getText())
print("__________________________________")
driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('ouzediop1234@gmail.com')
# driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
# driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
codesour1 = driver.page_source
page1 = BeautifulSoup(codesour1,'html.parser')
print(page1.find('title').getText())
driver.quit()
