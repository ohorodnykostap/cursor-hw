import dataclasses

from collections import namedtuple

# 1

class Laptop:
    def __init__(self):
        battery = Battery("battery for Lenovo-V15-IIL")
        self.battery = battery


class Battery:
    def __init__(self, volts):
        self.volts = volts


laptop = Laptop()
print(laptop.battery.volts)


# battery for Lenovo-V15-IIL

# 2
class Guitar:
    def __init__(self, guitarstring):
        self.guitarstring = guitarstring


class GuitarString:
    def __init__(self):
        pass


guitarstring = GuitarString()
guitar = Guitar(guitarstring)


# 3

class Calc:
    @staticmethod
    def add_nums(num, num1, num2):
        return num + num1 + num2


sum_all_num = Calc.add_nums(1, 2, 3)
print(sum_all_num)


# 4

class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pasta({self.ingredients})'

    @classmethod
    def carbonara(cls):
        return cls(['bacon', 'parmesan', 'eggs'])

    @classmethod
    def bolognaise(cls):
        return cls(['forcemeat', 'tomato'])


pasta_1 = Pasta.carbonara()
pasta_2 = Pasta.bolognaise()
print('bolognaise', pasta_1)
print('carbonara', pasta_2)

#5

class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value <= self.max_visitors_num:
            self._visitors_count = value
        else:
            self._visitors_count = self.max_visitors_num


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)
            # 50

# 6


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

# 7


AddressBookDataClass_1 = namedtuple('AddressBookDataClass',
                                    ['key', 'name',
                                     'phone_number',
                                     'address', 'email',
                                     'birthday', 'age'])

my_data = AddressBookDataClass_1(1, 'Ostap', '82-55-878',
                                'Lviv', 'ostap.ohorodnyk@gmail.com',
                                '26.06', 32)
print(my_data)

#8

class AddressBook:
    def __init__(self, key, name,
                 phone_number, address,
                 email, birthday, age):
        self.key = int(key)
        self.name = str(name)
        self.phone_number = str(phone_number)
        self.address = str(address)
        self.email = str(email)
        self.birthday = str(birthday)
        self.age = int(age)

    def __str__(self):
        return f'addbook {self.key}, {self.name},' \
               f'{self.phone_number}, {self.address},' \
               f'{self.email}, {self.birthday},' \
               f'{self.age}'


adresa = AddressBook(key=2, name='Bart',
                     phone_number='123-45-67',
                     address='Boston',
                     email='Bart@gmail.com',
                     birthday='01.01.2001',
                     age=21)
print(adresa)
print(adresa.name)

# 9

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def person_age(self):
        return self.age

    @person_age.setter
    def person_age(self, value):
        self.age = value


john = Person('John', 36, 'USA')
john.person_age = 32
print(john.person_age)

# 10

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(12, 'Ostap')
setattr(student, 'email', 'Ostap@gmail.com')
print(getattr(student, 'email'))