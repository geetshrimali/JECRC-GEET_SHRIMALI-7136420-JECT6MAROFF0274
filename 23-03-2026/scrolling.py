from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#
action = ActionChains(driver)
driver.get("https://supertails.com/")
driver.maximize_window()
sleep(3)

# cat = driver.find_element(By.XPATH, "//div[@data-ganame='Breed 5']")
#
# # action.scroll_to_element(cat).perform()
# #
# # sleep(3)
# # action.scroll_by_amount(0,-500).perform()
# # sleep(3)
#
# action.scroll_from_origin(cat,0,300)

action.send_keys(Keys.PAGE_DOWN).perform()
sleep(3)
action.send_keys(Keys.PAGE_UP).perform()  #scrolls for 100 px
sleep(3)
action.key_down(Keys.CONTROL).send_keys('a').perform()
sleep(2)
action.key_up(Keys.CONTROL).perform()
sleep(2)