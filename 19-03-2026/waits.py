#implicit wait
#only used with findelement/s and finds if present in dom structure
#if not present on screen, it will find element but not clickable as not present on screen

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://abc.com/')
#
# driver.implicitly_wait(.1)
#
# x = driver.find_element(By.XPATH,"(//a[@class='AnchorLink']/parent::li/descendant::img)[1]")
# print(x.get_attribute("src"))
#
# driver.quit()



#Explicit wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://abc.com/')

wait_obj = WebDriverWait(driver, 10,)

# submit_button = wait_obj.until(EC.element_to_be_clickable((By.ID, 'button')))
# submit_button.click()

x = driver.find_element(By.XPATH,"(//a[@class='AnchorLink']/parent::li/descendant::img)[1]")
print(x.get_attribute("src"))

driver.quit()

#fluent wait
# wait_obj = WebDriverWait(driver, 10,poll_frequency=200) #fix = 500ms

#if we use implicit and explicit together, total wait will be sum of both wait, never use together