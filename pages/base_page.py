import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step("Открытие страницы")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Клик по элементу {locator}")
    def click_element(self, locator, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        
            # Пробуем проскроллить к элементу, если он вне зоны видимости
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
            # Ждем, пока элемент станет кликабельным
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        
            element.click() 
        
        except TimeoutException:
            self.driver.save_screenshot("error_screenshot.png")
            raise

    @allure.step("Ввод текста {text} в поле {locator}")
    def input_text(self, locator, text, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_visibility(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Ожидание появления нового окна")
    def wait_for_new_window(self, current_count, timeout=10):
        # Ожидает, пока не появится новое окно
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > current_count
        )       