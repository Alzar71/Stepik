from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_link_text"
#link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    s=str(math.ceil(math.pow(math.pi, math.e)*10000))
    #s="224592"
    #lnk = browser.find_element_by_link_text("» "+s)
    lnk = browser.find_element_by_partial_link_text(s)
    lnk.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Aleksandr")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Zakharov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Kronshtadt")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла