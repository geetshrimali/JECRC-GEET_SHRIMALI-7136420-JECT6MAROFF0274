from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/automation-practice-form')
sleep(3)
driver.maximize_window()

fname = driver.find_element(By.XPATH, "//input[@id = 'firstName']")
fname.send_keys("Krish")

sname = driver.find_element(By.XPATH, "//input[@id = 'lastName']")
sname.send_keys("Kapoor")

mail = driver.find_element(By.XPATH, "//input[@id = 'userEmail']")
mail.send_keys("K0kapoor@gmail.com")

gender = driver.find_element(By.XPATH, "//input[@value = 'Male']")
gender.click()

num = driver.find_element(By.XPATH, "//input[@id = 'userNumber']")
num.send_keys("0123456789")

sub = driver.find_element(By.XPATH, "//input[@id = 'subjectsInput']")
sub.send_keys("English")
sleep(1)
driver.find_element(By.XPATH, "//div[text() = 'English']").click()
sub.send_keys("Maths")
sleep(1)
driver.find_element(By.XPATH, "//div[text() = 'Maths']").click()
sub.send_keys("Computer Science")
sleep(1)
driver.find_element(By.XPATH, "//div[text() = 'Computer Science']").click()

hobbies = driver.find_element(By.XPATH, "//input[@id = 'hobbies-checkbox-3']")
hobbies.click()

img = driver.find_element(By.XPATH, "//input[@id = 'uploadPicture']")
img.send_keys(r"C:\Users\GEET SHRIMALI\OneDrive\Pictures\Screenshots\Screenshot 2025-05-31 011236.png")

address = driver.find_element(By.XPATH, "//textarea[@id = 'currentAddress']")
address.send_keys("abc, westwood vines, Jaipur")
sleep(1)
state = driver.find_element(By.XPATH, "//div[@id ='state']")
sleep(1)
state.click()
sleep(1)
driver.find_element(By.XPATH, "//div[text() = 'Rajasthan']").click()

city = driver.find_element(By.XPATH, "//div[@id = 'city']")
sleep(1)
city.click()
sleep(1)
driver.find_element(By.XPATH, "//div[text() = 'Jaipur']").click()
sleep(1)
driver.find_element(By.XPATH, "//button[text() = 'Submit']").click() #submit
sleep(3)
driver.quit()