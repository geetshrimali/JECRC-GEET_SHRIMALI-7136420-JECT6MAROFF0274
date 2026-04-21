from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()

button = driver.find_element(By.XPATH,'//input[@id = "male"]')
button.click()
sleep(1)

# driver.quit()

#CHECKBOXES
checkbox = driver.find_element(By.XPATH,'//label[text() = "Sunday"]/preceding-sibling::input')
c1 = driver.find_element(By.XPATH,'//input[@id = "monday"]/following-sibling::label')
print(c1.text)

checkbox.click()
sleep(1)
