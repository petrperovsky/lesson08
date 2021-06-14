''' Надеюсь, я правильно понял, что по "этикету" мне не понадобится отдельно
запрашивть @classmethod, т.е. оперирую им внутри класса'''


class Date:
    def __init__(self, date: str):
        day, month, year = self.transform(date)
        self.day = day
        self.month = month
        self.year = year
        if not self.valid(day, month, year):
            raise ValueError(f"{date} - несуществующая дата, dd-mm-yyyy")

    @classmethod
    def transform(cls, date):
        for el in date.split('-'):
            yield int(el)

    @staticmethod
    def valid(*date):
        day, month, year = date
        return all([1 <= day <= 31, 1 <= month <= 12, year >= 0])

    def __str__(self):
        return f'Текущая дата {self.day}/{self.month}/{self.year}'


date1 = Date('12-12-1988')
print(date1)
print(Date.valid(12, 12, 1988))
print(Date.valid(12, 31, 1999))
date2 = Date('12-31-1999')
