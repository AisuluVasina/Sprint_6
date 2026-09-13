import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from locators import OrderPageLocators 


class OrderPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get(self.url)

    def input_text(self, locator, text):
        #Ввод текста в поле с ожиданием видимости и очисткой
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        #Клик по элементу с ожиданием кликабельности
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def find_status_button(self):
        #Проверка наличия кнопки статуса
        try:
            self.wait.until(EC.visibility_of_element_located(OrderPageLocators.STATUS_BTN))
            return True
        except:
            return False

    def order_scooter(self, first_name, last_name, address, metro_station, phone, delivery_date, rental_period):
        with allure.step("Шаг 1: Заполнение личных данных"):
            self.input_text(OrderPageLocators.NAME_INPUT, first_name)
            self.input_text(OrderPageLocators.LASTNAME_INPUT, last_name)
            self.input_text(OrderPageLocators.ADDRESS_INPUT, address)
            
            # Выбор станции метро
            self.input_text(OrderPageLocators.METRO_INPUT, metro_station)
            option_locator = OrderPageLocators.station_locator(metro_station)
            self.click_element(option_locator)
            
            self.input_text(OrderPageLocators.PHONE_FIELD, phone)

            # Переход на второй экран
            self.click_element(OrderPageLocators.NEXT_BTN)

        with allure.step("Шаг 2: Указание даты и срока аренды"):
            # Ввод даты доставки
            date_field = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT))
            date_field.clear()
            date_field.send_keys(delivery_date)
            time.sleep(0.5)  # Даём время календарю отреагировать

            # Закрываем календарь, чтобы он не мешал
            self.click_element(OrderPageLocators.ORDER_TITLE)

            # Выбор срока аренды
            self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
            period_option_locator = OrderPageLocators.period_locator(rental_period)
            self.click_element(period_option_locator)

        with allure.step("Шаг 3: Оформление заказа"):
            # Нажимаем "Заказать"
            self.click_element(OrderPageLocators.ORDER_BTN_PAGE)

            # Подтверждение заказа, если появилось модальное окно
            try:
                confirm_btn = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BTN_MODAL))
                with allure.step("Подтверждение заказа в модальном окне"):
                    confirm_btn.click()
            except:
                pass  # Модальное окно может не появиться

    def click_logo_self(self):
        with allure.step("Клик по логотипу Самоката"):
            self.click_element(OrderPageLocators.LOGO_SELF)

    def click_logo_yandex(self):
        with allure.step("Клик по логотипу Яндекса"):
            self.click_element(OrderPageLocators.LOGO_YANDEX)

