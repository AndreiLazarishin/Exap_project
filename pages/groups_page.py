from constants.groups import GroupPageConsts
from pages.base_page import BasePage
from pages.utils import rand_str, log_decorator


class GroupsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = GroupPageConsts

    @log_decorator
    def open_the_create_group_dialog(self):
        """Open the create group dialog"""
        self.click(self.constants.CREATE_NEW_GROUP_BUTTON_XPATH)

    @log_decorator
    def create_group(self, random_group=rand_str(7)):
        """Create the group"""
        self.click(self.constants.CHOOSE_PRIVACY_MENU_XPATH)
        self.click(self.constants.PUBLIC_GROUP_OPTION_XPATH)
        self.click(self.constants.GROUP_NAME_INPUT_FIELD_XPATH)
        self.fill_field(self.constants.GROUP_NAME_INPUT_FIELD_XPATH, value=random_group)
        self.click(self.constants.CREATE_GROUP_BUTTON_XPATH)

    @log_decorator
    def verify_the_group_is_created(self):
        """Verify the group is created"""
        assert self.is_exists(xpath=self.constants.MORE_BUTTON_XPATH)
        return GroupsPage(self.driver)

    @log_decorator
    def leave_the_group(self):
        """Leave the group"""
        self.click(self.constants.MORE_BUTTON_XPATH)
        self.click(self.constants.LEAVE_GROUP_BUTTON_XPATH)
        self.click(self.constants.LEAVE_GROUP_CONFIRMATION_BUTTON_XPATH)
        return GroupsPage(self.driver)

    @log_decorator
    def confirm_the_group_is_deleted(self):
        """Confirm the group is deleted"""
        assert self.is_exists(xpath=self.constants.CREATE_NEW_GROUP_BUTTON_XPATH)
