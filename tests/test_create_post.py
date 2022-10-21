import logging

from pages.utils import Post


class TestCreatePost:
    log = logging.getLogger("[CreatePost]")

    def test_create_post(self, hello_page):
        """
            Set up:
                Sign in as a user
            Steps:
                Create post
                Verify the message exists
                """
        create_post_menu = hello_page.open_the_create_post_dialog()
        post = Post()
        post.fill_default()
        create_post_menu.create_post(post)
        create_post_menu.verify_happy_post_was_created(post.body)

    def test_write_a_message(self, hello_page):
        """
            Set up:
                Sign in as a user
            Steps:
                Write a message
                Verify the message was written
                """
        create_post_dialog = hello_page.open_the_messenger()
        create_post_dialog.write_a_message()
        create_post_dialog.verify_the_message_exists()

