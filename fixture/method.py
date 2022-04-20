# -*- coding: utf-8 -*-
import time

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class MethodsHelper:
    def __init__(self, app):
        self.app = app


    # Функция проверки ввода xpath
    def verification_value_xpath(self, input_value, assert_value, locator):
        self.Input_values_xpath(input_value, locator)
        time.sleep(1)
        self.Assert_values_xpath(assert_value, locator)

    # Ввод значений в поле xpath
    def Input_values_xpath(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
            element.click()
            element.clear()
            time.sleep(1)
            element.send_keys(value)
        except Exception as e:
            assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"

    # Проверка введенных значений в поле xpath
    def Assert_values_xpath(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
            values = element.get_attribute('text')
            assert str(value) == str(
                values), f"Ожидаемый результат ввода = '{value}' Фактическое значение в поле = '{values}'"
        except TimeoutException:
            print(f"Ошибка при проверке локатор поля ввода '{locator}' - не найден")

    # Проверка логина (ограничения по почте)
    def Assert_email_values_auth(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.ID, ('%s' % locator))))
            element.clear()
            element.send_keys(value)
            pas = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.ID, 'password')))
            pas.clear()
            pas.send_keys('Bolid911')
            button = wd.find_element_by_xpath('//*[@id="app"]//button[@class="BTN-primary btn-submit"]').get_attribute(
                'disabled')
            assert "true" == button, f"Атрибут кнопки войти disabled = '{button}'! Логин почты принмает невалидные данные: '{value}'"
        except Exception as e:
            assert e == TimeoutException, f"Ошибка при проверке локатор поля ввода '{locator}' - не найден"

    # Проверка логина (ограничения по почте)
    def Assert_email_values_auth_reset(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.ID, ('%s' % locator))))
            element.clear()
            element.send_keys(value)
            button = wd.find_element_by_xpath('//*[@id="app"]//button[@class="BTN-primary btn-submit"]').get_attribute(
                'disabled')
            assert "true" == button, f"Атрибут кнопки войти disabled = '{button}'! Логин почты принмает невалидные данные: '{value}'"
        except Exception as e:
            assert e == TimeoutException, f"Ошибка при проверке локатор поля ввода '{locator}' - не найден"

    # Проверка логина (ограничения по почте)
    def Assert_email_values_auth_fiz(self, value, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.ID, ('%s' % locator))))
            element.clear()
            element.send_keys(value)
            pas = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.ID, 'password')))
            pas.clear()
            pas.send_keys('Bolid911')
            pas = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.ID, 'rePassword')))
            pas.clear()
            pas.send_keys('Bolid911')
            button = wd.find_element_by_xpath('//*[@id="app"]//button[@class="BTN-primary btn-submit"]').get_attribute(
                'disabled')
            assert "true" == button, f"Атрибут кнопки войти disabled = '{button}'! Логин почты принмает невалидные данные: '{value}'"
        except Exception as e:
            assert e == TimeoutException, f"Ошибка при проверке локатор поля ввода '{locator}' - не найден"

    def click(self, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((locator)))
            element.click()
        except Exception as e:
            assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"

    def click_by_visible(self, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_located_to_be_selected((locator)))
            element.click()
        except Exception as e:
            assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"


    def find_element_text(self, locator):
        wd = self.app.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, ('%s' % locator))))
        return element.text
