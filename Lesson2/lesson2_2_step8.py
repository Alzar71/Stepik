from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1) # ждем загрузки страницы

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Aleksandr")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Zakharov")
	
    input3 = browser.find_element_by_name("email")
    input3.send_keys("a@mail.ru")	

    current_dir = os.path.abspath(os.path.dirname("lesson2_2_step8.py"))    # получаем путь к директории текущего исполняемого файла 
    #current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 

    input4 = browser.find_element_by_name("file")
    input4.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
	
finally:
    print(current_dir)
    print(file_path)
    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#