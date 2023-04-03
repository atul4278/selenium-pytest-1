import logging
import os
from configparser import ConfigParser

import pytest
from _pytest.fixtures import FixtureRequest

from utils.driver_manager import get_driver_object


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="DEV", help="environment against which tests to be executed")
    parser.addoption("--browser", action='store', default="chrome", help="browser on which tests to be executed")


def pytest_configure(config):
    worker_id = os.environ.get("PYTEST_XDIST_WORKER")
    if worker_id is not None:
        logging.basicConfig(
            datefmt=config.getini("log_file_date_format"),
            format=config.getini("log_file_format"),
            filename=f"logs/tests_{worker_id}.log",
            level=config.getini("log_file_level"),
        )


def pytest_runtest_logstart(nodeid: str):
    logging.info("-" * 100)
    logging.info(nodeid)
    logging.info("-" * 100)


def pytest_report_teststatus(report):
    if report.when == 'call':
        logging.info("-" * 100)
        logging.info(f"{report.outcome.upper()} ==> {report.nodeid}")
        logging.info("-" * 100)


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
