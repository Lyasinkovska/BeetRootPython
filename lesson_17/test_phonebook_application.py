"""Write tests for the Phonebook application, which you have implemented in module 1. Design tests for this solution
and write tests using unittest library """
from lesson_9 import task_2 as phone_book
import unittest


class TestPhonebookApplication(unittest.TestCase):
    def setUp(self):
        self.phonebook = [{
            'firstname': 'Liudmyla',
            'lastname': 'Yasinkovska',
            'fullname': 'Liudmyla Yasinkovska',
            'number': '0123456789',
            'city': 'Lviv'
        }, {
            'firstname': 'Anna',
            'lastname': 'Yasinkovska',
            'fullname': 'Anna Yasinkovska',
            'number': '111111111',
            'city': 'Kyiv'
        }]

    def test_create_contact(self):
        contact = phone_book.create_contact('Liudmyla', 'Yasinkovska', 'Liudmyla Yasinkovska', '0123456789', 'Lviv')
        result = self.phonebook[0]
        self.assertEqual(contact, result)

    def test_search_by_key(self):
        phonebook = self.phonebook
        result = self.phonebook[0:2]
        value = 'Yasinkovska'
        key = 'lastname'
        self.assertEqual(phone_book.search_by_key(key, value, phonebook), result)

    def test_return_index(self):
        result = 1
        contact = self.phonebook[0]
        self.assertEqual(phone_book.return_index(contact, self.phonebook), result)


if __name__ == '__main__':
    unittest.main()
