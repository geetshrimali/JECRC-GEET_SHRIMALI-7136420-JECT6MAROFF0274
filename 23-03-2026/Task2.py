
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 30)

action = ActionChains(driver)
driver.get("https://www.myntra.com/")
driver.maximize_window()

men = wait.until(EC.presence_of_element_located((By.XPATH, "(// a [text() = 'Men'])[1]")))

action.move_to_element(men).perform()

suit = wait.until(EC.visibility_of_element_located((By.XPATH, "(// a [text() = 'Blazers & Coats'])[1]")))
suit.click()

action.send_keys(Keys.PAGE_DOWN).perform()
prod = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='product-sliderContainer'])[25]")))
action.scroll_to_element(prod).perform()
sleep(5)