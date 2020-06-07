from selenium import webdriver

PATH = "./chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.python.org/")
print(driver.title)
driver.quit()