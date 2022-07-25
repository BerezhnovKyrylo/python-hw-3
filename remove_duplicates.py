# Створіть функцію def remove_duplicates(array) яка приймає цілочисельний масив,
# відсортований у порядку зростання, видаліть дублікати чисел, щоб кожен унікальний елемент з’являвся лише один раз.
# Функція має повертати новий масив без дуплікатів чисел, відносний порядок елементів має бути незмінним

# Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми,
# або за допомогою input() або в результаті викликів функції. Але в файлі remove_duplicates.py
# повина бути створена функція def remove_duplicates(array) яка виконує необхідну логіку.

# Приклади:

# remove_duplicates([1,1,2]) -> [1,2]
# remove_duplicates([0,0,1,1,1,2,2,3,3,4]) -> [0,1,2,3,4]
# remove_duplicates([1,1,1,1,1,1,1,1]) -> [1]

def remove_duplicates(array):
    array_edit = array.copy()
    i = 0
    while i < (len(array_edit)-1):
        if array_edit[i] == array_edit[i+1]:
            array_edit.pop(i+1)
        else: i += 1
    return(array_edit)
str_inp = input("Введить числа ")
try:
    array_input = list(map(int, str_inp))
    array_input_rez = remove_duplicates(array_input)
    if len(array_input) != len(array_input_rez):
        print("Без дублікатів", array_input_rez)
    else:
        print("Дублікати не введені", array_input)
except ValueError:
    print("Введіть тільки числа")


