# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.amazon.in/')
# sleep(3)
# driver.maximize_window()
#
#
# search = driver.find_element(By.XPATH,"//input[@type = 'text']")
# sleep(1)
# search.clear()
# search.send_keys('Hello',Keys.ENTER)
# sleep(1)

# button = driver.find_element(By.ID,"nav-search-submit-button")
# button.click()

# driver.quit()


#flipkart
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.flipkart.com/')
sleep(3)
driver.maximize_window()

cross = driver.find_element(By.XPATH,"//span[@role = 'button']")
cross.click()
search = driver.find_element(By.XPATH,"//input[@name = 'q']")
sleep(1)
search.clear()
search.send_keys('Mobile',Keys.ENTER)
search = driver.find_element(By.XPATH,"//input[@name = 'q']")
x = search.get_attribute('value')
print(x)
sleep(2)
a = driver.find_element(By.XPATH,"//div[text() = 'Apple']/preceding-sibling::div")
a.click()
b = driver.find_element(By.XPATH,"//div[text() = 'Apple']")
print(b.text)
sleep(1)
c = driver.find_element(By.XPATH,"//div[@class = 'lWX0_T']/descendant::img[@loading = 'eager']")
c1 = c.get_attribute('src')
print(c1)
sleep(1)

driver.quit()