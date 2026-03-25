from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(3)

# parent_win = driver.current_window_handle
#
# driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
# sleep(3)
# windows = driver.window_handles
#
# print(len(windows))
# driver.switch_to.window(windows[-1])
#
# sleep(1)
# assert 'New' in driver.find_element(By.CLASS_NAME,'example').text
# # print('done')
# driver.close()
#
# # driver.switch_to.window(parent_win)
# sleep(3)


#opening in new window:
# driver.switch_to.new_window('tab')
driver.switch_to.new_window('window')
driver.get('https://www.google.com')
sleep(3)
