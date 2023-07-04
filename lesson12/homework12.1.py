import re

def validate_phone_number(phone_number):
    pattern = r"\+\d{1,3}-\d{2}-\d{5,7}"
    return re.fullmatch(pattern, phone_number) is not None

# Тесты для проверки валидации номеров
def test_valid_phone_numbers():
    valid_numbers = [
        "+375-29-7776655",
        "+37-29-7776655",
        "+3-29-7776655",
        "+375-44-777665",
        "+375-44-77766",
    ]
    for number in valid_numbers:
        assert validate_phone_number(number)

def test_invalid_phone_numbers():
    invalid_numbers = [
        "",
        "test12345test",
        "375-29-7776655",
        "+-29-7776655",
        "+3a5-29-7776655",
        "+3756-29-7776655",
        "+375--7776655",
        "+375-4-7776655",
        "+375-444-7776655",
        "+375-c4-7776655",
        "+375-33-",
        "+375-33-7",
        "+375-33-7776",
        "+375-33-77766554",
        "+375-29-7776e55",
    ]
    for number in invalid_numbers:
        assert not validate_phone_number(number)

test_valid_phone_numbers()
test_invalid_phone_numbers()