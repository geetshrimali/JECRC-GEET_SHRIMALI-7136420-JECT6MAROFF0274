from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

action = ActionChains(driver)
driver.get("https://www.chennaisuperkings.com/")
driver.maximize_window()
sleep(3)

thala = driver.find_element(By.XPATH, "(//img[@class = 'card-img-top w-100'])[9]")

action.scroll_to_element(thala).perform()

sleep(3)
for i in range(5):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(1)
sleep(3)
