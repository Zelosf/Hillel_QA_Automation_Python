from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

data = [
	("20400465481215", "Посилка отримана"),
	("20400465481216", "Посилка отримана"),
	("20400465481217", "Посилка отримана"),
]

for ttn, answer in data:
	driver.get("https://tracking.novaposhta.ua/#/uk")
	input_element = driver.find_element(By.CLASS_NAME, "track__form-group-input")
	input_element.send_keys(ttn)
	time.sleep(1)
	driver.find_element(By.ID, "np-number-input-desktop-btn-search-en").click()
	time.sleep(3)

	status = driver.find_element(By.CLASS_NAME, "header__status-text")
	status_text = status.text

	if "Отримана" in status_text:
		print(f"Чудово посилка {ttn} отримана!")
	else:
		print(f"Статус посилки {ttn}: {status_text}")

time.sleep(1)
driver.quit()
