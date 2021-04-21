import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime

noms = []
adresses = []
villes = []
tels = []

driver = webdriver.Chrome('chromedriver.exe')

# Lien de la page formulaire
driver.get('https://www.mundoanimalia.com/veterinarios')
time.sleep(2)

#  enlever cookie
driver.find_element_by_xpath('//*[@id="cf-root"]/div/div/div/div[2]/div[2]/div[1]/button').click()
driver.find_element_by_xpath('//*[@id="close-claim"]').click()

for j in range (1,342):
    print(j)
    for i in range (1,18):
        try:
            print(driver.find_element(By.CSS_SELECTOR, ".avanzado_profess:nth-child("+str(i)+") .bigtxt").text)
            nom = driver.find_element(By.CSS_SELECTOR, ".avanzado_profess:nth-child("+str(i)+") .bigtxt").text
            print(driver.find_element(By.CSS_SELECTOR, ".avanzado_profess:nth-child("+str(i)+") .direccion_servicio").text)
            adresse = driver.find_element(By.CSS_SELECTOR, ".avanzado_profess:nth-child("+str(i)+") .direccion_servicio").text
            print(driver.find_element(By.CSS_SELECTOR, ".avanzado_profess:nth-child("+str(i)+") .direccion_servicio:nth-child(4)").text)
            ville = driver.find_element(By.CSS_SELECTOR, ".avanzado_profess:nth-child("+str(i)+") .direccion_servicio:nth-child(4)").text
            driver.find_element_by_xpath('//li['+str(i)+']/div/div[2]/p[3]/a/span[2]').click()
            time.sleep(1)
            print(driver.find_element_by_xpath('//div[10]/div[2]/p/span[2]').text)
            tel = driver.find_element_by_xpath('//div[10]/div[2]/p/span[2]').text
            driver.find_element_by_xpath('//li[' + str(i) + ']/div/div[2]/p[3]/a/span[2]').click()

            noms.append(nom)
            adresses.append(adresse)
            villes.append(ville)
            tels.append(tel)

        except:
            pass
    # changement de page
    driver.find_element_by_xpath('//*[@id="content_filters_criadores_full"]/div[2]/a[4]').click()
    # driver.find_element_by_xpath('//*[@id="content_filters_criadores_full"]/div[2]/a[4]').click()
    time.sleep(2)

# affichage en tableau
test = pd.DataFrame({
    'Nom entreprise': noms,
    'Adresse': adresses,
    'Ville': villes,
    'Telephone': tels
})

# # creation de fichier csv
test.to_csv('scrapVeterinaireEspagne.csv',sep="|", encoding='utf-8-sig')