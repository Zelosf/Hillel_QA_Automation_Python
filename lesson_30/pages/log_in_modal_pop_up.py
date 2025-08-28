from selenium.webdriver.common.by import By


class LoginModalPopUp:
	def __init__(self, driver):
		self.driver = driver

	def registration_link(self):
		return self.driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[1]")