from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.amazon.in/')

driver.maximize_window()
sleep(3)
s_bar = driver.find_element(By.CSS_SELECTOR,'input[id = "twotabsearchtextbox"]')
print(s_bar)

logo = driver.find_element(By.CSS_SELECTOR,'a[id = "nav-logo-sprites"]')
print(logo)

cart = driver.find_element(By.CSS_SELECTOR,'span[class = "nav-cart-icon nav-sprite"]')
print(cart)

signin = driver.find_element(By.CSS_SELECTOR,'#nav-tools a')
print(signin)

categories = driver.find_elements(By.CSS_SELECTOR,'div[id="nav-xshop"] a')
print("Total categories:", len(categories))

driver.quit()