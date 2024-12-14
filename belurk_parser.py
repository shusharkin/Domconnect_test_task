from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os


load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

WEBSITE = "https://belurk.online/"
IP_INDEX = 5
EXPIRES_INDEX = 9

if not EMAIL or not PASSWORD:
    raise Exception("EMAIL и PASSWORD должны быть указаны в .env файле")

def login(driver, EMAIL, PASSWORD):
    login_button = driver.find_element(By.LINK_TEXT, 'Вход')
    login_button.click()

    signIn_form = driver.find_element(By.ID, 'signInForm')

    username_input = signIn_form.find_element(By.NAME, 'email')
    username_input.send_keys(EMAIL)

    password_input = signIn_form.find_element(By.NAME, 'password')
    password_input.send_keys(PASSWORD)

    signIn_form.submit()

def parse_proxy_table(driver, IP_INDEX, EXPIRES_INDEX):
    IPv4_button = driver.find_element(By.LINK_TEXT, 'IPv4 Shared Прокси')
    IPv4_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
    )

    proxy_table = driver.find_element(By.TAG_NAME, 'tbody')
    table_rows = proxy_table.find_elements(By.TAG_NAME, 'tr')

    proxy_data = []

    for row in table_rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        ip = cells[IP_INDEX].text
        expires = cells[EXPIRES_INDEX].text
        proxy_data.append((ip, expires))

    return proxy_data

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(WEBSITE)

    login(driver, EMAIL, PASSWORD)

    proxy_data = parse_proxy_table(driver, IP_INDEX, EXPIRES_INDEX)
    if proxy_data:
        for ip, expires in proxy_data:
            print(f'{ip} - {expires}')
    else:
        print('Нет ни одного действующего прокси')

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()
