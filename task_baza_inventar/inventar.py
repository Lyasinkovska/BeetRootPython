"""
Будем реализовывать процесс "катания на лыжах" а именно
Есть база сдающая в аренду инвентарь.
инвентарь лыжи шлемы палки и сноуборды санки.
Есть подьемник который пропускает человека только если он экиперован.
Лыжи+палки+каска
борд+каска
санки

каждый "инвентарь" знает кто ему из инвентарей пара.

баз выдающих несколько. Понятно что взять и сдать надо только владельцу лыж(или что там сдавать будет)

инвентарь имеет износ. С момента покупки каждое использование должно уменьшать его стоимость. Да конечно есть базовая
стоимость и остаточная. Например Санки купили за 500 рассчитаны на 200 раз покататься. через 100 проездов будет уже
250 остаточная цена.

Планы на среду. -
Реализуем снаряжение отдыхающего. - Реализуем "допуск" на гору с проверкой обмундирования. -
класс База должен знать кому что выдал и обратно принимать только свое и кто ему должен обязательно знать. - делаем
основной блок генерим и принимаем инвентарь на баланс в базы выдачи. - делаем (думаем как и где) сохранение и
восстановление состояния базы (наша база "Їжачок" приняла 20ть лыж при первом запуске так сгенерили. При втором
запуске уже ничего не генерим должно откуда то восстановить состояние склада. -  придумать куда впендюрить дескриптор
- вспомнить про статик и классметоды может тоже где пригодятся. Магические методы туда же.

Первый запуск - приняли в базы инвентарь. Следующие запуски инвентарь уже есть и выдается рандомно наверное пусть
набирает человек и пробует а мы смотрим кого пропустит наш "швейцар" на подьемник а кого нет.

Пишу сейчас чтоб могли себе продумать в голове что это и как должно быть. Может какой то элемент еще упустил
подумайте. Представьте реальную базу и какие варианты могут быть там.

База должна давать отчет
- что есть на сейчаc
- что на рукахє
"""
from datetime import datetime
from random import randint


class Inventar:
    IZNOS = 1
    LIFE = 1000
    accident_inv = 1

    def __init__(self, cost):
        self.name = self.__class__.__name__
        self.cost = cost
        self._hp = self.LIFE
        self.__owner = None

    @classmethod
    def restore(cls, baza_result):
        ex = cls(baza_result['cost'])
        ex.hp = baza_result['hp']
        return ex

    def use(self):
        self._hp -= self.IZNOS
        if self.accident():
            self._hp -= 10 * self.IZNOS

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, new_hp):
        if new_hp < self._hp:
            self._hp = new_hp

    @property
    def ok(self):
        return self._hp > self.IZNOS

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        from baza import Baza
        if self.owner is None:
            self.__owner = new_owner

    def accident(self):
        return True if randint(0, 100) < self.accident_inv else False

    @property
    def data(self):
        return {
            'name': self.name,
            'cost': self.cost,
            'hp': self._hp
        }

    def __repr__(self):
        return f'{self.name}, {self.hp}'


class Lizh(Inventar):
    LIFE = 700


class Sticks(Inventar):
    LIFE = 1000


class Sanki(Inventar):
    LIFE = 500
    accident_inv = 5


class Bord(Inventar):
    LIFE = 900


class Helmet(Inventar):
    LIFE = 990


class Restorer:

    @classmethod
    def restore(cls, baza_result):
        classes = globals()
        ex = classes.get(baza_result['name']).restore(baza_result)
        return ex


if __name__ == '__main__':
    # a1 = Lizh()
    a2 = Lizh(499)
    print(a2.__class__.__name__)
    print(Restorer.restore(({"name": "Lizh", "cost": 500, "hp": 600})))
