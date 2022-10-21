class HelloPageConsts:
    SEARCH_FIELD_XPATH = './/input[@aria-label="Search Facebook"]'
    CREATE_POST_INPUT_FIELD_XPATH = './/span[@class="x1lliihq x6ikm8r x10wlt62 x1n2onr6"]'
    MY_PROFILE_BUTTON_XPATH = './/*[@aria-label="Your profile"]'
    LOG_OUT_BUTTON_XPATH = './/*[text()="Log Out"]'
    GROUPS_TAB_XPATH = './/*[@aria-label="Groups"]'

    # Profile part
    EDIT_COVER_PHOTO_BUTTON_XPATH = './/span[text()="Edit Cover Photo"]'
    SELECT_PHOTO_BUTTON_XPATH = './/span[text()="Select photo"]'
    UPDATE_PHOTO_IMAGE1_XPATH = './/img[@alt="May be an image of mountain, nature and sky"]'
    UPDATE_THE_IMAGE2_PHOTO_XPATH = './/img[@alt="May be an image of mountain, sky and nature"]'
    SAVE_CHANGES_BUTTON_XPATH = './/div[@aria-label="Save changes" and @role="button" and @tabindex="0"]'
    EDIT_PROFILE_BUTTON_XPATH = './/*[text()="Edit profile"]'
    EDIT_BIO_BUTTON_XPATH = "//div[contains(@aria-label, 'Edit Bio')]"
    BIO_TEXTAREA_XPATH = './/textarea[@placeholder="Describe who you are"]'
    SAVE_BIO_UPDATES_BUTTON = './/*[text()="Save"]'
    SUCCESSFULLY_SAVED_TEXT_XPATH = './/*[text()="Saved"]'
    SKIP_BUTTON_XPATH = './/*[@aria-label="Skip"]'

    # Post part
    CREATE_POST_BUTTON = './/div[@aria-label="Post" and @role="button"]'
    VERIFY_CREATED_POST_XPATH = './/*[text()="{post_text}"]'
    VERIFY_CREATED_POST_TEXT = '"{post_text}"'
    LIKE_POST_BUTTON_XPATH = './/span[text()="Like"]'
    COMMENT_POST_BUTTON_XPATH = './/span[text()="Comment"]'
    SHARE_POST_BUTTON_XPATH = './/span[text()="Share"]'
    HAPPY_SMILE_FEELING_XPATH = './/div[@aria-label="happy"]'
    CREATE_POST_INPUT_FIELD_INSIDE_THE_DIALOG = './/p[@class="x16tdsg8 x1mh8g0r xat24cr x11i5rnm xdj266r"]'
    ADD_PHOTO_VIDEO_TO_POST_INSIDE_THE_POST_BUTTON_XPATH = './/div[@aria-label="Photo/Video"]'
    TAG_PEOPLE_INSIDE_THE_POST_BUTTON_XPATH = './/div[@aria-label="Tag people"]'
    ADD_FEELING_ACTIVITY_INSIDE_THE_POST_BUTTON_XPATH = './/div[@aria-label="Feeling/activity"]'
    ADD_CHECK_IN_INSIDE_THE_POST_BUTTON_XPATH = './/div[@aria-label="Check in"]'
    ADD_LIFE_EVENT_INSIDE_THE_POST_BUTTON_XPATH = './/div[@aria-label="Life event"]'
    DELETE_MESSAGE_BUTTON_XPATH = './/span[text()="Move to Recycle bin"]'
    CONFIRM_DELETE_BUTTON_XPATH = './/span[text()="Move"]'

    # Messenger part
    MESSENGER_BUTTON_XPATH = './/div[@aria-label="Messenger" and @role="button" and @tabindex="0"]'
    SEARCH_MESSENGER_FIELD_XPATH = './/*[@aria-label="Search Messenger"]'
    MESSENGER_ADDRESAT_XPATH = './/*[text()="Stepan Bandera"]'
    MESSENGER_INPUT_FIELD = './/*[@aria-label="Message"]'
    MESSENGER_PROVIDED_TEXT_XPATH = ".//*[text()='This is your problem now']"
    CHOOSE_A_GIF_BUTTON_XPATH = './/*[@aria-label="Choose a GIF"]'
    GIF_SEARCH_XPATH = './/*[@placeholder="Search"]'
