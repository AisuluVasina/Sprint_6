import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls

@pytest.fixture
def driver():
    options = Options()
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def main_page(driver):
    #Фикстура для главной страницы
    page = MainPage(driver, Urls.MAIN_PAGE)
    page.open()
    return page


@pytest.fixture
def order_page(driver):
    #Фикстура для страницы заказа
    page = OrderPage(driver, Urls.ORDER_PAGE)
    return page

@pytest.fixture
def faq_page(driver):
    page = MainPage(driver, Urls.MAIN_PAGE)
    page.open_and_close_cookies()
    return page