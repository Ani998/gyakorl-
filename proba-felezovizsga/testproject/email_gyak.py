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

URL = "https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/email_validation.html"
browser.get(URL)
browser.maximize_window()

#Helytelen kitöltés esete:
email_ad = browser.find_element(By.ID, 'email')
email_ad.send_keys('teszt@')
submit_btn = browser.find_element(By.ID, 'submit')
submit_btn.click()

msg = browser.find_element(By.XPATH, ('//div[@class="validation-error"]')).text
assert msg == 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.' or "Please enter a part following '@'. 'teszt@' is incomplete."

#Üres
email_ad.clear()
email_ad.send_keys('')
submit_btn.click()

msg = browser.find_element(By.XPATH, ('//div[@class="validation-error"]')).text
assert msg == "Kérjük, töltse ki ezt a mezőt." or "Please fill out this field."

#Helyes kitöltés

email_ad.clear()
email_ad.send_keys('teszt@elek.hu')
submit_btn.click()


time.sleep(3)
browser.quit()