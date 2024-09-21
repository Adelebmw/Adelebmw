def divide_numbers(a, b):
    try: 
        result = a / b
        return result
    except ZeroDivisionError:
        error_message = f'Ошибка деление на ноль: a={a}, b={b}, операция = деление'
        return error_message

numerator = 100
denominator = 0
print(divide_numbers(numerator, denominator)) 

    #2
# def input_integer():
#     try:
#         user_input = input('Введите целое число:')
    