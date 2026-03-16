from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/radio-button')

driver.maximize_window()
sleep(2)

button = driver.find_element(By.XPATH,"//li[@id = 'item-2']")
button.click()

title = driver.title
print(title)

rd = driver.find_element(By.XPATH,"//label[@for='yesRadio']")
rd.click()

result = driver.find_element(By.XPATH,"//span[@class='text-success']")
print("You have selected",result.text)

print("ID:",button.get_attribute("id"))
print("CLASS:",button.get_attribute("class"))

url = driver.current_url
print(url)

sleep(3)
driver.quit()