class Figure:
    def __init__(self, name: str) -> None:
        self.name = name


class Rectangle(Figure):
    def __init__(self, name: str, side_a: int, side_b: int) -> None:
        super().__init__(name)
        self.__side_a = side_a
        self.__side_b = side_b

    def get_side(self) -> str:
        """gets side rectangle"""
        return f'Side A is {self.__side_a} side B is {self.__side_b}'

    def set_side(self, new_a: int, new_b: int) -> None:
        """sets side rectangle"""
        print(f'New side A is {new_a} new side B is {new_b}')
        self.__side_a = new_a
        self.__side_b = new_b

    def get_area(self) -> str:
        """gets area rectangle"""
        return f'Area of rect is {self.__side_a * self.__side_b}'

    def info(self) -> str:
        """gets info rectangle"""
        return 'i am Rectangle'


class Square(Figure):
    def __init__(self, name: str,  side: int) -> None:
        super().__init__(name)
        self.__side = side

    def get_side(self) -> str:
        """gets side square"""
        return f'Side A is {self.__side}'

    def set_side(self, new_side: int) -> None:
        """sets side square"""
        print(f'New side A is {new_side}')
        self.__side = new_side

    def info(self) -> str:
        """gets info square"""
        return 'i am Square'

    def get_area(self) -> str:
        """gets area square"""
        return f'Area of square is {self.__side ** 2}'


if __name__ == '__main__':
    square = Square('my square', 5)
    rectangle = Rectangle('my rectangle', 1, 2)
    square.set_side(10)
    rectangle.set_side(10, 2)
    figures = [square, rectangle]
    for figure in figures:
        print(figure.info())
        print(figure.get_side())
        print(figure.get_area())
