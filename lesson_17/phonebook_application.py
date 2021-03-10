"""
Functionality of Phonebook application:

Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program
The first argument to the application should be the name of the phonebook. Application should load JSON data, if it is
present in the folder with application, else raise an error.
After the user exits, all data should be saved to loaded JSON.
"""
import json


class Phonebook:
    number = 0

    def __init__(self):
        self.__phonebook = []
        Phonebook.number += 1

    @property
    def phonebook(self):
        return self.__phonebook

    def add_contact_to_phonebook(self, contact):
        if contact not in self.__phonebook:
            self.__phonebook.append(contact)

    def delete_contact(self, contact: 'Contact'):
        self.__phonebook.remove(contact)

    def find_contact(self, attribute, value):
        result = []
        try:
            for contact in self.__phonebook:
                if getattr(contact, attribute) == value:
                    result.append(contact)
            return result
        except AttributeError:
            return []

    def update_contact_by_number(self, value):
        for contact in self.__phonebook:
            if getattr(contact, 'number'):
                setattr(contact, 'number', value)

    def save(self):
        with open(f'phonebook_{self.number}.json', 'w') as file:
            json.dump([contact.data for contact in self.phonebook], file)

    def __repr__(self):
        return f'{self.__phonebook}'


class Contact:

    def __init__(self, firstname: str = '', lastname: str = '', number: str = '', city: str = ''):
        self.__city = city
        self.__number = number
        self.__lastname = lastname
        self.__firstname = firstname

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value: str):
        if isinstance(value, str):
            self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value: str):
        if isinstance(value, str):
            self.__lastname = value

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value: str):
        if isinstance(value, str):
            self.__number = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value: str):
        if isinstance(value, str):
            self.__city = value

    @property
    def data(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'fullname': self.fullname,
            'number': self.number,
            'city': self.city
        }

    def __repr__(self):
        return f'{self.fullname}: {self.__number}'


if __name__ == '__main__':
    ph1 = Phonebook()
    contact1 = Contact('Liudmyla', 'Yasinkovska', '0123456', 'Lviv')
    contact3 = Contact('Liudmyla', 'Yasinkovska', '0177776', 'Lviv')
    contact2 = Contact('Anna', 'Yasinkovska', '012415456', 'Kyiv')
    ph1.add_contact_to_phonebook(contact1)
    ph1.add_contact_to_phonebook(contact2)
    ph1.add_contact_to_phonebook(contact3)
    contact1.firstname = 'Olha'
    contact1.lastname = 'Kryvtsova'
    print(ph1)
    ph1.update_contact_by_number('222222222')
    print(ph1.find_contact('lastname', 'Yasinkovska'))
    print(contact3)
    ph1.save()
