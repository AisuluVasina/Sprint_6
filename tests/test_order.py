import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import OrderData
from urls import Urls

@allure.feature("Яндекс.Самокат: Оформление заказа и навигация")
@allure.feature('Заказы')
class TestOrder:

    @pytest.fixture
    def main_page(self, driver):
        page = MainPage(driver, Urls.MAIN_PAGE)
        page.open() 
        return page

    @pytest.fixture
    def order_page(self, driver):
        page = OrderPage(driver, Urls.ORDER_PAGE)
        page.open()
        return page

    @allure.title('Проверка верхней кнопки заказа')
    @allure.description('Находим сверху кнопку Заказа и нажимаем на нее. Проверяем переход на страницу заказа.')
    def test_top_order_button(self, main_page):
        main_page.open()
        main_page.click_top_order_btn()
        # проверяем, что URL изменился на страницу заказа
        assert main_page.get_current_url() == Urls.ORDER_PAGE, f"Верхняя кнопка заказа ведёт на неправильную страницу. Ожидалось: {Urls.ORDER_PAGE}, Получено: {main_page.get_current_url()}"

    @allure.title('Проверка нижней кнопки заказа')
    @allure.description('Находим снизу кнопку Заказа и нажимаем на нее. Проверяем переход на страницу заказа.')
    def test_bottom_order_button(self, main_page):
        main_page.open()
        main_page.click_bottom_order_btn()
        # проверяем, что URL изменился на страницу заказа
        assert main_page.get_current_url() == Urls.ORDER_PAGE, f"Нижняя кнопка заказа ведёт на неправильную страницу. Ожидалось: {Urls.ORDER_PAGE}, Получено: {main_page.get_current_url()}"

    @allure.title('Полная процедура заказа самоката через верхнюю кнопку')
    @pytest.mark.parametrize(OrderData.param, OrderData.value)
    def test_order_scooter_via_top_button(self, main_page, order_page, first_name, last_name, address, metro_station, phone, delivery_date, rental_period):
        main_page.open()
        main_page.click_top_order_btn()
        
        # Выполняем полный флоу заказа
        order_page.order_scooter(first_name, last_name, address, metro_station, phone, delivery_date, rental_period)
        
        # проверяем наличие кнопки статуса (подтверждение успеха)
        assert order_page.find_status_button() == True, "Кнопка 'Посмотреть статус' не появилась после оформления заказа через верхнюю кнопку"

    @allure.title('Полная процедура заказа самоката через нижнюю кнопку')
    @pytest.mark.parametrize(OrderData.param, OrderData.value)
    def test_order_scooter_via_bottom_button(self, main_page, order_page, first_name, last_name, address, metro_station, phone, delivery_date, rental_period):
        main_page.open()
        main_page.click_bottom_order_btn()
        
        # Выполняем полный флоу заказа
        order_page.order_scooter(first_name, last_name, address, metro_station, phone, delivery_date, rental_period)
        
        # проверяем наличие кнопки статуса (подтверждение успеха)
        assert order_page.find_status_button() == True, "Кнопка 'Посмотреть статус' не появилась после оформления заказа через нижнюю кнопку"

    @allure.title('Переходим на главную страницу через лого "Самокат"')
    def test_scooter_logo_redirect(self, main_page, order_page):  # ← добавили order_page
        order_page.open()  # Открываем страницу заказа
        main_page.click_to_scooter()
        assert main_page.get_current_url() == Urls.MAIN_PAGE, f"Не вернулись на главную. Ожидалось: {Urls.MAIN_PAGE}, Получено: {main_page.get_current_url()}"

    @allure.title('Переходим на яндекс дзен через главное лого')
    def test_yandex_logo_redirect(self, main_page, order_page):  # ← добавили order_page
        order_page.open()  # Открываем страницу заказа
        current_window_count = len(main_page.driver.window_handles)
        main_page.click_to_yandex_logo()

        # Ждём новое окно
        import time
        time.sleep(2)
        assert len(main_page.driver.window_handles) > current_window_count, "Новое окно не открылось после клика по логотипу Яндекса"

        # Переключаемся на новое окно
        main_page.switch_to_window(1)

        # Проверяем URL
        assert Urls.DZEN_URL in main_page.get_current_url(), f"Не открылся Дзен. Текущий URL: {main_page.get_current_url()}"

        # Возвращаемся обратно
        main_page.switch_to_window(0)
    