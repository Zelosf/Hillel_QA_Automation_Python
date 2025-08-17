from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8000/dz.html")


data = [
	("frame1", "input1", "Frame1_Secret"),
	("frame2", "input2", "Frame2_Secret")
]

for frame, input_id, secret_text in data:
	driver.switch_to.frame(driver.find_element(By.ID, frame))

	input_element = driver.find_element(By.ID, input_id)
	input_element.clear()
	input_element.send_keys(secret_text)
	time.sleep(1)
	driver.find_element(By.TAG_NAME, "button").click()
	time.sleep(1)

	alert = driver.switch_to.alert
	alert_text = alert.text

	if "Верифікація пройшла успішно!" in alert_text:
		print(f"{frame} - Верифікація пройшла: {alert_text}")
	else:
		print(f"{frame} - Помилка: {alert_text}")
	alert.accept()
	driver.switch_to.default_content()

time.sleep(3)
driver.quit()
