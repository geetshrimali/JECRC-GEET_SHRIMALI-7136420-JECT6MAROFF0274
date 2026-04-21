from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get(r"D:\coding\capg\selenium\23-03-2026\ht.html")
driver.maximize_window()

sleep(1)
present = driver.find_element(By.ID,'presentAddress')

perm = driver.find_element(By.ID,'permanentAddress')

present.send_keys('JECRC, JAIPUR, RJ')
sleep(1)

present.click()

action = ActionChains(driver)
sleep(1)

action.key_down(Keys.CONTROL).send_keys('a').perform()
sleep(1)
action.key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys('c').perform()
action.key_up(Keys.CONTROL).perform()
sleep(1)
perm.click()
action.key_down(Keys.CONTROL).send_keys('v').perform()
sleep(1)
action.key_up(Keys.CONTROL).perform()
sleep(5)
