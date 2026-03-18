from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/upload")

driver.maximize_window()

file = driver.find_element(By.ID,"file-upload")
file.send_keys(r"C:\Users\GEET SHRIMALI\Downloads\Screenshot 2025-12-24 164603.png")

submit = driver.find_element(By.ID,"file-submit")
submit.click()
sleep(4)


#DOWNLOAD
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://the-internet.herokuapp.com/download")
#
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//a[text() = 'Screenshot 2025-12-24 164603.png']").click()
#
# sleep(10)
#
# print('downloaded')
