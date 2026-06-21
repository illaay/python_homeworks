# 1. Одно слово
# Напишите программу, которая обрабатывает список из строк и удаляет все строки,
# содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
# Данные:
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# Пример вывода:
# Обработанный список: ['hello', 'world', 'simple']

# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
#
# del_strs_count = 0
# for index in range(len(text_list)):
#     current_index = index - del_strs_count
#     if len(text_list[current_index].split()) > 1:
#         del text_list[current_index]
#         del_strs_count += 1
#         continue
#     text_list[current_index] = text_list[current_index].lower()
#
# print(text_list)



# Обновление цен товаров
# Дан список товаров с ценами. Программа должна применить скидку к каждому товару и
# добавить в список элемент с новой ценой. В конце вывести таблицу с новой ценой.
# Данные:
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
# Пример вывода:
# Введите скидку (в процентах): 17
# Товар          Старая цена    Новая цена
# Laptop            1200.00$       996.00$
# Mouse                25.00$         20.75$
# Keyboard           75.00$         62.25$
# Monitor            200.00$       166.00$

# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
# discount = int(input("Введите скидку (в процентах): "))
#
# print(f"{"Товар":<10}{"Старая цена":>21}{"Новая цена":>21}")
# for name, price in products:
#     new_price = price - price / 100 * discount
#     print(f"{name:<10}{float(new_price):>20.2f}${discount:>20.2f}$")
