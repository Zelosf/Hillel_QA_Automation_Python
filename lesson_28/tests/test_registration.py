import pytest


def test_registration(driver, open_start_page, sign_in, registration_in_log_in, registration, check_registration_done):
	open_start_page()
	sign_in()
	registration_in_log_in()
	registration("Oleksandr", "Hlushko", "Hlushko13@gmail.com", "111qqqAAA", "111qqqAAA")
	assert check_registration_done(), "No registration"
