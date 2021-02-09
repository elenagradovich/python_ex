'''
Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
на квадраты с наибольшей возможной на каждом этапе стороной.
Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.
'''


def get_squares(width_, height_):
    global square_number
    if width_ > 0.1 and height_ > 0.1:
        if width_ < height_:
            width_, height_ = height_, width_
        print(f'Квадрат со стороной: {round(height_, 2)}')
        square_number += 1
        get_squares(width_ - height_, height_)


width = float(input("width: \n"))
height = float(input("height: \n"))
square_number = 0

if width == 0 or height == 0 or width < 0 or height < 0:
    print('Такого квадрата не существует')
else:
    get_squares(width, height)
    print('----------------------')
    print(f'Количество квадратов {square_number}')
