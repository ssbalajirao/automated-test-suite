import pytest
from selenium import webdriver
from config.config import config


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if config.HEADLESS:
        options.add_argument("--headless")


    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(config.WAIT_TIME)
    driver.get(config.BASE_URL)

    yield driver

    driver.quit()