import json

from inventar import Inventar, Lizh, Sanki, Bord, Helmet, Restorer, Sticks


class Baza:
    def __init__(self, name):
        self.name = name
        self._inventar = []
        self._oblik_inventar = []

    @property
    def inventar(self):
        return self._inventar

    def add_inventar(self, type_inv: Inventar):
        if isinstance(type_inv, Inventar) and type_inv.owner is None:
            type_inv.owner = self
            self._inventar.append(type_inv)
        else:
            raise ValueError

    def save(self):
        with open(f'{self.name}_inventar.json', 'w') as file:
            json.dump([exemp.data for exemp in self._inventar], file)

    def restore(self):
        with open(f'{self.name}_inventar.json', 'r') as file:
            result = json.load(file)
            for item in result:
                exemplyar = Restorer.restore(item)
                self.add_inventar(exemplyar)

    def give_inventar_by_name(self, inv_name, person: 'Person'):
        for exem in self._inventar:
            if inv_name == exem.name:
                self._oblik_inventar.append((person, exem))
                self._inventar.remove(exem)
                return exem

    def take_back_inventar(self, person: 'Person', inventar):
        self._oblik_inventar.remove((person, inventar))
        self._inventar.append(inventar)

    def check_if_baza_inventar(self, person, inventar):
        if (person, inventar) in self._oblik_inventar:
            return True
        return False

    def __str__(self):
        return f'{self.inventar}'


class Podemnik:
    required_inventar = [('Lizh', 'Helmet', 'Sticks'), ('Bord', 'Helmet'), ('Sanki')]

    @staticmethod
    def check_inventar_of_person(inventar):
        for kit in Podemnik.required_inventar:
            return all([each_inventar.name in kit for each_inventar in inventar])

    @staticmethod
    def ride(person: "Person"):
        if Podemnik.check_inventar_of_person(person.inventar):

            for example in person.inventar:
                example.use()


class Person:

    def __init__(self, name='Vasyl'):
        self.name = name
        self.__inventar = []

    @property
    def inventar(self):
        return self.__inventar

    def take_inventar(self, baza: Baza, inventar: Inventar):
        if inventar in baza.inventar:
            inventar = baza.give_inventar_by_name(inventar.name, self)
            self.__inventar.append(inventar)

    def return_inventar_to_baza(self, baza: Baza):
        for one_inventar in self.inventar:
            if baza.check_if_baza_inventar(self, one_inventar):
                baza.take_back_inventar(self, one_inventar)
                print(one_inventar)
                # print(one_inventar)


if __name__ == '__main__':
    l1 = Lizh(500)
    st1 = Sticks(100)
    h1 = Helmet(300)
    b1 = Baza("Sonechko")
    b1.add_inventar(st1)
    b1.add_inventar(h1)
    b1.add_inventar(l1)

    b1.restore()
    p1 = Person('Ivan Ivanov')

    p1.take_inventar(b1, l1)
    p1.take_inventar(b1, h1)

    Podemnik.ride(p1)
    Podemnik.ride(p1)
    Podemnik.ride(p1)



    #
    # # print(b1._inventar)
    # # print(b1._oblik_inventar)
    # print(p1.inventar)
    # p1.return_inventar_to_baza(b1)
    # print()
    # print(b1.inventar)
    # print(b1._oblik_inventar)
    # print(p1.inventar)
