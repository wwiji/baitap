#Lấy ra tat cả họa sĩ chữ P
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Khoi tao WebDriver
drive = webdriver.Chrome()

#Mo trang
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22P%22"
drive.get(url)

#Doi 2s cho trang chay
time.sleep(2)

#Lay tat ca cac the    "ul"
ul_tag = drive.find_elements(By.TAG_NAME,"ul")

#Chon the ul thu 21
ul_painters = ul_tag[20]

#Lay ra tat ca the li
li_tag = ul_painters.find_elements(By.TAG_NAME, "li")

#Tao danh sach url
links = [tag.find_element(By.TAG_NAME, 'a').get_attribute("href") for tag in li_tag]

# Tao danh sach url
titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title") for tag in li_tag]
#Xuat ra danh sach
for link in links:
    print(link)
drive.quit()

for title in titles:
    print(title)
drive.quit()