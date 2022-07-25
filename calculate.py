#Покращити програму calculate (файл calculate_raw.py)
#яка була створена на лекції функцією виконання арифметичної операції в одній строчці.
#А також розширена новими арифметичними операціями.
#Можна використовувати вихідний код вашої програми виконання
#відповідного ДЗ, але попередньо повинні бути виправлені помилки.
#Програма має задовольняти наступні потреби:

#Створити файл calculate.py
#Программа повина зчитувати аргументи командної строки (за допомогою модуля sys) і виконувати арифметичні операції.
#Необхідна підтримка 5 базових арифметичних операцій: +, -, *, /
#Додано нову операцію - %.
#Результат виконання арифметичної операції потрібно виводити у консоль.
#Программа повинна адекватно оброблювати помилки.
#Программа повинна запускатись наступним чином: python calculate.py 2 + 2 або python calculate.py 2+2
#Приклади:
#python calculate.py 2 + 2 -> 4
#python calculate.py 2 * 8 -> 16
#python calculate.py 2 - 200 -> -198
#python calculate.py 200 / 2 -> 100
#python calculate.py 3+3 -> 6
#python calculate.py 100-20 -> 80
#python calculate.py 4*4 -> 16
#python calculate.py 25/2 -> 12.5
#Заборонено використовувати eval для обчислення результату.
#Повинна бути створена і використана функція обчислення def calc
# (left_operand, right_operand, operation) яка повертає результат арифметичного обчислення.


import sys
def calc(left_operand, operation, right_operand):
    l_int, op, r_int = left_operand, operation, right_operand
    match op:
        case '*':
            rez = l_int * r_int
        case '+':
            rez = l_int + r_int
        case '-':
            rez = l_int - r_int
        case '/':
            rez = l_int / r_int
        case '%':
            rez = l_int % r_int
    print(l_int, op, r_int, "=", rez)
list_sys=sys.argv[1:]
str_list_sys = "".join(list_sys)
for i in range(len(str_list_sys)):
    op=str_list_sys[i]
    if op in '+-/*%':
        operator = op
try:
    spl_str_list_sys = str_list_sys.split(operator)
    if len(spl_str_list_sys) > 2:
        print("Тільки 1 оператор")
    left_op = int(spl_str_list_sys[0])
    right_op = int(spl_str_list_sys[1])
    calc(left_op, operator, right_op)
except ValueError:
    print("Оператори повинні бути цілими")
except ZeroDivisionError:
    print("Ділення на 0 не можливо")
except NameError:
    print("Не знайдений арефметичний оператор")