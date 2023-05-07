from selenium.webdriver.common.by import By
import random

class FormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"label[for='gender-radio-{random.randint(1, 3)}']")
    PHOHE_NUMBER = (By.CSS_SELECTOR, "input[id='userNumber']")
    BIRTH_DAY = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    MONTHS_CHANGE = (By.CSS_SELECTOR, f"select[class='react-datepicker__month-select']")
    MONTHS = (
    By.CSS_SELECTOR, f"select[class='react-datepicker__month-select'] option[value='{random.randint(1, 12)}']")
    YEARS_CHANGE = (By.CSS_SELECTOR, f"select[class='react-datepicker__year-select']")
    YEARS = (
    By.CSS_SELECTOR, f"select[class='react-datepicker__year-select'] option[value='{random.randint(1900, 2100)}']")
    SUBJECT = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    SELECT_STATE = (By.CSS_SELECTOR, "div[id ='state']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY = (By.CSS_SELECTOR, "div[id ='city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    ALL_TABLE = (By.XPATH, "//div[@class='table-responsive']")


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_BUTTON = (By.CSS_SELECTOR, "label[class^='custom'][for='yesRadio']")
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, "label[class^='custom'][for='impressiveRadio']")
    NO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')


class ButtonsPageLocators:
    DOUBLE_CLICK = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")

    SUCCESS_DOUBLE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    SUCCESS_RIGHT = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, "a[id='bad-request']")
    NOT_FOUND_LINK = (By.CSS_SELECTOR, "a[id='invalid-url']")
    FORBIDDEN_LINK = (By.CSS_SELECTOR, "a[id='forbidden']")
    ALL_LINKS = [(By.CSS_SELECTOR, "a[id='created']"),
                 (By.CSS_SELECTOR, "a[id='no-content']"),
                 (By.CSS_SELECTOR, "a[id='moved']"),
                 (By.CSS_SELECTOR, "a[id='bad-request']"),
                 (By.CSS_SELECTOR, "a[id='unauthorized']"),
                 (By.CSS_SELECTOR, "a[id='forbidden']"),
                 (By.CSS_SELECTOR, "a[id='invalid-url']"),
                 ]
    TEXT_AFTER_CLICK = (By.CSS_SELECTOR, "p[id='linkResponse']")
    BROKEN_IMAGE = (By.XPATH, "//img[contains(@src, 'Toolsqa_1.jpg')]")


class UploadPageLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOADED_FILE = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")


class DownLoadPageLocators:
    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id='downloadButton']")


class DynamicPropertiesPageLocators:
    ENABLE_AFTER_FIVE_SECOND = (By.CSS_SELECTOR, "button[id='enableAfter']")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, " button[id='colorChange']")
    VISIBLE_AFTER_FIVE_SECOND = (By.CSS_SELECTOR, " button[id='visibleAfter']")
