import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path=r'C:\Users\chiz-\PycharmProjects\test_Google\venv\Scripts\chromedriver.exe')
    yield driver
    driver.quit()