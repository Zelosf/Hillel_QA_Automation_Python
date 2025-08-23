from selenium.webdriver.common.by import By


class GaragePage:
	def __init__(self, driver):
		self.driver = driver

	def log_out(self):
		return self.driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[4]")