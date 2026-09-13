import pytest
import allure
from pages.main_page import MainPage
from data.order_data import FAQData

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

@allure.feature("Яндекс.Самокат: Вопросы о важном (FAQ)")
@allure.description("Проверка корректного раскрытия ответов в аккордеоне")
class TestFAQ:
    
    @pytest.fixture
    def page(self, driver):
        page = MainPage(driver, BASE_URL)
        page.open_and_close_cookies()
        return page

    # передаем индекс и конкретный текст
    @pytest.mark.parametrize("index", list(range(8)))
    @allure.title("Тест FAQ: Проверка вопроса №{index}")
    def test_faq_item(self, page, index):
        expected_text = FAQData.answers[index]  # Получаем текст по индексу
        
        # Шаг 1: Раскрываем вопрос
        page.expand_accordion_item(index)
        
        # Шаг 2: Проверяем видимость
        assert page.is_answer_visible(index), f"Ответ на вопрос №{index} не отобразился"
        
        # Шаг 3: Проверяем текст
        actual_text = page.get_answer_text(index)
        
        allure.attach(actual_text, name=f"Фактический текст ответа №{index}", attachment_type=allure.attachment_type.TEXT)
        allure.attach(expected_text, name=f"Ожидаемый текст ответа №{index}", attachment_type=allure.attachment_type.TEXT)
        
        assert actual_text == expected_text, f"Текст ответа №{index} не совпадает"