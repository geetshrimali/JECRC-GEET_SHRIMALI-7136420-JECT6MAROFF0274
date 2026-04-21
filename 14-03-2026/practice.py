from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')

driver.find_element(By.XPATH, "//td[text() = 'Learn Java']/following-sibling::td[3]")

driver.find_element(By.XPATH, "//td[text() = 'Amod']/ancestor::tbody/descendant::tr[2]/td[3]")

a = driver.find_elements(By.XPATH, "//td[text() = '300']/preceding-sibling::td[3]")

for i in a:
    print(i.text)

b = driver.find_elements(By.XPATH, "//tbody[@id = 'rows']/tr/td[1]")

for x in b:
    print(x.text)