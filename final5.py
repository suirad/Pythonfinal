"Implementation and testing of Rectangle class"

class Rectangle:
    "Rectangle class"
    def __init__(self, size):
        self._length = 0.0
        self._width = 0.0
        if isinstance(size, tuple):
            self.setwidth(size[0])
            self.setlength(size[1])
    def __repr__(self):
        return "Width: {}, Length: {}".format(self.width(), self.length())
    def area(self):
        "Calulate area"
        return self.width() * self.length()
    def perimeter(self):
        "Calulate perimeter"
        return 2 * (self.width() + self.length())
    def setwidth(self, width):
        "Sets width"
        if isinstance(width, float):
            self._width = width
    def setlength(self, length):
        "Sets length"
        if isinstance(length, float):
            self._length = length

    def issquare(self):
        "Checks if rectangle is a square"
        if self.width() == self.length():
            return True
        return False
    def length(self):
        "Gets Length"
        return self._length
    def width(self):
        "Gets Width"
        return self._width


def main():
    "Main program"
    width = float(input("Give Width: "))
    length = float(input("Give Length: "))
    rect = Rectangle((width, length))
    print("Rectangle: {}\nArea: {}\nPerimeter: {}\nIs square?: {}".format(
        rect,
        rect.area(),
        rect.perimeter(),
        rect.issquare()

    ))


if __name__ == "__main__":
    main()
