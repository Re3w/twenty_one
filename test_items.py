import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_search_button_add_to_cart(browser):
    browser.get(link)
    time.sleep(30)#browser.implicitly_wait(10)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button, "Искомый элемент не найден"
