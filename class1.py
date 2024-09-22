class Animal:
    def __init__(self, name, legs, tail):
        self.name = name
        self.legs = legs
        self.tail = tail
    def __str__(self):
        return f"name = {self.name} legs = {self.legs} tail = {self.tail}


class Dog(Animal):