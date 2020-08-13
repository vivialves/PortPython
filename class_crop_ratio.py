class CropRatio:

    def __init__(self):
        self.__crops = {}
        self.__total_weight = 0

    def add(self, name, crop_weight):
        # Função que adiciona produto na colheita.
        if name in self.__crops:
            self.__crops[name] += crop_weight
        else:
            self.__crops[name] = crop_weight

        self.__total_weight += crop_weight
        # return f'{self.__total_weight} total_weight'

    def proportion(self, name):
        if name not in self.__crops.keys():
            return None
        return f'{self.__crops[name]/self.__total_weight} proportion'


if __name__== "__main__":
    crop_ratio = CropRatio()
    crop_ratio.add('Wheat', 2)
    crop_ratio.add('Wheat', 5)
    crop_ratio.add('Rice', 1)
    crop_ratio.add('Watermelon', 2)
    crop_ratio.add('Watermelon', 2)

    print(crop_ratio.proportion('Wheat'))
    print(crop_ratio.proportion('Rice'))
    print(crop_ratio.proportion('Apple'))
    print(crop_ratio.proportion('Watermelon'))