import pytest
import allure
from pages.main_page import MainPage
from data.order_data import FAQData
from urls import Urls
#from conftest.faq_page import FAQPage

@allure.feature("Яндекс.Самокат: Вопросы о важном (FAQ)")
@allure.description("Проверка корректного раскрытия ответов в аккордеоне")
class TestFAQ:

    # передаем индекс и конкретный текст
    @pytest.mark.parametrize("index", list(range(8)))
    @allure.title("Тест FAQ: Проверка вопроса №{index}")
    def test_faq_item(self, faq_page, index):
        expected_text = FAQData.answers[index]  # Получаем текст по индексу
        
        with allure.step(f"Раскрыть вопрос №{index}"):
            faq_page.expand_accordion_item(index)

        with allure.step(f"Проверить, что ответ на вопрос №{index} отобразился"):
            assert faq_page.is_answer_visible(index), f"Ответ на вопрос №{index} не отобразился"

        with allure.step(f"Проверить текст ответа на вопрос №{index}"):
            actual_text = faq_page.get_answer_text(index)
        
            allure.attach(actual_text, name=f"Фактический текст ответа №{index}", attachment_type=allure.attachment_type.TEXT)
            allure.attach(expected_text, name=f"Ожидаемый текст ответа №{index}", attachment_type=allure.attachment_type.TEXT)
        
            assert actual_text == expected_text, f"Текст ответа №{index} не совпадает"