from selenium.webdriver.common.by import By


class MainPage:
	def __init__(self, driver):
		self.driver = driver

	def sign_in_btn(self):
		return self.driver.find_element(By.CLASS_NAME("btn btn-outline-white header_signin"))