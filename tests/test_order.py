import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import OrderData
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait

@allure.feature("Яндекс.Самокат: Оформление заказа и навигация")
@allure.feature('Заказы')
class TestOrder:

    @allure.title('Проверка верхней кнопки заказа')
    @allure.description('Кликаем по верхней кнопке "Заказать" и проверяем переход на страницу заказа.')
    def test_top_order_button(self, main_page):
        main_page.click_top_order_btn()
        assert main_page.get_current_url() == Urls.ORDER_PAGE, \
            f"Верхняя кнопка заказа ведёт на неправильную страницу. Ожидалось: {Urls.ORDER_PAGE}, Получено: {main_page.get_current_url()}"


    @allure.title('Проверка нижней кнопки заказа')
    @allure.description('Кликаем по нижней кнопке "Заказать" и проверяем переход на страницу заказа.')
    def test_bottom_order_button(self, main_page):
        main_page.click_bottom_order_btn()
        assert main_page.get_current_url() == Urls.ORDER_PAGE, \
            f"Нижняя кнопка заказа ведёт на неправильную страницу. Ожидалось: {Urls.ORDER_PAGE}, Получено: {main_page.get_current_url()}"


    @allure.title('Полная процедура заказа самоката через верхнюю кнопку')
    @pytest.mark.parametrize(OrderData.param, OrderData.value)
    def test_order_scooter_via_top_button(self, main_page, order_page, first_name, last_name, address, metro_station, phone, delivery_date, rental_period):
        main_page.click_top_order_btn()
        order_page.order_scooter(first_name, last_name, address, metro_station, phone, delivery_date, rental_period)
        assert order_page.find_status_button(), "Кнопка 'Посмотреть статус' не появилась после оформления заказа через верхнюю кнопку"


    @allure.title('Полная процедура заказа самоката через нижнюю кнопку')
    @pytest.mark.parametrize(OrderData.param, OrderData.value)
    def test_order_scooter_via_bottom_button(self, main_page, order_page, first_name, last_name, address, metro_station, phone, delivery_date, rental_period):
        main_page.click_bottom_order_btn()
        order_page.order_scooter(first_name, last_name, address, metro_station, phone, delivery_date, rental_period)
        assert order_page.find_status_button(), "Кнопка 'Посмотреть статус' не появилась после оформления заказа через нижнюю кнопку"


    @allure.title('Переходим на главную страницу через лого "Самокат"')
    def test_scooter_logo_redirect(self, main_page, order_page):
        main_page.click_to_scooter()
        assert main_page.get_current_url() == Urls.MAIN_PAGE, \
            f"Не вернулись на главную. Ожидалось: {Urls.MAIN_PAGE}, Получено: {main_page.get_current_url()}"


    @allure.title('Переходим на Яндекс.Дзен через лого "Яндекс"')
    def test_yandex_logo_redirect(self, main_page, order_page):
        current_window_count = len(main_page.driver.window_handles)
        main_page.click_to_yandex_logo()

        # Ожидание открытия нового окна
        main_page.wait_for_new_window(current_window_count)
        main_page.switch_to_window(1)

        # Ждём, пока вкладка загрузится (URL сменится с about:blank)
        WebDriverWait(main_page.driver, 15).until(
            lambda driver: "dzen.ru" in driver.current_url
        )

        assert Urls.DZEN_URL in main_page.get_current_url(), \
            f"Не открылся Дзен. Текущий URL: {main_page.get_current_url()}"

        # Возвращаемся в исходное окно
        main_page.switch_to_window(0)
    