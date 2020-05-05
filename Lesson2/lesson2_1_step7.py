from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1) # ждем загрузки страницы

    x_element = browser.find_element_by_id("treasure")
    # x = x_element.valuex # получили значение
    x = x_element.get_attribute("valuex")
    y = calc(x) # вычислили результат

    inpt = browser.find_element_by_id("answer")
    inpt.send_keys(y) # внесли значение

    opt1 = browser.find_element_by_id("robotCheckbox")
    opt1.click()

    opt2 = browser.find_element_by_id("robotsRule")
    opt2.click()

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