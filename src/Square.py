from src.Figure import Figure


class Square(Figure):

    def __init__(self, side):
        super().__init__()
        if side > 0:
            self.name = 'Square'
            self.perimeter = round(side * 4, 2)
            self.area = round(side * side, 2)
        else:
            raise ValueError("ValueError This class can't be created")
