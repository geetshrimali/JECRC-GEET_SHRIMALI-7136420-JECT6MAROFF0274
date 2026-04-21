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
    sleep(2)
