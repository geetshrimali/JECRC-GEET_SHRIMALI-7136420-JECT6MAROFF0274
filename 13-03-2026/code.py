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

# name = driver.find_element(By.ID, 'name')#.send_keys('abcd')
# print('name textfield found')
# nav = driver.find_element(By.NAME, 'Navbar')#.send_keys('abcd')
# print(nav)
# rad = driver.find_element(By.CLASS_NAME, 'form-check-input')#.send_keys('abcd'
# print('form checkbox found')
#
# rad_b = driver.find_elements(By.CLASS_NAME, 'form-check-input')#.send_keys('abcd'
# print('form checkbox found')
# print(len(rad_b))

#CSS
# name = driver.find_element(By.CSS_SELECTOR,'select[id = "animals"]')
# name = driver.find_element(By.CSS_SELECTOR, '#animals')
# print('Found')
# driver.quit()

# driver.find_element(By.ID, 'textarea').send_keys('abcd')


#CSS selector
# <a href="http://testautomationpractice.blogspot.com/">Home</a>
# a[href*="testautomationpractice"] #partial
# a[href^="http:/"]  #starts with
# a[href$ = ".com"]  #ends with

#Drawback of Css selector: only goes top to botton
#inner text not included, so cannot access them

 #xpath
 # difficult to read and slower
 #pro: find elements using inner text
 #1)relative     2)absolute xpath

 #//input[@placeholder="Enter Name"]

# n1 = driver.find_element(By.XPATH, "//p[@class='description']")
# print('success')
# n2 = driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
# print('success')
# n3 = driver.find_element(By.XPATH, "//button[@onclick='myFunction()']")
# print('success')
# n4 = driver.find_element(By.XPATH, "//option[@value='yellow']")
# print('success')
# n5 = driver.find_element(By.XPATH, "//div[@class='svg-container']")
# print('success')



n1 = driver.find_element(By.XPATH, "//h2[text()='SVG Elements']")
print('success')
n2 = driver.find_element(By.XPATH, "//p[text()='Drag me to my target']")
print('success')
n3 = driver.find_element(By.XPATH, "//h2[text()='Drag and Drop']")
print('success')
n4 = driver.find_element(By.XPATH, "//button[text()='New Tab']")
print('success')
n5 = driver.find_element(By.XPATH, "//a[text()='Udemy Courses']")
print('success')
#for dropdown
n6 = driver.find_element(By.XPATH, "//option[contains(text(),'Dog')]")
print('success')

driver.quit()