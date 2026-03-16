from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://testautomationpractice.blogspot.com/')

driver.find_element(By.LINK_TEXT,"Udemy Courses")
print('found')
driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy")
print('found')

#it gets links, but there should be innertext in the tag, otherwise cannot use