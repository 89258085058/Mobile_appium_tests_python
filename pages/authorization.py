# -*- coding: utf-8 -*-
import string

import allure
from selenium.webdriver.common.by import By


class AuthorizationHelper:

    def __init__(self, app):
        self.app = app

    login = "//*[@class='android.widget.EditText' and @index='3']"
    Password = "//*[@class='android.widget.EditText' and @index='5']"
    OpenPasswordSecret = "//*[@class='android.widget.Button' and @index='0']"
    EntryButton = "//*[@class='android.widget.Button' and @index='6']"

    # Проверка ввода поле ЛОГИН
    def input_login_data(self, locator=str(login)):
        with allure.step("Ввод Цифр"):
            self.app.method.verification_value_xpath(string.digits, string.digits + ", Введите почту", locator)
        with allure.step("Ввод Латиницы"):
            self.app.method.verification_value_xpath(string.ascii_letters, string.ascii_letters + ", Введите почту",
                                                     locator)
        with allure.step("Ввод Русских букв"):
            self.app.method.verification_value_xpath("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", ', Введите почту', locator)
            self.app.method.verification_value_xpath("ёйцукенгшщзхъфывапролджэячсмитьбю", ', Введите почту', locator)
        with allure.step("Ввод Спецсимволов"):
            self.app.method.verification_value_xpath("!#$%&'()*+,-./:;<=>?@[]^_`{|}~",
                                                     "!#$%&'()*+,-./:;<=>?@[]^_`{|}~, Введите почту",
                                                     locator)
        with allure.step("Ввод Совместных значений(спецсимволы/буквы/цифры)"):
            self.app.method.verification_value_xpath('123  АБВABC!@#', '123ABC!@#, Введите почту', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.verification_value_xpath('   ', ', Введите почту', locator)
            self.app.method.verification_value_xpath('123     ', '123, Введите почту', locator)
            self.app.method.verification_value_xpath('   123', '123, Введите почту', locator)
            self.app.method.verification_value_xpath('1 2 3', '123, Введите почту', locator)
        with allure.step("Проверка границ ввода"):
            self.app.method.verification_value_xpath('a', 'a, Введите почту', locator)
            self.app.method.verification_value_xpath('a' * 253, 'a' * 253 + ", Введите почту", locator)
            self.app.method.verification_value_xpath('a' * 254, 'a' * 254 + ", Введите почту", locator)
            self.app.method.verification_value_xpath('a' * 255, 'a' * 254 + ", Введите почту", locator)

    # Проверка ввода поле Пароль
    def input_password_data(self, locator=str(Password)):
        with allure.step("Раскрыитие пароля для просмотра"):
            self.app.method.click((By.XPATH, str(self.OpenPasswordSecret)))
        with allure.step("Ввод Цифр"):
            self.app.method.verification_value_xpath(string.digits, string.digits + ", Введите пароль", locator)
        with allure.step("Ввод Латиницы"):
            self.app.method.verification_value_xpath(string.ascii_letters, string.ascii_letters + ", Введите пароль",
                                                     locator)
        with allure.step("Ввод Русских букв"):
            self.app.method.verification_value_xpath("АПРОЛДЖЭЯЧСМИТЬБЮЁЙЦУКЕНГШЩЗХЪФЫВ", ', Введите пароль', locator)
            self.app.method.verification_value_xpath("ёйцукенгшщзхъфывапролджэячсмитьбю", ', Введите пароль', locator)
        with allure.step("Ввод Спецсимволов"):
            self.app.method.verification_value_xpath("!#$%&'()*+,-.:;<=>?@[]^_{|}~",
                                                     "!#$%&()*+,-.:;<=>?@[]^_{|}~, Введите пароль",
                                                     locator)
        with allure.step("Ввод Совместных значений(спецсимволы/буквы/цифры)"):
            self.app.method.verification_value_xpath('123  АБВABC!@#', '123ABC!@#, Введите пароль', locator)
        with allure.step("Проверка ввода пробелов"):
            self.app.method.verification_value_xpath('   ', ', Введите пароль', locator)
            self.app.method.verification_value_xpath('123     ', '123, Введите пароль', locator)
            self.app.method.verification_value_xpath('   123', '123, Введите пароль', locator)
            self.app.method.verification_value_xpath('1 2 3', '123, Введите пароль', locator)
        with allure.step("Проверка границ ввода"):
            self.app.method.verification_value_xpath('a', 'a, Введите пароль', locator)
            self.app.method.verification_value_xpath('a' * 253, 'a' * 253 + ", Введите пароль", locator)
            self.app.method.verification_value_xpath('a' * 254, 'a' * 254 + ", Введите пароль", locator)
        self.app.method.click((By.XPATH, str(self.OpenPasswordSecret)))

    # Проверка ввода поле ЛОГИН ограничение email
    def input_login_data_email(self, locator='email'):
        with allure.step(
                "Проверка ограничение на ввод для почты (символ точки (.) является последним в локальной части)"):
            self.app.method.Assert_email_values_auth('g123.@Example.com', locator)
        with allure.step("Проверка ограничение на ввод для почты (символ точки (.) два раза подряд)"):
            self.app.method.Assert_email_values_auth('g123..123@example.com', locator)
        with allure.step("Проверка ограничение на ввод для почты (только один допускается вне кавычек)"):
            self.app.method.Assert_email_values_auth('b@l@a@example.com', locator)
        with allure.step("Проверка ограничение на ввод для почты (символ отсутствует)"):
            self.app.method.Assert_email_values_auth('', locator)
