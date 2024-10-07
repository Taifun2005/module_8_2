# try:
#     i = 0
#     print(10 / i)
#     print('Сделано')
# except (ZeroDivisionError, NameError) as exe:
#     print(f'Нельзя делить на НОЛЬ ')
# else:
#     print(Если ошибок не было{exe.args})
# finally:
#     print('Выполнять всегда')

def personal_sum(numbers):
    result, incorrect_data = 0, 0
    for num in numbers:
        try:
            result += num
        except TypeError as exc:
            print(f'Некорректный тип данных для подсчёта суммы - {num}')
            incorrect_data += 1
    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        s = personal_sum(numbers)
        average = s[0] / (len(numbers) - s[1])
        return average
    except ZeroDivisionError as exc:
        return 0
    except TypeError  as exc:
        print('В numbers записан некорректный тип данных')
        return None




    # average = sum(numbers) / len(numbers)

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать