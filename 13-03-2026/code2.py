
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

# opts.add_argument('--headless')

driver = webdriver.Chrome(options=opts)


driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

sleep(1)

i1 = driver.find_element(By.ID, 'name')
print('found')
i2 = driver.find_element(By.ID, 'email')
print('found')
i3 = driver.find_element(By.ID, 'phone')
print('found')
i4 = driver.find_element(By.ID, 'textarea')
print('found')
i5 = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
print('found')

n1 = driver.find_element(By.NAME, 'start')
print('found')
n2 = driver.find_element(By.NAME, 'Cross-Column')
print('found')
n3 = driver.find_element(By.NAME, 'Navbar')
print('found')
n4 = driver.find_element(By.NAME, 'Cross-Column 2')
print('found')
n5 = driver.find_element(By.NAME, '1307673142697428135')
print('found')

c1 = driver.find_elements(By.CLASS_NAME, 'form-check-input')
print('found')
print(len(c1))
c2 = driver.find_elements(By.CLASS_NAME, 'blog-pager')
print('found')
print(len(c2))
c3 = driver.find_elements(By.CLASS_NAME, 'widget-content')
print('found')
print(len(c3))
c4 = driver.find_elements(By.CLASS_NAME, 'widget HTML')
print('found')
print(len(c4))
c5 = driver.find_elements(By.CLASS_NAME, 'clear')
print('found')
print(len(c5))

t1 = driver.find_elements(By.TAG_NAME, 'form')
print('found')
print(len(t1))
t2 = driver.find_elements(By.TAG_NAME, 'input')
print('found')
print(len(t2))
t3 = driver.find_elements(By.TAG_NAME, 'button')
print('found')
print(len(t3))
t4 = driver.find_elements(By.TAG_NAME, 'h2')
print('found')
print(len(t4))
t5 = driver.find_elements(By.TAG_NAME, 'style')
print('found')
print(len(t5))

driver.quit()