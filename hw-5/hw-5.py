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
print(pasta_1)
print(pasta_2)
