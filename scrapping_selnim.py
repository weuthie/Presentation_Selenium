from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import csv
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.youtube.com/channel/UCV8M-U3qHFLlS24jGVJmgIQ/videos")
chaine_titre=driver.find_elements(By.XPATH,'//*[@id="video-title"]')
chaine_vue = driver.find_elements(By.XPATH,'//*[@id="metadata-line"]/span[1]')
dict1={}
for e in range(len(chaine_titre)):
    titre = chaine_titre[e].text.split(':')[-1]
    nbvue = chaine_vue[e].text
    dict1[titre] = nbvue

with open("algomius.csv","w") as donne:
    ens_donne = csv.DictWriter(donne, fieldnames=["Titre","Vue"])
    ens_donne.writeheader()
    for keys in dict1:
        ens_donne.writerow({"Titre":str(keys),"Vue":str(dict1[keys])})

driver.quit()



