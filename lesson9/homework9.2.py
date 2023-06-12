class Auto:
    brand = 'BMW'
    age = 3
    color = 'Blue'
    mark = "M8"
    weight = 2800
    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark
        return

    def move(self):
        print(self.brand, self.mark, 'move')

    def birthday(self):
        print(self.age + 1)

    def stop(self):
        print(self.brand, self.mark, 'stop')

import time
class Truck(Auto):
    max_load = 5000
    def __init__(self, max_load):
        self.max_load = max_load
        return

    def move(self):
        super.move
        print(self.brand, self.mark, 'attention move')

    def load(self):
        time.sleep(1)
        print(self.load, 'load')
        time.sleep(1)
        return

class Car(Auto):
    max_speed = 300
    def __init__(self, max_speed):
        self.max_speed = max_speed
        return

    def move(self):
        super().move
        print(self.brand, self.mark, 'max speed is', self.max_speed)

x = Truck(Auto)
y = Car(Auto)
print(x)
print(y)