#Створіть функцію def spiral(matrix) яка приймає цілочисельну матрицю розміром NxM
#та повертає масив в якому числа з матриці записані в порядку спіралі. Матриця виглядає наступним чином:

#[
#  [1,2,3],
#  [4,5,6],
#  [7,8,9]
#]
#Це масив цілочисельних масивів. Наприклад матриця розміром 3x4 виглядає ось так:

#[
#    [1,2,3,4],
#    [5,6,7,8],
#    [9,10,11,12]
#]
#Порядок спіралі виглядає ось так:
#m1

#m2

#Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми,
#або за допомогою input() або в результаті викликів функції. Але в файлі spiral.py
# повина бути створена функція def spiral(matrix) яка виконує необхідну логіку.

#Приклади:

#spiral([[1,2,3],[4,5,6],[7,8,9]]) -> [1,2,3,6,9,8,7,4,5]
#spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) -> [1,2,3,4,8,12,11,10,9,5,6,7]

def spiral(matrix):
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    res = []
    print('Matrix:\n')
    [print(*m, sep='\t') for m in matrix]

    while left < right and top < bottom:

        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    print('\nSpiral matrix: ', res)


if __name__ == '__main__':
    spiral([[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]])
    spiral([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
