import math
from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, side1, side2, side3):
        super().__init__()
        if (side1 + side2 >= side3) and (side2 + side3 >= side1) and (side1 + side3 >= side2):
            self.name = 'Triangle'
            self.perimeter = round(side1 + side2 + side3, 2)
            self.half_perimeter = round(self.perimeter / 2, 2)
            self.area = round(
                math.sqrt(self.half_perimeter * (self.half_perimeter - side1) * (self.half_perimeter - side2) * (
                        self.half_perimeter - side3)), 2)
        else:
            raise ValueError("ValueError This class can't be created")
