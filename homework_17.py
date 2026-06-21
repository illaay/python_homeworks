# 1. Проверка на подмножество
# Напишите программу, которая проверяет, содержит ли первое множество
# все элементы второго множества. Реализуйте решение несколькими способами.
# Решите одним из способов не используя возможности множеств.
# Данные:
# set1 = {1, 2, 3, 4}
# set2 = {2, 3}
# Пример вывода:
# True

# set1 = {1, 2, 3, 4}
# set2 = {2, 3}
#
# print(set1 > set2)
# print(set1.issuperset(set2))
# print(set2 < set1)
# print(set2.issubset(set1))
# print(set1 == set1 | set2)
# print(set1 == set1.union(set2))
# print(not set2 - set1)
#
# subset = True
# for item in set2:
#     if item not in set1:
#         subset = False
#         break
# print(subset)
#
# for item in set1:
#     set2.discard(item)
# print(not bool(set2))



# 2. Зеркальное подмножество
# Напишите программу, которая проверяет, являются ли элементы одного из
# множеств подмножеством другого. В случае положительного ответа возвращает
# разницу между двумя множествами. Проверить необходимо в обе стороны.
# Данные:
# set1 = {2, 3, 4, 5, 6}
# set2 = {4, 5}
# Пример вывода:
# Подмножество: True
# Разница: {2, 3, 6}

# set1 = {2, 3, 4, 5, 6}
# set2 = {4, 5, 7}
#
# is_diff = set1 == set1 & set2 or set2 == set1 & set2
# if is_diff:
#     diff = set1 ^ set2
#
# print(f"Подмножество: {is_diff}{f"\nРазница: {diff}" if is_diff else ""}")
