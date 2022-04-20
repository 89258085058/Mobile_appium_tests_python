from selenium.webdriver.common.by import By
from pages.authorization import AuthorizationHelper


class SessionHelper(AuthorizationHelper):


    def login(self, username, password):
        self.app.method.Input_values_xpath(username, AuthorizationHelper.login)
        self.app.method.Input_values_xpath(password, AuthorizationHelper.Password)
        self.app.method.click((By.XPATH, AuthorizationHelper.EntryButton))




