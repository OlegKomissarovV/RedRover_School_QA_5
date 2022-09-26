class Figure:
    def __init__(self, name) -> None:
        self.name = name


class Rectangle(Figure):
    def __init__(self, name,  side_a, side_b) -> None:
        super().__init__(name)
        self.__side_a = side_a
        self.__side_b = side_b

    def get_side(self):
        return f'Side A is {self.__side_a} side B is {self.__side_b}'

    def set_side(self, new_a, new_b):
        print(f'New side A is {new_a} new side B is {new_b}')
        self.__side_a = new_a
        self.__side_b = new_b

    def get_area(self):
        return f'Area of rect is {self.__side_a * self.__side_b}'

    def info(self):
        return 'i am Rectangle'


class Square(Figure):
    def __init__(self, name,  side) -> None:
        super().__init__(name)
        self.__side = side

    def get_side(self):
        return f'Side A is {self.__side}'

    def set_side(self, new_side):
        print(f'New side A is {new_side}')
        self.__side = new_side

    def info(self):
        return 'i am Square'

    def get_area(self):
        print('Test1')
        return f'Area of square is {self.__side ** 2}'


if __name__ == '__main__':
    f = Square('my square', 5)
    p = Rectangle('my rectangle', 1, 2)
    f.set_side(10)
    print('Test')
    p.set_side(10, 2)
    figures = [f, p]
    for figure in figures:
        print(figure.info())
        print(figure.get_side())
        print(figure.get_area())
