from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

el = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )

button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_id("input_value")
#x = x_element.valuex # получили значение
x = x_element.text
y = calc(int(x)) # вычислили результат

inpt = browser.find_element_by_id("answer")
inpt.send_keys(y) # внесли значение    
	
button2 = browser.find_element_by_id("solve")
button2.click()

assert "successful" in message.text
