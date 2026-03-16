from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()

button1 = driver.find_element(By.XPATH,'//input[@id = "male"]')
button2 = driver.find_element(By.XPATH,'//input[@id = "female"]')

x = True
def a():
    if x:
        button1.click()
        sleep(2)
        button2.click()
        sleep(2)
        a()
a()
driver.quit()
