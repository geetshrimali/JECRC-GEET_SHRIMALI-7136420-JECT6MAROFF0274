from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

wait = WebDriverWait(driver, 10)

driver.get(r'D:\coding\capg\selenium\20-03-2026\playlist.html')
driver.maximize_window()

x = driver.find_element(By.XPATH,"//select[@id = 'songs']")
select = Select(x)

if select.is_multiple:
    select.select_by_index(2)
    select.select_by_visible_text('Shake It Off')
    select.select_by_visible_text('Night Changes')

print([i.text for i in select.all_selected_options])

print([i.text for i in select.options])
driver.find_element(By.XPATH,"//button[text() = 'Add to Playlist']").click()
sleep(3)

driver.quit()

