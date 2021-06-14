'''Это читерство, что использовал комплексные числа внутри класса?
Я пока плохо понимаю действия с комплексными числами'''


class ComplexNumber():
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        complex1 = self.__complex + other.__complex
        return ComplexNumber(complex1.real, int(complex1.imag))

    def __mul__(self, other):
        complex1 = self.__complex * other.__complex
        return ComplexNumber(complex1.real, int(complex1.imag))

    def __str__(self):
        return str(self.__complex)


c1 = ComplexNumber(2, -1)
c2 = ComplexNumber(6)

print(c1 + c2, c1 * c2)
print(complex(2, -1) + complex(6), complex(2, -1) * complex(6))
