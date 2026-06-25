# 1. Простое число
# Напишите функцию, которая проверяет, является ли число n простым
# (делится только на 1 и само себя) и возвращает булевый результат.
# Данные:
# n = 17
# Пример вывода:
# Число 17 является простым

# def is_prime_number(user_number):
#     if user_number <= 1:
#         return False
#     if user_number <= 3:
#         return True
#     if user_number % 2 == 0 or user_number % 3 == 0:
#         return False
#
#     # + 2 (вместо + 1) для корректной работы, если number ** 0.5 равняется 5
#     # (иначе при range(6, 5 + 1, 6) цикл не начнется)
#     for num in range(6 , int(user_number ** 0.5) + 2, 6):
#         if user_number % (num - 1) == 0 or user_number % (num + 1) == 0:
#             return False
#
#     return True
#
#
# n = 17
# print(f"Число {n} {"" if is_prime_number(n) else "не "}является простым")



# 2. Фильтрация чисел по чётности
# Напишите функцию, которая принимает filter_type ("even" или "odd") и
# произвольное количество чисел, возвращая только те, которые соответствуют фильтру.
# Пример вызова:
# print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
# print(filter_numbers("odd", 10, 15, 20, 25))
# print(filter_numbers("prime", 2, 3, 5, 7))
# Пример вывода:
# [2, 4, 6]
# [15, 25]
# Некорректный фильтр

# def filter_numbers(filter_type, *args):
#     if filter_type == 'even':
#         divider = 0
#     elif filter_type == 'odd':
#         divider = 1
#     else:
#         # raise ValueError("Некорректный фильтр")
#         return "Некорректный фильтр"
#
#     suitable_numbers = []
#     for number in args:
#         if number % 2 == divider:
#             suitable_numbers.append(number)
#     return suitable_numbers
#
#
# print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
# print(filter_numbers("odd", 10, 15, 20, 25))
# print(filter_numbers("prime", 2, 3, 5, 7))



# 3. Объединение словарей
# Напишите функцию, которая принимает любое количество словарей и объединяет
# их в один. Если ключи повторяются, используется значение из последнего словаря.
# Данные:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict3 = {"d": 5}
# Пример вызова:
# print(merge_dicts(dict1, dict2, dict3))
# Пример вывода:
# {'a': 1, 'b': 3, 'c': 4, 'd': 5}

# def merge_dicts(*args):
#     # наверное, более затратный по ресурсам, но лаконичный
#     # return {k: v for dictionary in args for k, v in dictionary.items()}
#
#     result = {}
#     for dictionary in args:
#         result.update(dictionary)
#     return result
#
#
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict3 = {"d": 5}
#
# print(merge_dicts(dict1, dict2, dict3))
