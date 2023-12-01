from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1) Перейти на https://sbis.ru/ в раздел "Контакты"
sbis_link = "https://sbis.ru/"
browser = webdriver.Chrome()
browser.get(sbis_link)

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                """li[class*=sbisru-Header__menu-item-1]"""))).click()
print('1. Переход на https://sbis.ru/ в раздел "Контакты"')

browser.get('https://sbis.ru/contacts')
contacts_block_container = browser.find_elements(By.CSS_SELECTOR, "div[class*=sbis_ru-container]")
for container in contacts_block_container:
    try:
        if container.find_element(By.TAG_NAME, 'h2').text == "Контакты":
            print('2. Регион соответствует настоящему:', container.find_element(By.CSS_SELECTOR, 'span[class*=sbis_ru-Region-Chooser__text]').text)
            print('Субъекты региона:', [x.text for x in browser.find_elements(By.CSS_SELECTOR, "div[class*=sbisru-Contacts-List__city]")])
            container.find_element(By.CSS_SELECTOR, 'span[class*=sbis_ru-Region-Chooser__text]').click()
            break
    except:
        pass

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                'li[class*=sbis_ru-Region-Panel__item]')))
region_panel = browser.find_element(By.CSS_SELECTOR, 'span[title*="Камчатский край"]').click()
time.sleep(7)
print('3. Регион изменен на Камчатский')

print('4. title:', browser.title,
      ', url:', browser.current_url)
print('Регион:',
      container.find_element(By.CSS_SELECTOR, 'span[class*=sbis_ru-Region-Chooser__text]').text)
print('Субъекты региона:',
      [x.text for x in browser.find_elements(By.CSS_SELECTOR, "div[class*=sbisru-Contacts-List__city]")])
