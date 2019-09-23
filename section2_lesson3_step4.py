from selenium import webdriver
import math


def calc_y(x):
    return math.log(abs(12*math.sin(int(x))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_tag_name('button')
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_value = browser.find_element_by_id("input_value")
x = x_value.text

answer = calc_y(x)

input_field = browser.find_element_by_id("answer")
input_field.send_keys(str(answer))

submit_button = browser.find_element_by_tag_name("button")
submit_button.submit()
