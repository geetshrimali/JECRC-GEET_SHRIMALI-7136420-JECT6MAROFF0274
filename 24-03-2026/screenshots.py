import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

folder = os.path.join(os.getcwd(),'Screenshots')
os.makedirs(folder,exist_ok=True)

driver = webdriver.Chrome()

driver.get('https://www.marvel.com/movies/blade')

driver.maximize_window()

action = ActionChains(driver)

sleep(2)

# driver.save_screenshot(f"{folder}/full_scr.png")
# sleep(2)

# img = driver.find_element(By.XPATH,"(//img[@data-testid = 'prism-image'])[1]")
#
# img.screenshot(f"{folder}/Blade.png")

poster = driver.find_element(By.XPATH,"(//img[@data-testid = 'prism-image'])[4]")
action.scroll_to_element(poster).perform()
sleep(1)

poster.screenshot(f"{folder}/Poster.png")
sleep(1)
