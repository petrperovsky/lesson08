''' Над задачами 5 и 6 буду думать дальше, не могу понять как извлечь данные
для создания словаря {'type': количество}'''

class Storage():
    '''Склад оргтехники'''
    pass


class OfficeMachines():
    '''Общий класс для оргтехники'''
    added_price = 1.5

    def __init__(self, type: str, model: str, start_price: float):
        self.type = type
        self.model = model
        self.start_price = start_price

    @property
    def finish_price(self):
        return self.start_price * self.added_price

    def __str__(self):
        return f'{self.type} {self.model}'


class Printer(OfficeMachines):

    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeMachines):

    def __init__(self, *args):
        super().__init__('Сканнер', *args)


machine1 = Printer('Xerox', 3300)
print(machine1, machine1.finish_price)
