from selenium import webdriver

PATH = "./chromedriver"

driver1 = webdriver.Chrome(PATH)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver2 = webdriver.Chrome(PATH, chrome_options=chrome_options)

driver1.get("https://www.python.org/")
driver2.get("https://www.python.org/")