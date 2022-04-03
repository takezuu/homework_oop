class Figure:
    __COUNT = 0

    def __init__(self):
        self.area = 0

    def add_area(self, figure):
        if figure.name in ['Square', 'Triangle', 'Rectangle', 'Circle']:
            return self.area + figure.area
        else:
            raise ValueError("ValueError Transferred an incorrect class")

    def __del__(self):
        self.__decrease_count()

    @classmethod
    def __decrease_count(cls):
        if cls.__COUNT > 0:
            cls.__COUNT -= 1
