from framework import LoginPage
from framework.home_page import HomePage


class Actions():
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    def login_actions(self, email, password):
        self.login_page.click_login_start_screen()
        self.login_page.input_email(email)
        self.login_page.input_password(password)
        self.login_page.click_next_login_btn()

    def assert_later_btn(self):
        return self.login_page.later_btn()

    def assert_negative_login(self):
        return self.login_page.message_incorrect_login()

    def side_bar_actions(self):
        self.login_actions("qa.ajax.app.automation@gmail.com", "qa_automation_password")
        self.home_page.click_later_btn()
        self.home_page.click_menu_drawer_btn()

    def assert_menu_addhuv(self):
        return self.home_page.menu_check_addhub_btn()

    def assert_menu(self):
        add_hub_btn = self.home_page.menu_check_addhub_btn()
        settings_btn = self.home_page.menu_check_settings_btn()
        help_btn = self.home_page.menu_check_help_btn()
        report_btn = self.home_page.menu_check_report_btn()
        agreement_btn = self.home_page.menu_check_agreenebt_btn()
        return add_hub_btn and settings_btn and help_btn and report_btn and agreement_btn

