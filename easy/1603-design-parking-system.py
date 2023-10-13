class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

        
    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        if carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        if carType == 3 and self.small > 0:
            self.small -= 1
            return True

obj = ParkingSystem(1, 1, 1)
param_1 = print(obj.addCar(1))
param_2 = print(obj.addCar(2))
param_3 = print(obj.addCar(3))
param_4 = print(obj.addCar(1))