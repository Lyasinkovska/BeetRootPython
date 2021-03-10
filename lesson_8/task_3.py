"""create a phonebook application
Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or 
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program"""


def create_contact(firstname, lastname, number, city):
    return {
        'firstname': firstname,
        'lastname': lastname,
        'fullname': firstname + " " + lastname,
        'number': number,
        'city': city
    }


def append_contact(contact):
    return phonebook.append(contact)


def search_by_key(key, value):
    return [element for element in phonebook if element.get(key) == value]


def search_by_firstname(firstname):
    return search_by_key('firstname', firstname)


def search_by_lastname(lastname):
    return search_by_key(value=lastname, key='lastname')


def search_by_fullname(fullname):
    return search_by_key(value=fullname, key='fullname')


def search_by_number(number):
    return search_by_key(value=number, key='number')


def search_by_city(city):
    return search_by_key(value=city, key='city')


def delete_record(index_of_contact):
    if index_of_contact:
        return phonebook.pop(int(index_of_contact))
    else:
        print("There is no such record.")


def update_record():
    pass


def print_phonebook(phonebook):
    print(phonebook)


def print_contacts(contacts):
    if not contacts:
        print("There is no such contacts in a phonebook.")
    else:
        for contact in contacts:
            print(f'Index of contact {phonebook.index(contact)}: {contact}')


if __name__ == '__main__':
    phonebook = [
        {'firstname': 'Liudmyla', 'lastname': 'Yasinkovska', 'fullname': 'Liudmyla Yasinkovska', 'number': '123',
         'city': 'Lviv'},
        {'firstname': 'Yuriy', 'lastname': 'Mamonov', 'fullname': 'Yuriy Mamonov', 'number': '14586', 'city': 'Lviv'},
        {'firstname': 'Yura', 'lastname': 'Mamonov', 'fullname': 'Yura Mamonov', 'number': '45588', 'city': 'Kyiv'}]

    phonebook_keys = ['firstname', 'lastname', 'number', 'city']

    while True:
        user_choice = input(f'"cc" - create new contact,\n"sn" - search by firstname,\n"sl" - search by lastname,'
                            f'\n"sf" - search by fullname,\n"snm" - search by number,\n"sc" - search by city,'
                            f'\n"d" - delete record,\n"u" - update record,\n"pr" - print phonebook'
                            f'\n"q" - quit application\nYour choice: ')

        search_actions = {'sn': search_by_firstname, 'sl': search_by_lastname, 'sf': search_by_fullname,
                          'snm': search_by_number, 'sc': search_by_city}

        if user_choice == 'cc':
            firstname, lastname, number, city, = [input(f'Enter {elem}: ').capitalize().strip() for elem in phonebook_keys]
            phonebook.append(create_contact(firstname, lastname, number, city))
        elif user_choice in search_actions:
            user_input = input(f"Enter {str(search_actions[user_choice])}: ").capitalize().strip()
            print_contacts(search_actions[user_choice])
        # elif user_choice == 'sn':
        #     user_input = input("Enter firstname: ").capitalize().strip()
        #     print_contacts(search_by_firstname(user_input))
        # elif user_choice == 'sl':
        #     user_input = input("Enter lastname: ").capitalize().strip()
        #     print_contacts(search_by_lastname(user_input))
        # elif user_choice == 'sf':
        #     user_input = input("Enter fullname: ").title().strip()
        #     print_contacts(search_by_fullname(user_input))
        # elif user_choice == 'snm':
        #     user_input = input("Enter number: ").strip()
        #     print_contacts(search_by_number(user_input))
        # elif user_choice == 'sc':
        #     user_input = input("Enter city: ").capitalize().strip()
        #     print_contacts(search_by_city(user_input))
        elif user_choice == 'd':
            user_input = input("What contact do you want to delete? Enter fullname: ").title().strip()
            contacts = search_by_fullname(user_input)
            if contacts is not None:
                print_contacts(search_by_fullname(user_input))
                index_of_contact = input("Please choose the index of contact: ")
                delete_record(index_of_contact)
        elif user_choice == 'u':
            update_record()
        elif user_choice == "q":
             break

    print(phonebook)
