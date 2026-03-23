from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
#
# action = ActionChains(driver)
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.maximize_window()
# sleep(3)
#
# orig = driver.find_element(By.ID,'column-a')
# target = driver.find_element(By.ID,'column-b')
#
# action.drag_and_drop(orig,target).perform()
# sleep(3)

# driver = webdriver.Chrome()
#
# action = ActionChains(driver)
# driver.get("https://supertails.com/")
# driver.maximize_window()
# sleep(3)
#
# dog = driver.find_element(By.XPATH, "(//span[contains(text(),'Dogs')])[1]")
#
# action.move_to_element(dog).perform()
#
# sleep(5)

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)


driver.get("https://demoqa.com/droppable")
driver.maximize_window()


orig = wait.until(EC.visibility_of_element_located((By.ID,'draggable')))
target = wait.until(EC.visibility_of_element_located((By.ID,'droppable')))

action = ActionChains(driver)
sleep(2)
action.drag_and_drop(orig,target).perform()

sleep(5)








