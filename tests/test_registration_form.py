from selene import command
from selene.support.shared import browser
from pages.registration_page import RegistrationPage

browser.config.click_by_js = True


def test_registration_page(set_options_in_browser):
    registration_page = RegistrationPage()
    # OPEN PAGE
    registration_page.open()

    # WHEN
    registration_page.type_first_name('Abra')
    registration_page.type_last_name('Kadabra')
    registration_page.type_email('abrakadabra@gmail.com')
    registration_page.choose_gender('Male')
    registration_page.type_number('9211234567')
    registration_page.type_date_of_birth('June', '1997', '30')
    registration_page.type_subjects('physics')
    registration_page.choose_hobbies('Reading')
    registration_page.picture_path('/resources/wings.jpg')
    registration_page.type_address('baker st 221b')
    registration_page.choose_state_and_city('Haryana', 'Karnal')
    browser.element('#submit').perform(command.js.click)

    # THEN
    registration_page.should_registered_user_with(
        'Abra Kadabra',
        'abrakadabra@gmail.com',
        'Male',
        '9211234567',
        '30 June,1997',
        'Physics',
        'Reading',
        'wings.jpg',
        'baker st 221b',
        'Haryana Karnal'
    )
    browser.element('#closeLargeModal').click()
