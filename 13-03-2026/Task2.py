from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/login')

driver.maximize_window()

username = driver.find_element(By.XPATH, "//input[@name='username']")
print(username)

password = driver.find_element(By.XPATH, "//input[@id='password']")
print(password)

text = driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']")
print(text)

heading = driver.find_element(By.XPATH, "//h2[contains(text(),'Login Page')]")
print(heading)

sleep(1)

driver.quit()