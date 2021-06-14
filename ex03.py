class NumberError(Exception):
    text = 'Нечисловые данные'

    def __str__(self):
        return self.text


my_list = []

while True:
    my_input = input('Введите число или "stop" для выхода: ')
    if my_input == 'stop':
        break
    try:
        if not my_input.isdigit():
            raise NumberError
        my_list.append(my_input)
    except NumberError as e:
        print(e)

print(my_list)
