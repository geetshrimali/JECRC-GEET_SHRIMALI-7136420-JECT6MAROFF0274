'''
.is_displayed()
.is_enabled()
.is_selected()
'''

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
#
# driver.maximize_window()
#
# button = driver.find_element(By.XPATH,'//input[@id = "male"]')
# button.click()
# sleep(1)
# print(button.is_displayed())  ##
# print(button.is_enabled())    ##
# # driver.quit()
#
# #CHECKBOXES
# checkbox = driver.find_element(By.XPATH,'//label[text() = "Sunday"]/preceding-sibling::input')
#
# c1 = driver.find_element(By.XPATH,'//input[@id = "monday"]/following-sibling::label')
# print(c1.text)
#
# checkbox.click()
# print(checkbox.is_selected())  ##
#
# sleep(1)
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.lenskart.com/')
#
# driver.maximize_window()
#
# sleep(2)
#
# x = driver.find_element(By.ID, 'lrd1')
#
# print(x.text)
#
# assert 'EYEGLASSES' == x.text, 'not found' ##
#
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.lenskart.com/lenskart-air-la-e17269-c1-eyeglasses.html')
#
# sleep(4)
# driver.maximize_window()
#
# sleep(3)
#
# cross = driver.find_element(By.XPATH," //button[@aria-label = 'Close']")
# cross.click()
#
# check = driver.find_element(By.XPATH," //button[@data-cy = 'Clarity-Box-Button']/ancestor::div[@id = 'IOElement']")
# check.click()
#
# search = driver.find_element(By.XPATH," //div[@class = 'sc-a3b31f26-12 cVOVTL']")
# search.clear()
# search.send_keys('313001',Keys.ENTER)
#
# sleep(5)

