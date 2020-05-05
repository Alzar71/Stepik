from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1) # ждем загрузки страницы

    first_window = browser.window_handles[0]
    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id("input_value")
    #x = x_element.valuex # получили значение
    x = x_element.text
    y = calc(int(x)) # вычислили результат

    inpt = browser.find_element_by_id("answer")
    inpt.send_keys(y) # внесли значение    
	
    button = browser.find_element_by_css_selector("button.btn")
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