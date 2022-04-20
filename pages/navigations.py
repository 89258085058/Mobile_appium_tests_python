# -*- coding: utf-8 -*-
import string

import allure
from selenium.webdriver.common.by import By


class NavigationHelper:

    def __init__(self, app):
        self.app = app


    # Кнопки меню
    MenuButton = "//android.widget.Button[@content-desc='Open navigation menu']"
    MainPageButton = "//android.widget.Button[@content-desc=\"Главная\"]"
    ExitButton = "//*[@class='android.widget.Button' and @index='2']"
    PathButton = "//android.widget.Button[@content-desc='Разделы']"
    SensorsButton = "//android.widget.Button[@content-desc=\"Датчики\"]"
    JournalButton = "//android.widget.Button[@content-desc=\"Журнал\"]"
    DeviceButton = "//android.widget.Button[@content-desc=\"Устройства\"]"
    SettingsButton = "//android.widget.Button[@content-desc=\"Настройки\"]"

    def exitApp(self):
        with allure.step("Выход из приложения"):
            self.app.method.click((By.XPATH, str(self.MenuButton)))
            self.app.method.click((By.XPATH, str(self.MainPageButton)))
            self.app.method.click((By.XPATH, str(self.ExitButton)))

    def goToMainPage(self):
        with allure.step("Переход на страницу ГЛАВНАЯ"):
            self.app.method.click((By.XPATH, str(self.MenuButton)))
            self.app.method.click((By.XPATH, str(self.MainPageButton)))

    def goToPathPage(self):
        with allure.step("Переход на страницу РАЗДЕЛЫ"):
            self.app.method.click((By.XPATH, str(self.MenuButton)))
            self.app.method.click((By.XPATH, str(self.PathButton)))

    def goToSensorsPage(self):
        with allure.step("Переход на страницу ДАТЧИКИ"):
            self.app.method.click((By.XPATH, str(self.MenuButton)))
            self.app.method.click((By.XPATH, str(self.SensorsButton)))

    def goToJournalPage(self):
        with allure.step("Переход на страницу ЖУРНАЛ"):
            self.app.method.click((By.XPATH, str(self.MenuButton)))
            self.app.method.click((By.XPATH, str(self.JournalButton)))

    def goToDevicePage(self):
        with allure.step("Переход на страницу УСТРОЙСТВА"):
            self.app.method.click((By.XPATH, str(self.MenuButton)))
            self.app.method.click((By.XPATH, str(self.DeviceButton)))

    def goToSettingsPage(self):
        with allure.step("Переход на страницу НАСТРОЙКИ"):
            self.app.method.click((By.XPATH, str(self.MenuButton)))
            self.app.method.click((By.XPATH, str(self.SettingsButton)))

    def page_check(self):
        self.goToMainPage()
        self.goToPathPage()
        self.goToSensorsPage()
        self.goToJournalPage()
        self.goToDevicePage()
        self.goToSettingsPage()






