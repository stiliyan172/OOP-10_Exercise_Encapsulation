class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.flour_type

    @flour_type.setter
    def flour_type(self, value):
        if value == "":
            raise ValueError('The flour can not be an empty string')
        self.__flour_type = value

    @property
    def baking_technique(self):
        return self.baking_technique

    @baking_technique.setter
    def baking_technique(self, value):
        if value == "":
            raise ValueError('The baking technique can not be an empty string')
        self.__baking_technique = value

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value):
        if value == "":
            raise ValueError('The weight technique can not be an empty string')
        self.__weight = value
