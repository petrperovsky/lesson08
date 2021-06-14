class MyZeroDivision(Exception):
    text = 'Делить на ноль нельзя'

    def __str__(self):
        return self.text


class Number(float):
    def __truediv__(self, other):
        if other == 0:
            raise MyZeroDivision
        return float(self) / float(other)


while True:
    x, y = map(Number, input('Введите два числа через пробел: ').split())
    try:
        print(x / y)
    except MyZeroDivision as e:
        print(e)
        break
