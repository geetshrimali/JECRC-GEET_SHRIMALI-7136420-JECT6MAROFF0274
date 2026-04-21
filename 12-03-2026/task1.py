
from selenium import webdriver
from time import sleep

opts = webdriver.FirefoxOptions()

driver = webdriver.Firefox(options=opts)
driver.get("https://capgemini.com")

sleep(2)

driver.get("https://apple.com")
driver.maximize_window()

sleep(2)
driver.back()

sleep(2)
driver.forward()

sleep(2)
driver.refresh()

x = driver.current_url
y = driver.title
z = driver.name
print(f'url = {x}')
print(f'title = {y}')
print(f'browser = {z}')

sleep(2)
driver.quit()

