import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.url)

    @allure.step("Клик по элементу {locator}")
    def click_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        # JS клик надежнее для React элементов
        self.driver.execute_script("arguments[0].click();", element)

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