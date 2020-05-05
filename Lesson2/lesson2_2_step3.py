from selenium import webdriver
import time
import math

try: 
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # time.sleep(1) # ждем загрузки страницы

    x_element = browser.find_element_by_id("num1")
    # x = x_element.valuex # получили значение
    x1 = x_element.text
    x_element = browser.find_element_by_id("num2")
    x2 = x_element.text
    y = str(int(x1)+int(x2)) # вычислили результат

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(y) # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#