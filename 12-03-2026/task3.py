from selenium import webdriver
from time import sleep

browsers = [
    webdriver.Chrome,
    webdriver.Edge,
    webdriver.Firefox
]

for browser in browsers:
    driver = browser()
    driver.get("https://google.com")
    x = driver.current_url
    y = driver.title
    z = driver.name
    print(f'url = {x}')
    print(f'title = {y}')
    print(f'browser = {z}')
    sleep(2)