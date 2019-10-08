from selenium import webdriver
from  selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\Users\dell\Downloads\chromedriver.exe')
driver.get("http://google.com")
print('Current URL is----> '+driver.current_url)
print('Title is:---> '+driver.title)
driver.quit()