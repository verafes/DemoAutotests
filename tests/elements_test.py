import time
import allure
import pytest

from pages.elements_page import *


@allure.suite("Main test")
class TestElements:
    @allure.feature("Test Text Box")
    class TestTextBox:
        @allure.title("Test text box")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_field()
            out_name, out_email, out_current_address, out_permanent_address = text_box_page.check_filled_field()
            time.sleep(5)
            assert full_name == out_name
            assert email == out_email
            assert current_address == out_current_address
            assert permanent_address == out_permanent_address

    @allure.feature("Test Check Box")
    class TestCheckBox:
        @allure.title("Test check box")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random()
            input_checkbox = check_box_page.get_checked_box()
            output_checkbox = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox == output_checkbox

    @allure.feature("Test Radio Button")
    class TestRadioButton:
        @allure.feature("Test Radio Button")
        class TestRadioButton:
            radio_buttons_list = ['yes', 'impressive', 'no']
            random.shuffle(radio_buttons_list)

            @pytest.mark.parametrize('item', radio_buttons_list)
            @allure.title("Check radio button")
            def test_radio_button(self, driver, item):
                radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
                radio_button_page.open()
                with allure.step("check click on the buttons"):
                    radio_button_page.click_on_the_radio_button(item)
                    output_field = radio_button_page.get_output_result()
                    assert output_field == item.title(), f"{item.title()} radiobutton is not clickable"

        @allure.title("Check radio button - var")
        def test_radio_button1(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            with allure.step("check click on the buttons"):
                # radio_buttons_list = ['yes', 'impressive', 'no']
                # random.shuffle(radio_buttons_list)
                # for i in radio_buttons_list:
                #     radio_button = radio_button_page.click_on_the_radio_button(i)
                #     output = radio_button_page.get_output_result()
                #     print(output)
                radio_button_page.click_on_the_radio_button('yes')
                output_yes = radio_button_page.get_output_result()
                radio_button_page.click_on_the_radio_button('impressive')
                output_impressive = radio_button_page.get_output_result()
                radio_button_page.click_on_the_radio_button('no')
                output_no = radio_button_page.get_output_result()
            assert output_yes == "Yes", "Yes radiobutton is not clickable"
            assert output_impressive == "Impressive", "Impressive radiobutton is not clickable"
            assert output_no == "No", "No radiobutton is not clickable"


    @allure.feature("Check webtable")
    class TestWebTable:
        @allure.title("add new person in table")
        def test_add_person_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            # count = random.randint(1, 100)
            new_person = web_table_page.add_new_person()
            result = web_table_page.check_new_added_person()
            assert new_person in result

        @allure.title("check people in the table")
        def test_check_people_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_people(key_word)
            table_result = web_table_page.check_people()
            time.sleep(15)
            assert key_word in table_result

    @allure.feature("Buttons Page")
    class TestButtonsPage:
        button = ["double", "right", "click"]

        @pytest.mark.parametrize('item', button)
        @allure.title("check clicking on buttons of dif types")
        def test_different_click_on_the_button(self, driver, item):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button = button_page.click_on_different_button(item)
            assert button in ["You have done a dou", "You have done a right click", "You have done a click click"], \
                f"The {item} button was not pressed"

        @allure.title("check clicking on buttons of dif types - version 2")
        def test_different_click_on_the_button_three(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button("double")
            right = button_page.click_on_different_button("right")
            click = button_page.click_on_different_button("click")
            assert double == "You have clicked a double click", "The double click button was not pressed"
            assert right == "You have clicked a right click", "The right click button was not pressed"
            assert click == "You have clicked a click click", "The dynamic click button was not pressed"

    @allure.feature("Links Page")
    class TestLinksPage:

        @allure.title("Check simple link")
        def test_check_simple_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.click_on_simple_link()
            assert href_link == current_url, "The link is broken or url is incorrect"

        @allure.title("Check simple link")
        def test_check_simple_link_v2(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.click_on_simple_link_v2()
            assert href_link == current_url, "The link is broken or url is incorrect"

        @allure.title("Check the broken link")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_the_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "The link works or the status code is not 400"


    @allure.feature("Upload and Download page")
    class TestDownloadAndUploadPage:

        def test_download_file(self, driver):
            download_page = DownloadPage(driver, "https://demoqa.com/upload-download")
            download_page.open()
            check = download_page.download_file()
            assert check is True

        def test_upload_file(self, driver):
            upload_file = UploadPage(driver, "https://demoqa.com/upload-download")
            upload_file.open()
            file_name, result = upload_file.upload_file()
            assert file_name == result, "There is not been upload"

    @allure.feature("check dynamic buttons")
    class TestDynamicButtons:
        @allure.title("check enable button")
        def test_enable_button(self, driver):
            enable_button = DynamicPage(driver, "https://demoqa.com/dynamic-properties")
            enable_button.open()
            clickable_button = enable_button.check_enable_button()
            assert clickable_button is True, "The button is not enable"

        @allure.title("check changed color")
        def test_check_changed_color(self, driver):
            color_button = DynamicPage(driver, "https://demoqa.com/dynamic-properties")
            color_button.open()
            color_before, color_after = color_button.check_changed_of_color()
            assert color_after != color_before, "The color is not changed"

        @allure.title("check appear button")
        def test_appear_button(self, driver):
            appear_button = DynamicPage(driver, "https://demoqa.com/dynamic-properties")
            appear_button.open()
            button = appear_button.check_appear_button()
            assert button is True, "The button don't appear"