from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Khoi tao WebDriver
drive = webdriver.Chrome()

#Mo trang
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name"
drive.get(url)

#Doi 3s cho trang chay
time.sleep(3)

#Lay tat ca cac the can lay "See also"
tags = drive.find_elements(By.TAG_NAME, "a")

#Tao ra danh sach cac lien ket
links = [tag.get_attribute("href") for tag in tags]

#Xuat ra danh sach
for link in links:
    print(link)

drive.quit()