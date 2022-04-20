import json
import os

import pytest
from fixture.application import Application

import logging
import allure



target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture(autouse=True)
def app():
    global fixture
    url = load_config("target.json")['appium_server']['Url']
    android = load_config("target.json")['desired_caps']
    fixture = Application(url, android)
    return fixture

@pytest.fixture()
def auth(app):
    logAndPass = load_config("target.json")['admin']
    app.session.login(username=logAndPass["username"], password=logAndPass["password"])


@pytest.fixture(autouse=True)
def app_close(app):
    yield fixture
    try:
        app.navigations.exitApp()
        fixture.destroy()
    except:
        fixture.destroy()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    result = yield
    report = result.get_result()
    if report.longrepr:
        logging.error('FAILED: %s', report.longrepr)
    else:
        logging.info('Did not fail...')
    if report.outcome == 'failed':
        with allure.step('Скриншот браузера при падении теста'):
            fixture.get_screen()
            logging.error('FAILED: %s', report.longrepr)
    elif report.outcome == 'skipped':
        logging.info('Skipped')
    else:
        logging.info('Passed')


