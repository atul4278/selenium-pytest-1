import os
from configparser import ConfigParser

import pytest
from _pytest.fixtures import FixtureRequest

from utils.driver_manager import get_driver_object


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="DEV", help="environment against which tests to be executed")
    parser.addoption("--browser", action='store', default="chrome", help="browser on which tests to be executed")


@pytest.fixture(scope="session")
def environment(request: FixtureRequest):
    env = request.config.getoption("--env").upper()
    os.environ["TEST_ENV"] = env
    yield env


@pytest.fixture(scope="session")
def browser(request: FixtureRequest):
    yield request.config.getoption("--browser")


@pytest.fixture(scope="session")
def config(environment, pytestconfig):
    config_object = ConfigParser()
    config_object.read(os.path.join(pytestconfig.rootpath, 'config.ini'))
    yield config_object[environment]


@pytest.fixture(scope='session')
def driver(browser):
    driver = get_driver_object(browser=browser)
    yield driver
    driver.quit()
