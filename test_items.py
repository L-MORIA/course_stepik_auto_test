import time
import pytest
from selenium.webdriver.common.by import By

def test_product_page_contains_add_to_basket_button(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(30)  # Для визуальной проверки языка кнопки
    # Проверяем, что кнопка добавления в корзину существует
    add_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert add_button.is_displayed(), "Кнопка 'Добавить в корзину' не найдена на странице"
