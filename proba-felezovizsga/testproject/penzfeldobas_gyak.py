import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path=r'/home/user/Asztal/chromedriver_linux64/chromedriver')
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

URL = "https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/penzfeldobas.html"
browser.get(URL)
browser.maximize_window()

btn = browser.find_element(By.ID, 'submit')
btn.click()
szamlalo = 0

for x in range(100):
    btn.click()
    if browser.find_element(By.ID, 'lastResult').text == 'fej':
        szamlalo += 1
assert szamlalo >= 30
print(szamlalo)
time.sleep(2)
browser.quit()