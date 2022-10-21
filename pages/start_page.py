from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import log_decorator


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants

    @log_decorator
    def sign_in(self, user):
        """Sign in as user"""
        self.fill_field(xpath=self.constants.SIGN_IN_EMAIL_FIELD_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=user.password)
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    @log_decorator
    def verify_empty_fields_alert(self):
        """Verify empty fields alert"""
        self.click(self.constants.SIGN_IN_BUTTON_XPATH)
        assert self.get_element_text(
            xpath=self.constants.FIND_YOUR_ACC_XPATH) == self.constants.FIND_UR_ACC_TEXT

    @log_decorator
    def change_the_localization(self):
        """Change the localization to Ukrainian"""
        self.click(self.constants.SHOW_MORE_LANGUAGE_XPATH)
        self.click(self.constants.UKRAINIAN_LANGUAGE_OPTION_XPATH)
        assert self.get_element_text(
            xpath=self.constants.UKRAINIAN_ENTER_CREATE_ACC_XPATH) == \
            self.constants.UKRAINIAN_ENTER_CREATE_ACC_BUTTON_TEXT

    @log_decorator
    def verify_logged_out(self):
        """Verify the user logged out"""
        assert self.is_exists(xpath=self.constants.SIGN_IN_BUTTON_XPATH)
