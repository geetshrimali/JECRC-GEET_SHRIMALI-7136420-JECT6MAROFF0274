# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# sleep(10)


# from selenium import webdriver
# from time import sleep
# driver = webdriver.Edge()
# sleep(10)

# from selenium import webdriver
# from time import sleep
# driver = webdriver.Firefox()
# sleep(10)

# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('https://apple.com')
# driver.maximize_window()
# sleep(5)
# driver.minimize_window()
# sleep(2)

# from selenium import webdriver
# from time import sleep
# driver = webdriver.Edge()
# driver.get('https://apple.com')
# driver.maximize_window()
# sleep(5)
# driver.minimize_window()
# sleep(2)

# from selenium import webdriver
# from time import sleep
# driver = webdriver.Firefox()
# driver.get('https://apple.com')
# driver.maximize_window()
# sleep(5)
# driver.minimize_window()
# sleep(2)


# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('https://apple.com')
# driver.maximize_window()
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.refresh()
# sleep(2)
# driver.minimize_window()
# sleep(2)


# from selenium import webdriver
# from time import sleep
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(options=opts)
# driver.get('https://apple.com')
# driver.maximize_window()
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.refresh()
# sleep(2)
# driver.minimize_window()
# sleep(2)


from selenium import webdriver
from time import sleep

opts = webdriver.FirefoxOptions()

driver = webdriver.Firefox(options=opts)
driver.get("https://capgemini.com")

sleep(2)

driver.get("https://apple.com")
driver.maximize_window()

sleep(2)
driver.back()

sleep(2)
driver.forward()

sleep(2)
driver.refresh()

x = driver.current_url
y = driver.title
z = driver.name
print(f'url = {x}')
print(f'title = {y}')
print(f'browser = {z}')

sleep(2)
driver.quit()

