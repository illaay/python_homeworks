# 1. Оценки текстом
# Напишите программу, которая преобразует список оценок по системе от 1 до 5
# в текстовое представление. Нужно сохранить в списках числовой результат и
# текстовое представление. Где, 5 — "отлично", 3-4 — "хорошо", а 2 и ниже — "неудовлетворительно".
# Данные:
# grades = [5, 3, 4, 2, 1, 5, 3]
# Пример вывода:
# [[5, 'отлично'], [3, 'хорошо'], [4, 'хорошо'], [2, 'неудовлетворительно'],
#  [1, 'неудовлетворительно'], [5, 'отлично'], [3, 'хорошо']]

# grades = [5, 3, 4, 2, 1, 5, 3]
# grades_words = ["отлично" if grade == 5 else ("хорошо" if grade >= 3 else "неудовлетворительно")
#                 for grade in grades]
#
# # print(list(zip(grades, grades_words)))
# # для вывода как в примере
# print([list(pair) for pair in zip(grades, grades_words)])



# 2. Правильные скобки
# Напишите программу, которая принимает строку, содержащую любые виды
# скобок — круглые (),квадратные [] и фигурные {}.
# Необходимо проверить, правильно ли они расставлены.
# Скобки считаются правильно расставленными, если:
# Каждая открывающая скобка имеет соответствующую закрывающую.
# Скобки закрываются в правильном порядке.
# Пример данных:
# string = "({[}])"
# Пример вывода:
# Скобки: ({[}])
# Валидны: False
# Скобки: ([({}()){}])
# Валидны: True

# string = "([({}()){}])"
# opened_brackets = []
# is_valid = True
# opens = "([{"
# closes = ")]}"
#
# for bracket in string:
#     if bracket in opens:
#         opened_brackets.append(bracket)
#     elif bracket in closes:
#         closes_index = closes.index(bracket)
#         if not opened_brackets or opens[closes_index] != opened_brackets[-1]:
#             is_valid = False
#             break
#         opened_brackets.pop()
#
# if opened_brackets:
#     is_valid = False
#
# print(f"Скобки: {string}")
# print(f"Валидны: {is_valid}")
