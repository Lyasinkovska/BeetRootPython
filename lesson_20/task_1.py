import json
from typing import List


class Phonebook:
    number: int = 0

    def __init__(self):
        self.__contacts: List['Contact'] = []
        Phonebook.number += 1

    @property
    def contacts(self):
        return self.__contacts

    def add_contact_to_phonebook(self, contact: 'Contact') -> None:
        if contact not in self.__contacts:
            self.__contacts.append(contact)

    def delete_contact(self, contact: 'Contact') -> None:
        self.__contacts.remove(contact)

    def find_contact(self, attribute, value: str) -> List:
        result: List = []
        try:
            for contact in self.__contacts:
                if getattr(contact, attribute) == value:
                    result.append(contact)
            return result
        except AttributeError:
            return []

    def update_contact_by_number(self, number: str) -> None:
        for contact in self.__contacts:
            if getattr(contact, 'number'):
                setattr(contact, 'number', number)

    def save(self) -> None:
        with open(f'phonebook_{self.number}.json', 'w') as file:
            json.dump([contact.data for contact in self.contacts], file)

    def __repr__(self) -> str:
        return f'{self.__contacts}'


class Contact:

    def __init__(self, firstname: str = '', lastname: str = '', number: str = '', city: str = '') -> None:
        self.__city = city
        self.__number = number
        self.__lastname = lastname
        self.__firstname = firstname

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, value: str) -> None:
        if isinstance(value, str):
            self.__firstname = value

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, value: str):
        if isinstance(value, str):
            self.__lastname = value

    @property
    def fullname(self) -> str:
        return f'{self.firstname} {self.lastname}'

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, value: str):
        if isinstance(value, str):
            self.__number = value

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, value: str):
        if isinstance(value, str):
            self.__city = value

    @property
    def data(self) -> dict:
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'fullname': self.fullname,
            'number': self.number,
            'city': self.city
        }

    def __repr__(self) -> str:
        return f'{self.fullname}: {self.__number}'


if __name__ == '__main__':
    ph1 = Phonebook()
    print(ph1.contacts)
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
    print(ph1.contacts)
