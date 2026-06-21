# 1. Число в конце
# Напишите программу, которая создает новый список. В него необходимо добавить
# только те строки из исходного списка, в которых цифры находятся только в конце.
# Данные:
# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# Пример вывода:
# Строки с цифрами только в конце: ['apple23', 'grape3']

# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# new_strings = []
#
# for word in strings:
#     cleaned_word = word.rstrip("1234567890")
#     if cleaned_word.isalpha():
#         new_strings.append(word)
#
# print(new_strings)



# 2. Удаление кратных
# Напишите программу, которая удаляет из списка все значения,
# кратные числу, которое вводится пользователем.
# Данные:
# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# Пример вывода:
# Введите число для удаления кратных ему элементов: 3
# Список без кратных значений: [1, 10, 19, 20]

# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# clean_numbers = []
# user_num = int(input("Введите число для удаления кратных ему элементов: "))
#
# for num in numbers:
#     if num % user_num != 0:
#         clean_numbers.append(num)
#
# print(clean_numbers)



# 3. Порядок четных
# Напишите программу, которая формирует новый список чисел.
# Добавьте в него все элементы исходного списка, где:
# нечетные числа занимают те же позиции,
# чётные числа отсортированы между собой обратном порядке.
# Данные:
# numbers = [5, 2, 3, 8, 4, 1, 2, 7]
# Пример вывода:
# Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]

# numbers = [5, 2, 3, 8, 4, 1, 2, 7]
# new_numbers = []
# sorted_even_nums = []
#
# for num in numbers:
#     if num % 2 == 0:
#         sorted_even_nums.append(num)
# sorted_even_nums.sort(reverse=True)
#
# even_index = 0
# for num in numbers:
#     if num % 2 != 0:
#         new_numbers.append(num)
#     else:
#         new_numbers.append(sorted_even_nums[even_index])
#         even_index += 1
#
# print(new_numbers)
