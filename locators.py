from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки заказа
    BTN_ORDER_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]")
    BTN_ORDER_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button')]")
    
    # Логотипы
    LOGO_SELF = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    
    # Cookie баннер
    COOKIE_BTN = (By.ID, "rcc-confirm-button")

    # --- ЛОКАТОРЫ АККОРДЕОНА (FAQ) ---
    ACCORDION_HEADER_TEMPLATE = "//div[@id='accordion__heading-{}']"
    ACCORDION_PANEL_TEMPLATE = "//div[@id='accordion__panel-{}']"

    # Локатор для поиска ВСЕХ заголовков аккордеона
    ALL_ACCORDION_HEADERS = (By.XPATH, "//div[starts-with(@id, 'accordion__heading-')]")

class OrderPageLocators:
    # --- ГЛАВНАЯ: Кнопки заказа ---
    BTN_ORDER_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[contains(text(), 'Заказать')]")
    BTN_ORDER_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[contains(text(), 'Заказать')]")
    
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    # Поле "Станция метро" 
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    
    # Выпадающий список станций 
    METRO_OPTION = (By.XPATH, "//div[@class='select-search__input' and contains(text(), '{}')]")  # подставляем имя
    METRO_OPTIONS_CONTAINER = (By.CLASS_NAME, "select-search__input")

    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BTN = (By.XPATH, "//button[text()='Далее']")
    
    # --- ФОРМА: Шаг 2 ---
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[text()='* Срок аренды']")
    ORDER_TITLE = (By.XPATH, "//div[text()='Про аренду']") 
    
    # --- ДЕЙСТВИЯ И МОДАЛКИ ---
    ORDER_BTN_PAGE = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    CONFIRM_BTN_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    
    # --- ПОДТВЕРЖДЕНИЕ УСПЕХА (Кнопка статуса) ---
    STATUS_BTN = (By.XPATH, "//button[text()='Посмотреть статус']")
    
    # --- ЛОГОТИПЫ ---
    LOGO_SELF = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    
    # --- ДЗЕН (для проверки открытия) ---
    DZEN_NEWS_BLOCK = (By.CSS_SELECTOR, ".news-feed")

    @staticmethod
    def station_locator(station: str):
        return (By.XPATH, f"//div[contains(text(),'{station}')]")

    @staticmethod
    def period_locator(period: str):
        return (By.XPATH, f"//div[contains(text(),'{period}')]")