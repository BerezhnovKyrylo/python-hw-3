#Створіть функцію def double_zero(array) яка приймає цілочисельний масив і дублює всі нулі,
# повертаючи новий масив в якому нулі продубльювані, при дублювані всі інші елементи повинні бути зсунутті вправо.

#Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми,
# або за допомогою input() або в результаті викликів функції. Але в файлі double_zero.py
# повина бути створена функція def double_zero(array) яка виконує необхідну логіку.

#Приклади:

#double_zero([1,0,2,3,0,4,5,0]) -> [1,0,0,2,3,0,0,4,5,0,0]
#double_zero([1,0,2,3,0,4,5,0]) -> [1,0,0,2,3,0,0,4,5,0,0]
#double_zero([1,2,3]) -> [1,2,3]


def double_zero(array):
    array_edit = array.copy()
    i = 0
    while i < len(array_edit):
        if array_edit[i] == 0:
            array_edit.insert(i+1, 0)
            i += 2
        else: i += 1
    return (array_edit)
str_inp = input("Введить числа ")
try:
    array_input = list(map(int, str_inp))
    array_input_rez = double_zero(array_input)
    if len(array_input) != len(array_input_rez):
        print("0 продублювані", array_input_rez)
    else:
        print("Не містить 0", array_input)
except ValueError:
    print("Введіть тільки числа")