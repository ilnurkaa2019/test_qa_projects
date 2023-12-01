from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 1) Перейти на https://sbis.ru/ в раздел "Контакты"
sbis_link = "https://sbis.ru/"
tensor_link = "https://tensor.ru/"
browser = webdriver.Chrome()
browser.get(sbis_link)

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                """li[class*=sbisru-Header__menu-item-1]"""))).click()
print('1. Переход на https://sbis.ru/ в раздел "Контакты"')

# 2) Найти баннер Тензор, кликнуть по нему
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                'a[class*=sbisru-Contacts__logo-tensor'))).click()
print('2. Клик по баннеру "Тензор"')

# 3) Перейти на https://tensor.ru/
browser.get(tensor_link)
print('3. Перешли на "https://tensor.ru/"')
# 4) Проверить, что есть блок "Сила в людях"
card_titles = WebDriverWait(browser, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[class*=tensor_ru-Index__card]")))

for card_title in card_titles:
    if card_title.find_element(By.CSS_SELECTOR, "p[class*=tensor_ru-Index__card-title]").text == "Сила в людях":
        print('4. Есть блок "Сила в людях"')

        # 5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
        element = card_title.find_element(By.CSS_SELECTOR, 'a[class*=tensor_ru-link]')
        print('5. Открывается ссылка:', element.get_attribute('href'))

        if element.get_attribute('href') != 'https://tensor.ru/about':
            quit()
        browser.execute_script("arguments[0].click();", element)

        # 6) Находим раздел Работаем и проверяем, что у всех фотографии хронологии одинаковые высота (height) и ширина (width)
        browser.get("https://tensor.ru/about")
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "p")))
        card_titles_2 = browser.find_elements(By.CSS_SELECTOR, "div[class*=tensor_ru-section]")
        images_size = []
        for card_title_2 in card_titles_2:
            try:
                h2_title = card_title_2.find_element(By.TAG_NAME, "h2")
            except:
                continue
            if h2_title.text == "Работаем":
                images = card_title_2.find_elements(By.TAG_NAME, 'img')
                for img in images:
                    images_size += [[(img.rect).get(x) for x in ('height', 'width')]]
                print(('6. Размеры изображений совпадают' if images_size == [images_size[0]]*len(images_size) else 'Размеры изображений не совпадают'))
    else:
        print('4. Блок "Сила в людях" отсутствует')




