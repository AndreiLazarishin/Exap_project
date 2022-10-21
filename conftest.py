import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User, rand_str


@pytest.fixture(scope='function')
def start_page():
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(DRIVER_PATH, chrome_options=options)
    driver.get(BASE_URL)
    driver.implicitly_wait(1.5)
    yield StartPage(driver)
    driver.close()


@pytest.fixture()
def random_group():
    group_name = rand_str(7)
    return group_name


@pytest.fixture()
def known_user():
    user = User()
    user.username = 'whoami7654321@gmail.com'
    user.password = 'Tester1234'
    return user


@pytest.fixture()
def hello_page(start_page, known_user):
    """Sign up as a user and return the page"""
    return start_page.sign_in(known_user)
