from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, side1, side2):
        super().__init__()
        if side1 or side2 > 0:
            self.name = 'Rectangle'
            self.perimeter = round((side1 + side2) * 2, 2)
            self.area = round(side1 * side2, 2)
        else:
            raise ValueError("ValueError This class can't be created")
