from pages.registration_page import RegistrationPage
from data.users import User


user = User('Abra', 'Kadabra',
            'abrakadabra@gmail.com',
            'Male',
            '9211234567',
            'June', '1997', '30',
            'Physics',
            'Reading',
            '/resources/wings.jpg',
            'baker st 221b',
            'Haryana', 'Karnal')


def test_registration_page(set_options_in_browser):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.user_registration(user)
    registration_page.should_registered_user_with('Abra Kadabra',
                                                  'abrakadabra@gmail.com',
                                                  'Male',
                                                  '9211234567',
                                                  '30 June,1997',
                                                  'Physics',
                                                  'Reading',
                                                  'wings.jpg',
                                                  'baker st 221b',
                                                  'Haryana Karnal')
