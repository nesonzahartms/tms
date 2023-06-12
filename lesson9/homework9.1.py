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
    def move(self):
        print(self.brand, self.mark, 'move')
    def birthday(self):
        print(self.age + 1)
    def stop(self):
        print(self.brand, self.mark, 'stop')

