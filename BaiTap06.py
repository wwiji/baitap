#Lấy ra tất cả các họa sĩ
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re
#Tao dataframe rong~
d = pd.DataFrame({'name': [], 'birth ': [], 'death ': [], 'nationality ': [] })
number = 0
#Khoi tao webdriver
driver = webdriver.Chrome()
href_list = []
for i in range(65, 91):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"
    try:
        driver.get(url)
        time.sleep(2)
        #lấy từng đường link the li
        ul_tag = driver.find_elements(By.XPATH, "//div[@class='div-col']/ul/li")
        for ul in ul_tag:
            a_tag = ul.find_element(By.TAG_NAME, "a")
            href = a_tag.get_attribute("href")
            href_list.append(href)
    except:
        print("error")

for href in href_list:
    try:
        driver.get(href)
        time.sleep(2)
        #Lay ten hoa si
        try:
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""

        #Lay ngay sinh
        try:
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            birth = birth_element.text
            birth = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
        except:
            birth = ""

        #Lay ngay DEAD
        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = death_element.text
            death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
        except:
            death = ""


        #Lay QUOC GIA
        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
            nationality = nationality_element.text
        except:
            nationality = ""

        #Them vao dataframe
        painter = {'name': name, 'birth ': birth, 'death ': death, 'nationality ': nationality }
        d   = pd.concat([d, pd.DataFrame([painter])], ignore_index=True)
        number += 1
        if number % 50 == 0:
            print(number)
    except:
        print("error")

d.to_excel("painter.xlsx", index=False)
driver.quit()

