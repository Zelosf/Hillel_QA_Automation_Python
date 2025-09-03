import pytest
import allure


@allure.feature("Корректна регістрація")
def test_registration(driver, open_start_page, sign_in, registration_in_log_in, registration, check_registration_done):
	open_start_page()
	sign_in()
	registration_in_log_in()
	registration("Oleksandr", "Hlushko", "Hlushk1111@gmail.com", "111qqqAAA", "111qqqAAA")
	assert check_registration_done(), "No registration"


@allure.feature("Помилка при регістрації")
def test_registration_failed(driver, open_start_page, sign_in, registration_in_log_in, registration, check_registration_done):
	open_start_page()
	sign_in()
	registration_in_log_in()
	registration("Oleksandr", "Hlushko", "Hlushk1111@gmail.com", "111qqqAAA", "111qqqAAA")
	assert check_registration_done(), "No registration"


@allure.feature("Тест failed")
def test_failed():
	assert False


#pytest --alluredir=allure-results
#allure serve allure-results