from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    el1 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group first_class']/input")
    el1.send_keys("blah")
    el2 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group second_class']/input")
    el2.send_keys("blah")
    el3 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group third_class']/input")
    el3.send_keys("blah")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()