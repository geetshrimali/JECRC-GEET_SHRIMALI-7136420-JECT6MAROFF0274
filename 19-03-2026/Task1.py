from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://abc.com/')

wait = WebDriverWait(driver, 10,)

x = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='tile--hero__container']/descendant::picture/img")))
for i in x:
    print(i.get_attribute('src'))