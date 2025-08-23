from selenium.webdriver.common.by import By


class RegistrationModalPopUp:
	def __init__(self, driver):
		self.driver = driver

	def name_input(self):
		return self.driver.find_element(By.ID,"signupName")

	def last_name_input(self):
		return self.driver.find_element(By.ID,"signupLastName")

	def email_input(self):
		return self.driver.find_element(By.ID,"signupEmail")

	def password_input(self):
		return self.driver.find_element(By.ID,"signupPassword")

	def re_password_input(self):
		return self.driver.find_element(By.ID,"signupRepeatPassword")

	def registration_btn(self):
		return self.driver.find_element(By.XPATH,"/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button")