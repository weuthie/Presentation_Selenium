from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('ouzediop1234@gmail.com')
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()