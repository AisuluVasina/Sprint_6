import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step("Инициализация главной страницы")
    def __init__(self, driver, url):
        super().__init__(driver, url)  

    @allure.step("Открыть страницу и закрыть попап с куками")
    def open_and_close_cookies(self):
        """Открывает главную страницу и закрывает попап с куками"""
        self.open()  # открыть страницу
        self.accept_cookies()  # закрыть куки

    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click_element(MainPageLocators.COOKIE_BTN)

    @allure.step("Клик по кнопке заказа")
    def click_top_order_btn(self):
        """Кликаем по верхней кнопке 'Заказать'"""
        self.click_element(MainPageLocators.BTN_ORDER_TOP)

    @allure.step("Клик по нижней кнопке заказа")
    def click_bottom_order_btn(self):
        """Кликаем по нижней кнопке 'Заказать'"""
        self.click_element(MainPageLocators.BTN_ORDER_BOTTOM)

    @allure.step("Клик по логотипу")
    def click_to_scooter(self):
        """Кликаем по логотипу 'Самокат'"""
        self.click_element(MainPageLocators.LOGO_SELF)

    @allure.step("Клик по логотипу Яндекс")
    def click_to_yandex_logo(self):
        """Кликаем по логотипу 'Яндекс'"""
        self.click_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Раскрыть вопрос №{index}")
    def expand_accordion_item(self, index):
        """Раскрывает вопрос аккордеона по индексу"""
        header_locator = (By.XPATH, MainPageLocators.ACCORDION_HEADER_TEMPLATE.format(index))
        self.click_element(header_locator)

    @allure.step("Проверить видимость ответа на вопрос №{index}")
    def is_answer_visible(self, index):
        """Проверяет, виден ли ответ на вопрос"""
        panel_locator = (By.XPATH, MainPageLocators.ACCORDION_PANEL_TEMPLATE.format(index))
        try:
            self.wait_for_visibility(panel_locator, timeout=10)
            return True
        except:
            return False

    @allure.step("Получить текст ответа на вопрос №{index}")
    def get_answer_text(self, index):
        """Получает текст ответа на вопрос из аккордеона"""
        self.expand_accordion_item(index)
        panel_locator = (By.XPATH, MainPageLocators.ACCORDION_PANEL_TEMPLATE.format(index))
        element = self.wait_for_visibility(panel_locator, timeout=10)
        return element.text.strip()