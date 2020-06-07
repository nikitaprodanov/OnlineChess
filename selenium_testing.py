from selenium import webdriver

PATH = "/home/nikita/Desktop/Python/OnlineChess/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.python.org/")
print(driver.title)
driver.quit()