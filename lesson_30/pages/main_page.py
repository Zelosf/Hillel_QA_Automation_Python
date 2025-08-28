from selenium.webdriver.common.by import By


class MainPage:
	def __init__(self, driver):
		self.driver = driver

	def sign_in_btn(self):
		return self.driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]")