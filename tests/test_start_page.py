import logging

log = logging.getLogger(__name__)


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    def test_empty_fields_alert(self, start_page):
        """
            Setup:
                Open the facebook.com
            Steps:
                Click on the login button
                Check the alert message
        """
        start_page.verify_empty_fields_alert()

    def test_change_localization(self, start_page):
        """
            Setup:
                Open the facebook.com
            Steps:
                Change the site localization
                Verify the changes applied
        """
        start_page.change_the_localization()

    def test_success_login(self, start_page, known_user):
        """
        Setup:
            Open the facebook.com site
        Steps:
            Fill in the email address field
            Clear the password field
            Click on the 'Log in' button
            Check if there is a 'Search' button
        """

        hello_page = start_page.sign_in(known_user)
        hello_page.verify_success_login()

    def test_logout(self, hello_page):
        """
        Setup:
            The user is logged in to facebook.com
        Steps:
            Click on the 'Log in' button
            Check if there is a 'Messenger' button
        """
        start_page = hello_page.log_out()
        start_page.verify_logged_out()
