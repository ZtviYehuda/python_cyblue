class Rectangle:
    def __init__(self, lan, width):
        self.lan = lan
        self.width = width

    def perimeter(self):
        return 2 * (self.lan + self.width)

    def area(self):
        return self.lan * self.width

    def is_square (self):
        return self.lan == self.width

    def __str__(self):
        return f"rectangle lan = {self.lan}, width = {self.width}"

    def print_rectangle(self):
        for i in range(self.lan):
            print("*" * self.width)

rec = Rectangle(4, 3)
print(rec.print_rectangle())
