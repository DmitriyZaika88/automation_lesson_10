import os

from selene import be, have
from selene.support.shared import browser


class RegistrationPage:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def type_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def type_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def type_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def choose_gender(self, value):
        browser.element('[for="gender-radio-1"]').should(have.text(value)).click()
        return self

    def type_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def type_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def type_subjects(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
        return self

    def choose_hobbies(self, value):
        browser.element('[for="hobbies-checkbox-2"]').should(have.text(value)).click()
        return self

    def picture_path(self, file_name):
        return str(
            browser.element('#uploadPicture').send_keys(os.getcwd() + file_name)
        )

    def type_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def choose_state_and_city(self, state, city):
        browser.element('#react-select-3-input').should(be.blank).type(state).press_enter()
        browser.element('#react-select-4-input').should(be.blank).type(city).press_enter()
        return self

    def should_registered_user_with(self, full_name, email, gender, number,
                                    date_of_birth, subjects, hobbies, photo, address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(full_name, email, gender, number,
                             date_of_birth, subjects, hobbies, photo, address, state_and_city))
        return self
