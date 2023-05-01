from framework.page import Page


class HomePage(Page):
    ID = "com.ajaxsystems:id/"
    LATER_BTN = ('id', f"{ID}cancel_button")
    MENU_DRAWER_BTN = ('id', f"{ID}menuDrawer")
    ADD_HUB_BTN = ('id', f"{ID}addHub")
    APP_SETTINGS_BTN = ('id', f"{ID}settings")
    HELP_BTN = ('id', f"{ID}settings")
    REPORT_A_PROPLEM_BTN = ('id', f"{ID}logs")
    END_USER_AGREEMENT = ("id",f"{ID}agreementText")

    def check_later_btn(self):
        return self.get_element(self.LATER_BTN)

    def click_later_btn(self):
        return self.click(self.LATER_BTN)

    def click_menu_drawer_btn(self):
        return self.click(self.MENU_DRAWER_BTN)

    def menu_check_addhub_btn(self):
        return self.get_element(self.ADD_HUB_BTN)

    def menu_check_settings_btn(self):
        return self.get_element(self.APP_SETTINGS_BTN)

    def menu_check_help_btn(self):
        return self.get_element(self.HELP_BTN)

    def menu_check_report_btn(self):
        return self.get_element(self.REPORT_A_PROPLEM_BTN)

    def menu_check_agreenebt_btn(self):
        return self.get_element(self.END_USER_AGREEMENT)