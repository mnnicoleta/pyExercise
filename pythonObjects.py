# Build two classes of your choice that can model a real-life example. The class needs to meet the
# following requirements:
# • at least 5 attributes each
# • at least 2 methods each
# • one class to inherit from another
# As a demonstration create at least 5 instances of one class (preferably the child class) and call all
# the methods it holds
# Ex: You can have one class (Country) that has general attributes about countries such as area,
# neighbours, cities etc and methods related to those attributes. The second class can be a specific
# country (Romania) that has more specific attributes such as attractions, universities etc.


class Animal(object):
    def __init__(self, name, has_feet, colour, length, sound):
        self.name = name
        self.has_feet = has_feet
        self.colour = colour
        self.length = length
        self.sound = sound

    def makes_sound(self):
        print("Makes : " + self.sound)

    def to_string(self):
        print("Animal with name = " + self.name + " has " + self.colour + " colour, " + str(self.length))


class Duck(Animal):
    def __init__(self, name, has_feet, colour, length, sound,
                 has_tail, weight, is_bio, price, is_mute):
        self.has_tail = has_tail
        self.weight = weight
        self.isBio = is_bio
        self.price = price
        self.is_mute = is_mute
        super().__init__(name, has_feet, colour, length, sound)

    def makes_sound(self):
        print("Makes = " + self.sound)

    def has_legs(self):
        return self.has_feet


animal1 = Animal("ceceil", True, "yellow", 23, "ga-ga")
animal1.makes_sound()
animal1.to_string()

duck1 = Duck("ceceil", True, "yellow", 23, "ga-ga", True, 2, True, 25, False)
duck1.makes_sound()
duck1.to_string()

duck1 = Duck("ceceil2", True, "yellow", 23, "ga-ga-ga", True, 2, True, 25, False)
duck1.makes_sound()
duck1.to_string()
