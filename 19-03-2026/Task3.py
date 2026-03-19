import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.amazon.in/')

wait = WebDriverWait(driver, 10,)

driver.maximize_window()

search = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'twotabsearchtextbox']")))
search.send_keys("shampoo")

comp = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id = 'sac-autocomplete-results-container']/descendant::div[@role = 'row'][4]")))
comp.click()

sort_by = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id = 'a-autoid-0-announce']")))
sort_by.click()

sort = wait.until(EC.visibility_of_element_located((By.XPATH,"//ul[@role = 'listbox']/li[5]")))
sort.click()

ship = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id = 'p_n_free_shipping_eligible/205563695031']/descendant::i")))
ship.click()

name = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@role = 'listitem']/descendant::h2[1]")))
print(name.get_attribute('aria-label'))

price = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@role = 'listitem']/descendant::span[@class = 'a-price-whole'][1]")))
print(price.text)

driver.quit()