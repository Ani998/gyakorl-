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

URL = "https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/teglalap_kerulet.html"
browser.get(URL)
browser.maximize_window()

a = browser.find_element(By.ID, 'a')
b = browser.find_element(By.ID, 'b')
calc_btn = browser.find_element(By.ID, 'submit')

a.send_keys(74)
b.send_keys(32)
calc_btn.click()
time.sleep(3)

result = browser.find_element(By.ID, 'result').text
assert result == '212'

time.sleep(2)

a.clear()
a.send_keys('kiskutya')
b.clear()
b.send_keys(32)
calc_btn.click()

result = browser.find_element(By.ID, 'result').text
assert result == 'NaN'
time.sleep(2)

a.clear()
a.send_keys('')
b.clear()
b.send_keys('')
calc_btn.click()

time.sleep(2)

result = browser.find_element(By.ID, 'result').text
assert result == 'NaN'
time.sleep(2)

browser.quit()




