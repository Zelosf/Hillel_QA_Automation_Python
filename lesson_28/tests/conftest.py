import pytest
from selenium import webdriver
from lesson_28.pages.main_page import MainPage
from lesson_28.pages.log_in_modal_pop_up import LoginModalPopUp
from lesson_28.pages.registration_modal_pop_up import RegistrationModalPopUp
from lesson_28.pages.garage_page import GaragePage
import time


@pytest.fixture
def driver():
	driver = webdriver.Chrome()
	yield driver
	driver.quit()


@pytest.fixture
def open_start_page(driver):
	def _open_start_page():
		driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
		time.sleep(1)
	return _open_start_page


@pytest.fixture
def sign_in(driver):
	def _sign_in():
		main_page = MainPage(driver)
		main_page.sign_in_btn().click()
		time.sleep(1)
	return _sign_in


@pytest.fixture
def registration_in_log_in(driver):
	def _registration_in_log_in():
		log_in_modal_pop_up = LoginModalPopUp(driver)
		log_in_modal_pop_up.registration_link().click()
		time.sleep(1)
	return _registration_in_log_in


@pytest.fixture
def registration(driver):
	def _registration(name, last_name, email, password, re_password):
		registration_modal_pop_up = RegistrationModalPopUp(driver)

		name_input = registration_modal_pop_up.name_input()
		name_input.clear()
		name_input.send_keys(name)
		time.sleep(1)
		last_name_input = registration_modal_pop_up.last_name_input()
		last_name_input.clear()
		last_name_input.send_keys(last_name)
		time.sleep(1)
		email_input = registration_modal_pop_up.email_input()
		email_input.clear()
		email_input.send_keys(email)
		time.sleep(1)
		password_input = registration_modal_pop_up.password_input()
		password_input.clear()
		password_input.send_keys(password)
		time.sleep(1)
		re_password_input = registration_modal_pop_up.re_password_input()
		re_password_input.clear()
		re_password_input.send_keys(re_password)
		time.sleep(1)

		registration_button = registration_modal_pop_up.registration_btn()
		registration_button.click()
		time.sleep(1)

	return _registration


@pytest.fixture
def check_registration_done(driver):
	def _check_registration_done():
		garage_page = GaragePage(driver)

		log_out = garage_page.log_out()
		return (log_out.text) == "Log out"

	return _check_registration_done