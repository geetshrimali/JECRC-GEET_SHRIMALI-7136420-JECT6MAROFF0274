from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://opensource-demo.orangehrmlive.com/')

driver.maximize_window()
sleep(2)

title = driver.title
print(title)

username = driver.find_element(By.XPATH," //input[@name = 'username']")
username.clear()
username.send_keys('Admin')

password = driver.find_element(By.XPATH," //input[@name = 'password']")
password.clear()
password.send_keys('admin123',Keys.ENTER)

# submit = driver.find_elements(By.XPATH," //button[@type = 'submit']")

url = driver.current_url
print(url)

if "dashboard" in url:
    print("successful login")
sleep(3)
driver.quit()