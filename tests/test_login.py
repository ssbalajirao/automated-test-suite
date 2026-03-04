import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLogin:
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        dashboard = DashboardPage(driver)
        assert dashboard.is_dashboard_loaded()

    def test_invalid_username(self, driver):
        login_page = LoginPage(driver)
        login_page.login("invalidUser", "secret_sauce")

        assert login_page.is_error_there()

    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user","wrongPasscode")

        assert login_page.is_error_there()
    
    def test_empty_username(self, driver):
        login_page  = LoginPage(driver)
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        assert login_page.is_error_there()

    def test_empty_password(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.click_login()

        assert login_page.is_error_there()

class TestDashboard:
    
    def test_inventory_products_displayed(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        dashboard = DashboardPage(driver)
        product_count = dashboard.product_count()

        assert product_count > 0

