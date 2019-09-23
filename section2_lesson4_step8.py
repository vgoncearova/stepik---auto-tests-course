from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc_y(x):
    return math.log(abs(12*math.sin(int(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button = browser.find_element_by_id('book')
button.click()

x_value = browser.find_element_by_id("input_value")
x = x_value.text

answer = calc_y(x)

input_field = browser.find_element_by_id("answer")
input_field.send_keys(str(answer))

submit_button = browser.find_element_by_id("solve")
submit_button.submit()
