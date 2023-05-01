from .page import Page


class LoginPage(Page):
    ID = "com.ajaxsystems:id/"

    EMAIL_FIELD = ("id", f"{ID}login")
    PASSWORD_FIELD = ("id", f"{ID}password")
    NEXT_LOGIN_BTN = ("id", f"{ID}next")
    LOGIN_BTN = ('id', f"{ID}login")
    CHECK_LATER_BTN = ('id', f"{ID}cancel_button")
    WRONG_PASSWORD_EMAIL = ('id', f"{ID}snackbar_text")

    def click_login_start_screen(self):
        self.click(self.LOGIN_BTN)

    def input_email(self, email):
        self.send_keys(self.EMAIL_FIELD, email)

    def input_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_next_login_btn(self):
        self.click(self.NEXT_LOGIN_BTN)

    def check_later_btn(self):
        return self.click(self.CHECK_LATER_BTN)

    def message_incorrect_login(self):
        return self.get_element(self.WRONG_PASSWORD_EMAIL)

    def later_btn(self):
        return self.get_element(self.CHECK_LATER_BTN)
