# # # 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__ (self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def my_car(self):
        print(f'my car max spead { self.max_speed } mileage of my car is {self.mileage}')
ford_focus = Vehicle( 240, 208550)
ford_focus.my_car()

            # my car max spead 240 mileage of my car is 208550

# 2. Create a child class Bus that will inherit all the variables and methods of the Vehicle class and will have seating_capacity own method


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage)
        self.capacity = capacity

    def seating_capacity(self):
        print(f'the bus has {self.capacity} seats.')


my_bus = Bus(110, 10000, 50)
my_bus.seating_capacity()


        # the bus has 50 seats.

# 3. Determine which class a given Bus object belongs to (Check type of an object)
print(type(my_bus))
        # <class '__main__.Bus'>

# 4. Create an instance of Bus named school_bus and determine if school_bus is also an instance of the Vehicle class
School_bus = Bus(100, 110, 50)
print(isinstance(School_bus, Vehicle))
        # True

# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

# 6*. Create a new class SchoolBus that will inherit all the methods from School and Bus and will have its own - bus_school_color

class SchoolBus(School, Bus):
    def __init__(self, max_speed, mileage, capacity, school_bus_color, number_of_students, get_school_id):
        Bus.__init__(self, max_speed, mileage, capacity)
        School.__init__(self, get_school_id, number_of_students)
        self.school_bus_color = school_bus_color
    def bus_color(self):
        print(f'Bus color is {self.capacity}.')

bus_2 = SchoolBus(130, 222000, 'RED', 50, 28, 123 )
print(bus_2.max_speed, bus_2.mileage,bus_2.number_of_students, bus_2.school_bus_color)
bus_2.bus_color()

# 7.
class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return (self.sound)


class Wolf(Bear):
    def __init__(self, sound):
        super().__init__(sound)


bears = Bear('rrrrrr')
wolves = Wolf('aaauuuu')
animals = (bears, wolves)

for sound in animals:
    print(sound.make_sound())
                # rrrrrr
                # aaauuuu
# # 8
# class City():
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
#
#     def check_population(self):
#         if self.population > 1500:
#             return self.population
#         else:
#             return (f'Your city {self.name} is too small')
#
#
# Lviv = City( 'Lviv', 1000000)
# Pidbirchi = City('Pidbirchi', 3500)
# all_cities = (Lviv, Pidbirchi)
#
#
# for i in all_cities:
#     print(i.check_population())