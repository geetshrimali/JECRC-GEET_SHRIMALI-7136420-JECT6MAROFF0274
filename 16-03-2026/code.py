from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()

name = driver.find_element(By.ID,'name')
sleep(1)
name.send_keys('Hello')
sleep(1)
email = driver.find_element(By.XPATH,'//input[@placeholder="Enter EMail"]')
email.clear()
email.send_keys('knight@gmail.com')

x = name.get_attribute('placeholder')
y = email.get_attribute('value')
print(x)
print(y)
driver.quit()