from src.Figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        super().__init__()
        if radius > 0:
            self.name = 'Circle'
            self.perimeter = round(2 * radius * 3.14, 2)
            self.area = round(3.14 * (radius ** 2), 2)
        else:
            raise ValueError("ValueError This class can't be created")
