from selenium.webdriver import Keys

from constants.hello_page import HelloPageConsts
from pages.base_page import BasePage

from pages.utils import log_decorator


class HelloPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HelloPageConsts()

    @log_decorator
    def open_the_create_post_dialog(self):
        """Open the create post dialog"""
        self.click(self.constants.CREATE_POST_INPUT_FIELD_XPATH)
        return HelloPage(self.driver)

    @log_decorator
    def create_post(self, post):
        """Create post"""
        self.fill_field(xpath=self.constants.CREATE_POST_INPUT_FIELD_INSIDE_THE_DIALOG, value=post.body)
        self.click(xpath=self.constants.ADD_FEELING_ACTIVITY_INSIDE_THE_POST_BUTTON_XPATH)
        self.click(xpath=self.constants.HAPPY_SMILE_FEELING_XPATH)
        self.click(xpath=self.constants.CREATE_POST_BUTTON)
        return HelloPage(self.driver)

    @log_decorator
    def verify_happy_post_was_created(self, actual_text):
        """Verify created message"""
        assert self.get_element_text(xpath=self.constants.VERIFY_CREATED_POST_XPATH.format(post_text=actual_text)) == \
               actual_text
        return HelloPage(self.driver)

    @log_decorator
    def open_the_messenger(self):
        """Open the messenger and find the guy"""
        self.click(xpath=self.constants.MESSENGER_BUTTON_XPATH)
        self.click(xpath=self.constants.MESSENGER_ADDRESAT_XPATH)
        return HelloPage(self.driver)

    @log_decorator
    def write_a_message(self):
        """Write a message via messenger"""
        self.fill_field(xpath=self.constants.MESSENGER_INPUT_FIELD, value="This is your problem now" + Keys.ENTER)

    @log_decorator
    def verify_the_message_exists(self):
        """Verify that message exists"""
        assert self.is_exists(xpath=self.constants.MESSENGER_PROVIDED_TEXT_XPATH)
        return HelloPage(self.driver)

    @log_decorator
    def update_the_cover_photo(self):
        """Update the cover photo"""
        self.click(self.constants.EDIT_COVER_PHOTO_BUTTON_XPATH)
        self.click(self.constants.UPDATE_PHOTO_IMAGE1_XPATH)
        self.click(self.constants.SAVE_CHANGES_BUTTON_XPATH)

    def delete_the_post(self, actual_text):
        """Delete the post"""
        self.get_element_text(
            xpath=self.constants.VERIFY_CREATED_POST_XPATH.format(post_text=actual_text))
        self.click(xpath=self.constants.DELETE_MESSAGE_BUTTON_XPATH)
        self.click(xpath=self.constants.CONFIRM_DELETE_BUTTON_XPATH)
        # assert not self.get_element_text(
        #     xpath=self.constants.VERIFY_CREATED_POST_XPATH.format(post_text=actual_text))

    def verify_the_post_was_deleted(self, post_text):
        """Verify the post was deleted"""
        assert not self.get_element_text(
            xpath=self.constants.VERIFY_CREATED_POST_XPATH.format(post_text=post_text))

    @log_decorator
    def verify_success_login(self):
        """Verify success login"""
        assert self.is_exists(xpath=self.constants.SEARCH_FIELD_XPATH)

    @log_decorator
    def log_out(self):
        """Log out the user"""
        self.click(self.constants.MY_PROFILE_BUTTON_XPATH)
        self.click(self.constants.LOG_OUT_BUTTON_XPATH)
        from pages.start_page import StartPage
        return StartPage(self.driver)

    @log_decorator
    def verify_logged_out(self):
        """Verify the user logged out"""
        assert not self.is_exists(xpath=self.constants.MESSENGER_BUTTON_XPATH)

    @log_decorator
    def open_the_groups_page(self):
        """Open the groups page"""
        self.click(self.constants.GROUPS_TAB_XPATH)
        from pages.groups_page import GroupsPage
        return GroupsPage(self.driver)

