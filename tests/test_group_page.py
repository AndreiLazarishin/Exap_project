import logging

log = logging.getLogger(__name__)


class TestGroupPage:
    log = logging.getLogger("[GroupPage]")

    def test_create_group(self, hello_page):
        """
            Setup:
                Open the Group page
            Steps:
                Create a group
                Check the group is created
        """
        group_page = hello_page.open_the_groups_page()
        group_page.open_the_create_group_dialog()
        group_page.create_group()
        group_page.verify_the_group_is_created()

