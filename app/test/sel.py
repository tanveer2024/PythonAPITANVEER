from selenium import webdriver
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()

driver = webdriver.Firefox()
driver.get("https://www.python.org/")
assert "Python" in driver.title
