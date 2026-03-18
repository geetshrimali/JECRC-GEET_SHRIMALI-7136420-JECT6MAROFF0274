#DROPDOWNS


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
#
# drop = Select(driver.find_element(By.XPATH, "//select[@id = 'country']"))
#
# drop.select_by_value('australia')
# sleep(1)
# drop.select_by_index(0)
# sleep(1)
# drop.select_by_visible_text('Japan')
# sleep(4)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(2)
search = driver.find_element(By.XPATH,"//input[@class = 'aa-Input']")
search.send_keys('glasses',Keys.ENTER)
sleep(2)
drop = Select(driver.find_element(By.XPATH, "//select[@id = 'sortByDropdown']"))
drop.select_by_value('saving')
sleep(2)
select = driver.find_elements(By.XPATH,"//div[@id = 'card-wrapper-parent']/descendant::p[@data-cy = 'plpProductTitle']")
print(select[0].text)
sleep(4)