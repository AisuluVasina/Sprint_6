import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)  

    def open_and_close_cookies(self):
        """Открывает главную страницу и закрывает попап с куками"""
        self.open()  # открыть страницу
        self.accept_cookies()  # закрыть куки

    def accept_cookies(self):
        self.click_element(MainPageLocators.COOKIE_BTN)

    @allure.step("Клик по кнопке заказа")
    def click_top_order_btn(self):
        """Кликаем по верхней кнопке 'Заказать'"""
        self.click_element(MainPageLocators.BTN_ORDER_TOP)

    def click_bottom_order_btn(self):
        """Кликаем по нижней кнопке 'Заказать'"""
        self.click_element(MainPageLocators.BTN_ORDER_BOTTOM)

    @allure.step("Клик по логотипу")
    def click_to_scooter(self):
        """Кликаем по логотипу 'Самокат'"""
        self.click_element(MainPageLocators.LOGO_SELF)

    def click_to_yandex_logo(self):
        """Кликаем по логотипу 'Яндекс'"""
        self.click_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Раскрыть вопрос №{index}")
    def expand_accordion_item(self, index):
        # Формируем локатор для конкретного заголовка
        header_locator = (By.XPATH, MainPageLocators.ACCORDION_HEADER_TEMPLATE.format(index))
        
        wait = WebDriverWait(self.driver, 10)
        
        # Ждем, пока элемент станет кликабельным
        try:
            element = wait.until(EC.element_to_be_clickable(header_locator))
            element.click()
        except Exception as e:
            raise Exception(f"Не удалось кликнуть по заголовку аккордеона №{index}: {e}")

    @allure.step("Проверить видимость ответа на вопрос №{index}")
    def is_answer_visible(self, index):
        panel_locator = (By.XPATH, MainPageLocators.ACCORDION_PANEL_TEMPLATE.format(index))
        wait = WebDriverWait(self.driver, 10)
        
        try:
            # Ждем, пока панель станет видимой
            wait.until(EC.visibility_of_element_located(panel_locator))
            return True
        except Exception:
            return False

    @allure.step("Получить текст ответа на вопрос №{index}")
    def get_answer_text(self, index):
        self.expand_accordion_item(index)
        
        panel_locator = (By.XPATH, MainPageLocators.ACCORDION_PANEL_TEMPLATE.format(index))
        wait = WebDriverWait(self.driver, 10)
        
        element = wait.until(EC.visibility_of_element_located(panel_locator))
        return element.text.strip()