from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get(r"D:\coding\capg\selenium\23-03-2026\index1.html")
driver.maximize_window()

sleep(1)
txt = driver.find_element(By.ID,'password')
txt.send_keys('hshshs')
sleep(1)

pswrd = driver.find_element(By.ID,'eyeBtn')

action = ActionChains(driver)

action.click_and_hold(pswrd).perform()
sleep(3)
action.release()
sleep(1)