from selenium import webdriver
from selenium.webdriver import ActionChains
import time

def test_func():
    driver = webdriver.Remote(
        command_executor='http://localhost:9999',
        desired_capabilities={
            "app": r"C:\Users\chiz-\PycharmProjects\test_Google\venv"
        })
    window = driver.find_element_by_name('Выбрать файл').click()
