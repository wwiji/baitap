from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Thu vien

# Khởi tao WebDriver
driver = webdriver.Chrome()

#Mo mot trang web
driver.get("https://gomotungkinh.com")
time.sleep(3)
#Tìm phần tử img co id là 'bonk'
bonk_img = driver.find_element(By.ID, "bonk")

#Click liên tc
while True:
    bonk_img.click()
    print("Clicked on the bonk image")
    time.sleep(3)
