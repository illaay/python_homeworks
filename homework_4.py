# 1. Логические операции
# Напишите программу, которая получит два логических значения от пользователя
# и выведет результат логических операций and, or, not для этих значений,
# а также сравнение на равенство и неравенство. Для операции not используйте первое число.
# Продумайте в каком виде получать ввод от пользователя для логического значения.
# Пример вывода:
# Enter first value: <value1>
# Enter second value: <value1>
# and: True
# or: True
# not: False
# equal: False
# not equal: True

# boolean_value_1 = bool(input("Enter first boolean value (0/1): "))
# boolean_value_2 = bool(input("Enter second boolean value (0/1): "))
#
# print(f"and: {boolean_value_1 and boolean_value_2}")
# print(f"or: {boolean_value_1 or boolean_value_2}")
# # насчет not не понял - нужно перевернуть первое полученное значение через input или
# # первую операцию сравнения, поэтому на всякий случай оба (с использованием закона де Моргана)
# print(f"not (value 1): {not boolean_value_1}")
# print(f"not (and): {not (boolean_value_1 or boolean_value_2)}")
# print(f"equal: {boolean_value_1 == boolean_value_2}")
# print(f"not equal: {boolean_value_1 != boolean_value_2}")



# Проверка условий
# Напишите программу, которая принимает на вход логические значения двух переменных
# (свет включён и окно открыто) и проверяет:
# Оба ли условия выполнены.
# Хотя бы одно из условий выполнено.
# Пример вывода:
# Свет включён? True
# Окно открыто? False
# Оба условия выполнены? False
# Хотя бы одно условие выполнено? True

# is_light_on = bool(input("Свет включен? (0/1): "))
# is_window_open = bool(input("Окно открыто? (0/1): "))
#
# print(f"Оба условия выполнены? {is_light_on and is_window_open}")
# print(f"Хотя бы одно условие выполнено? {is_light_on or is_window_open}")



# * Стоимость мобильного тарифа
# Напишите программу для расчёта стоимости использования мобильного тарифа:
# Базовая стоимость: 30 евро.
# Каждый мегабайт интернета сверх 500 МБ стоит 0.2 евро.
# Программа должна запросить у пользователя количество использованных мегабайтов
# и вывести сколько всего он заплатил (базовый и переплата).
# Пример вывода:
# Введите использованные мегабайты: 510
# Общая стоимость: 32.0

# base_cost = 30
# price_for_one_extra_mb = 0.2
# base_mb = 500
# used_mb = int(input("ведите использованные мегабайты: "))
#
# final_price = base_cost + ((used_mb - base_mb) * price_for_one_extra_mb * (used_mb > base_mb))
# print(f"Общая стоимость: {final_price}")