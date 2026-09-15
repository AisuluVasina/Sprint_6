import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from locators import OrderPageLocators 
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Инициализация страницы заказа")
    def __init__(self, driver, url):
        super().__init__(driver, url)  

    @allure.step("Заполнение формы заказа самоката")
    def order_scooter(self, first_name, last_name, address, metro_station, phone, delivery_date, rental_period):
        with allure.step("Шаг 1: Заполнение личных данных"):
            self.input_text(OrderPageLocators.NAME_INPUT, first_name)
            self.input_text(OrderPageLocators.LASTNAME_INPUT, last_name)
            self.input_text(OrderPageLocators.ADDRESS_INPUT, address)
            
            # Выбор станции метро
            metro_input = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.METRO_INPUT))
            metro_input.click()
            metro_input.clear()
            metro_input.send_keys(metro_station)

            try:
                # Ждем, пока появится блок с опциями
                self.wait.until(EC.visibility_of_element_located(OrderPageLocators.METRO_OPTIONS_CONTAINER))
                option_locator = OrderPageLocators.station_locator(metro_station)
                option_element = self.wait.until(EC.element_to_be_clickable(option_locator))

                option_element.click()
            
            except TimeoutException:
                self.driver.save_screenshot(f"debug_metro_fail_{station_name}.png")
                print(f"Ошибка: Не удалось найти станцию '{station_name}' в выпадающем списке.")
                print("Проверьте: совпадает ли текст в списке (например, 'ВДНХ (линия)') с тем, что вы передаете.")
                raise
            
            self.input_text(OrderPageLocators.PHONE_FIELD, phone)

            # Переход на второй экран
            self.click_element(OrderPageLocators.NEXT_BTN)

        with allure.step("Шаг 2: Указание даты и срока аренды"):
            # Ввод даты доставки
            date_field = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT))
            date_field.clear()
            date_field.send_keys(delivery_date)

            # Закрываем календарь, чтобы он не мешал
            self.click_element(OrderPageLocators.ORDER_TITLE)

            # Выбор срока аренды
            self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
            period_option_locator = OrderPageLocators.period_locator(rental_period)
            self.click_element(period_option_locator)

        with allure.step("Шаг 3: Оформление заказа"):
            # Нажимаем "Заказать"
            self.click_element(OrderPageLocators.ORDER_BTN_PAGE)

            # Подтверждение заказа
            try:
                with allure.step("Подтверждение заказа в модальном окне"):
                    self.click_element(OrderPageLocators.CONFIRM_BTN_MODAL)
            except:
                pass  # Модальное окно может не появиться

    @allure.step("Клик по логотипу Самоката")
    def click_logo_self(self):
        self.click_element(OrderPageLocators.LOGO_SELF)

    @allure.step("Клик по логотипу Яндекса")
    def click_logo_yandex(self):
        self.click_element(OrderPageLocators.LOGO_YANDEX)

    @allure.step("Проверка наличия кнопки статуса заказа")
    def find_status_button(self):
        try:
            self.wait_for_visibility(OrderPageLocators.STATUS_BTN, timeout=10)
            return True
        except:
            return False