from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

# driver.get("https://www.python.org/")
# sleep(2)
# driver.get("https://www.myntra.com/")
sleep(2)
driver.get("https://www.amazon.in/")
sleep(2)
text = driver.find_element(By.XPATH, "//span[text()='All']/ancestor::div[@id = 'nav-main']")
print(text)
# //input[@id = "username"]/ancestor::div[@class =]
text1 = driver.find_element(By.XPATH, "//a[text()='Mobiles']/ancestor::div[@class = 'nav-div']")
print(text1)

#descendent(first the element, then the descendent of the element)
text2 = driver.find_element(By.XPATH, "//a[@class='a-carousel-goto-prevpage']/descendant::i[@class = 'a-icon a-icon-previous-rounded']")
print(text2)

#parent - sibling(replace ascendent descendent with siblings)
#preceding-sibling(finds elder sibling)
#following-sibling(finds younger sibling)

text3 = driver.find_element(By.XPATH, "//a[text() = 'Fresh']/ancestor::li/following-sibling::li[1])")