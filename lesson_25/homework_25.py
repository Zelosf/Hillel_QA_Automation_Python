from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Запуск Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://qauto2.forstudy.space/")
#login - guest
#pass - welcome2qauto

player_anch = driver.find_element(By.ID, "player")
sign_in_anch = driver.find_element(By.CLASS_NAME, "btn btn-outline-white header_signin")
sign_up_anch = driver.find_element(By.CLASS_NAME, "hero-descriptor_btn btn btn-primary")
facebook_anch = driver.find_element(By.CLASS_NAME, "socials_icon icon icon-facebook")
telegram_anch = driver.find_element(By.CLASS_NAME, "socials_icon icon icon-telegram")
inst_anch = driver.find_element(By.CLASS_NAME, "socials_icon icon icon-instagram")
home_button_anch = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > nav > a")
home_button_anch = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/a")
about_button_anch = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > nav > button:nth-child(2)")
about_button_anch = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/button[1]")
contact_button_anch = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-global-layout > div > div > app-header > header > div > div > div.header_left.d-flex.align-items-center > nav > button:nth-child(3)")
contact_button_anch = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/button[2]")

driver.get("https://qauto2.forstudy.space/panel/garage")
add_car_button_anch = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-global-layout > div > div > div > app-panel-layout > div > div > div > div.col-lg-9.main-wrapper > div > app-garage > div > div.panel-page_heading.d-flex.justify-content-between > button")
add_car_button_anch = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button")
log_out_anch = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-global-layout > div > div > div > app-panel-layout > div > div > div > div.col-3.d-none.d-lg-block.sidebar-wrapper > nav > a.btn.btn-link.text-danger.btn-sidebar.sidebar_btn")
log_out_anch = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[4]")

