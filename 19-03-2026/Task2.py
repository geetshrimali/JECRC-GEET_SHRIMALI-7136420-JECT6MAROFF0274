
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://qavbox.github.io/demo/signup/')

wait = WebDriverWait(driver, 10,)

driver.maximize_window()

name = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'username']")))
name.send_keys("krish")

email = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'email']")))
email.send_keys("kkapoor@gmail.com")

tel = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'tel']")))
tel.send_keys("1234567890")

upload = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@multiple = 'multiple']")))
upload.send_keys(r"C:\Users\GEET SHRIMALI\OneDrive\Pictures\Screenshots\Screenshot 2025-05-31 011236.png")

gender = wait.until(EC.element_to_be_clickable((By.XPATH,"//select[@name = 'sgender']")))
select = Select(gender)
select.select_by_value("male")

exp = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@value = 'three']")))
exp.click()

skill = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id = 'ip']")))
skill.click()

tools = wait.until(EC.presence_of_element_located((By.XPATH,"//select[@id = 'tools']")))
select = Select(tools)
select.select_by_value("selenium")

submit = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id = 'submit']")))
submit.click()

driver.quit()