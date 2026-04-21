from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/')
sleep(3)
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Checkboxes")  #checkboxes

driver.find_element(By.PARTIAL_LINK_TEXT,"Drag and") #dragaddrop

l = driver.find_elements(By.TAG_NAME, 'li') #list li items
print(len(l))

driver.get('https://the-internet.herokuapp.com/tables')

driver.find_element(By.XPATH, "//td[text() = 'jdoe@hotmail.com']/following-sibling::td[2]") #website

driver.find_element(By.XPATH, "//td[text() = 'Bach']/following-sibling::td[5]/child::a[2]") #delete

driver.find_element(By.XPATH, "//div[@class = 'example']/descendant::table[2]") #second table

driver.find_element(By.XPATH, "//table[@id = 'table2']/descendant::tr[4]/child::td[4]") #100$ cell

driver.find_element(By.XPATH, "//table[@id = 'table2']/descendant::tr[4]/child::td[4]/parent::tr") #parent
sleep(2)
driver.quit()

