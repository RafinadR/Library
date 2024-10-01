from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select


user_email = "roman@gmail.com"
user_pass = "Rom@n2024"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://127.0.0.1:8000/")
time.sleep(2)

# user registration
driver.find_element(By.XPATH, "//button[text()='Registration']").click()
time.sleep(2)
driver.find_element(By.NAME, "email").send_keys(user_email)
time.sleep(2)
driver.find_element(By.NAME, "password1").send_keys(user_pass)
time.sleep(2)
driver.find_element(By.NAME, "password2").send_keys(user_pass)
time.sleep(2)
driver.find_element(By.NAME, "first_name").send_keys("Roman")
time.sleep(2)
driver.find_element(By.NAME, "middle_name").send_keys("Ivanovich")
time.sleep(2)
driver.find_element(By.NAME, "last_name").send_keys("Veles")
time.sleep(2)
select = Select(driver.find_element(By.ID, "id_role"))
select.select_by_visible_text("librarian")
driver.find_element(By.XPATH, "//button[text()='Register']").click()
time.sleep(2)

# user valid authentivation
driver.find_element(By.NAME, "email").send_keys(user_email)
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys(user_pass)
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Log In']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Books']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='Kobzar (poetry collection)']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Back to all books']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Main Page']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Log Out']").click()
time.sleep(2)

# user invalid authentivation
driver.find_element(By.NAME, "email").send_keys("user_email")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("user_pass")
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Log In']").click()
time.sleep(2)
driver.find_element(By.NAME, "email").clear()
driver.find_element(By.NAME, "password").clear()
time.sleep(2)
driver.find_element(By.NAME, "email").send_keys(user_email)
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("user_pass")
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Log In']").click()
time.sleep(2)

driver.quit()
