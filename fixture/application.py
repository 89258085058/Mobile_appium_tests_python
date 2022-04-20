# -*- coding: utf-8 -*-

import allure
from allure_commons.types import AttachmentType
from appium import webdriver

from fixture.method import MethodsHelper
from pages.authorization import AuthorizationHelper
from fixture.session import SessionHelper
from pages.navigations import NavigationHelper


class Application:

    def __init__(self, url, android):
        desired_caps = android
        self.wd = webdriver.Remote(url, desired_caps)
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.authorization = AuthorizationHelper(self)
        self.method = MethodsHelper(self)
        self.navigations = NavigationHelper(self)

    def destroy(self):
        self.wd.quit()

    def get_screen(self):
        wd = self.wd
        allure.attach(wd.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
