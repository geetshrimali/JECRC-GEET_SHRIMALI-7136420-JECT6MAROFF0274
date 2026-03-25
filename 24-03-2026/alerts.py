from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

action = ActionChains(driver)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
sleep(3)

#simple-alert:
# driver.find_element(By.XPATH, "//button[text() = 'Click for JS Alert']").click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
# sleep(1)

#confirmation alert
# driver.find_element(By.XPATH, "//button[text() = 'Click for JS Confirm']").click()
# sleep(2)
# alert = driver.switch_to.alert
# # alert.accept()
# alert.dismiss()
# sleep(4)

#prompt alert
# driver.find_element(By.XPATH, "//button[text() = 'Click for JS Prompt']").click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.send_keys("Hello World")
# alert.accept()
# sleep(4)

# wait = WebDriverWait(driver, 10)
# driver.find_element(By.XPATH,"//button[text() = 'Click for JS Alert']").click()
# alert = wait.until(EC.alert_is_present())
# sleep(2)
# alert.accept()
# sleep(2)


