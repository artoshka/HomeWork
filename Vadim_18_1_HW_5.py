import re


class ValidCarNumber:


    def __init__(self, number):
        self.number = number


    def is_valid(self, number):
        is_valid = re.search(r"([0-9]{2})(KG)([0-9]{3})([a-zA-Z]{3})", number)
        if not is_valid:
            print("Номер не валидный!")
        elif number[is_valid.start():is_valid.end()] == number:
            print("Номер валидный!")



car_number = ValidCarNumber("")

car_number.is_valid(input("Введите номер: "))