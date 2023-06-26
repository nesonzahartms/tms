@dataclass

class MyDataClass:
    a: str
    b: int
    c: list

    @classmethod
    def build(cls, *args):
        """
        Your implementation here
        """


# Тесты для задания 1: должны отработать без ошибок!
person1 = MyDataClass.build("TEST", 34, [1, 2, 3])  # valid parameters
print(person1)
try:
    person2 = MyDataClass.build(100, 33, [1, 2, 3])  # invalid parameters
except Exception as exc:
    print(exc)

try:
    person3 = MyDataClass.build("TEST", "33", [1, 2, 3])  # invalid parameters
except Exception as exc:
    print(exc)

try:
    person3 = MyDataClass.build("TEST", 33, (1, 2, 3))  # invalid parameters
except Exception as exc:
    print(exc)