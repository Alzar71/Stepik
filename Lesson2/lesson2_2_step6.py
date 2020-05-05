from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = " http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1) # ждем загрузки страницы

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text # получили значение
    y = calc(x) # вычислили результат

    inpt = browser.find_element_by_id("answer")
    inpt.send_keys(y) # внесли значение

    opt1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    opt1.click()

    opt2 = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", opt2)
    opt2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#