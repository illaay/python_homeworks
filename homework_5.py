# Сортировка чисел
# Напишите программу, которая запрашивает у пользователя три числа
# и выводит их в порядке возрастания, разделенные запятой.
# Пример вывода:
# Введите первое число: 5
# Введите второе число: 2
# Введите третье число: 7
# Числа в порядке возрастания: 2, 5, 7

# first_num = int(input("Введите первое число: "))
# second_num = int(input("Введите второе число: "))
# third_num = int(input("Введите третье число: "))
#
# if first_num > second_num and first_num > third_num:
#     biggest = first_num
#     if second_num > third_num:
#         average = second_num
#         smallest = third_num
#     else:
#         average = third_num
#         smallest = second_num
# elif second_num > first_num and second_num > third_num:
#     biggest = second_num
#     if first_num > third_num:
#         average = first_num
#         smallest = third_num
#     else:
#         average = third_num
#         smallest = first_num
#
# else:
#     biggest = third_num
#     if first_num > second_num:
#         average = first_num
#         smallest = second_num
#     else:
#         average = second_num
#         smallest = first_num
#
# print(f"Числа в порядке возрастания: {biggest, average, smallest}")



# Високосный год
# Напишите программу, которая запрашивает у пользователя год и проверяет,
# является ли он високосным. Год является високосным, если он
# делится на 4 без остатка, и в то же время не делится на 100 без остатка.
# При этом если год делятся на 400 без остатка, он тоже является високосным.
# Выведите соответствующее сообщение на экран с помощью функции print.
# Пример вывода:
# Введите год: 2024
# Год является високосным.
# Введите год: 2000
# Год является високосным.
# Введите год: 1900
# Год не является високосным.

# user_year = input("Введите год: ")
#
# if user_year % 4 == 0 and user_year % 100 != 0 or user_year % 100 == 0:
#     print("Год является високосным")
# else:
#     print("Год не является високосным")