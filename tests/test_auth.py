# -*- coding: utf-8 -*-
import allure
import pytest

reruns = 0

@allure.epic("Тесты авторизация")
@allure.feature("Проверки на валидацию")
@pytest.mark.flaky(reruns=reruns)
class TestAuthValidation():

    @allure.story("ЛОГИН")
    @allure.title("Проверка ввода значений в поле")
    def test_login_input_data(self, app):
        with allure.step("Проверка ввода значений в поле логин"):
            app.authorization.input_login_data()

    @allure.story("ЛОГИН")
    @allure.title("Проверка ограничений по email")
    def test_login_input_data_email(self, app):
        with allure.step("Проверка ввода значений в поле логин"):
            app.authorization.input_login_data_email()

    @allure.story("ПАРОЛЬ")
    @allure.title("Проверка ввода значений в поле")
    def test_password_input_data(self, app):
        with allure.step("Проверка ввода значений в поле логин"):
            app.authorization.input_password_data()

    @allure.story("Маршрутизация")
    @allure.title("Проверка перехода по страницам приложения")
    def test_navigation_check(self, app, auth):
        with allure.step("Переход по страницам"):
            app.navigations.page_check()




