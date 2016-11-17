import sys
from math import hypot, asin, degrees, tan, radians, sin, cos, acos

NEG_ANSWERS = ('n', 'no', 'н', 'нет')

E_INTERVAL = 'Число должно быть в интервале ({0}; {1}).'
E_CONVERT = 'Читайте, пожалуйста, внимательнее.'

I_CONTINUE = 'Повторить ввод ([да]/нет)? '
I_GET_SIDE = 'Введите длину катета: '
I_GET_PRI_U="введите прилежащий угол"
I_GET_PRO_U='введите противолещащий угол'
I_GET_HIP='введите длины гипотенузы'

MAIN_INTERFACE = """
Выберите способ задания треугльника:
0. Выход.
1. По двум катетам.
2. По катету и прилежащему углу.
3. По катету и противолещащему углу.
4. По катету и гипотенузе.
5. По гипотенузе и углу
"""

RESULT = """
Длина катета a1 = {0[0]:.2f}.
Длина катета a2 = {0[1]:.2f}.
Длина гипотенузы b = {0[2]:.2f}.
Угол alfa1 = {0[3]:.2f} градусов.
Угол alfa2 = {0[4]:.2f} градусов.
Площадь треугольника per= {0[5]:.2f}
Периметр треугольника plo = {0[6]:.2f}
"""

class SimpleError(Exception):
    """Здесь может быть ваша документация"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def get_number(prompt, to_type, left_limit, right_limit):
    while True:
        try:
            try:
                res = to_type(input(prompt))
                if left_limit < res < right_limit:
                    return res
                else:
                    raise SimpleError(E_INTERVAL.format(left_limit, right_limit))
            except ValueError:
                raise SimpleError(E_CONVERT)
        except SimpleError as se:
            print(se.value)
        if input(I_CONTINUE).lower() in NEG_ANSWERS:
            break


def get_side(prompt):
    return get_number(prompt, float, 0, float('+inf'))


def get_angle(prompt):
    return get_number(prompt, float, 0, 90)


def t_two_sides():
    a1 = get_side(I_GET_SIDE)
    a2 = get_side(I_GET_SIDE)
    b = hypot(a1, a2)
    alfa1 = degrees(asin(a2/b))
    alfa2 = degrees(asin(a1/b))
    per=a1+a2+b
    plo=a1*a2/2
    return a1, a2, b, alfa1, alfa2,per,plo

def t_side_pri_u():
    a1=get_side(I_GET_SIDE)
    alfa1=get_angle(I_GET_PRI_U)
    b = a1 / cos(radians(alfa1))
    alfa2=90-alfa1
    a2 = sin(radians(alfa1)) * b
    per = a1 + a2 + b
    plo = a1 * a2 / 2
    return a1, a2, b, alfa1, alfa2, per, plo

def t_side_pro_u():
    a1 = get_side(I_GET_SIDE)
    alfa2 = get_angle(I_GET_PRO_U)
    b = a1 / sin(radians(alfa2))
    alfa1 = 90 - alfa2
    a2 = sin(radians(alfa1)) * b
    per = a1 + a2 + b
    plo = a1 * a2 / 2
    return a1, a2, b, alfa1, alfa2, per, plo

def t_side_hip():
    a1 = get_side(I_GET_SIDE)
    b = get_side(I_GET_HIP)
    alfa1 = degrees(acos(a1 / b))
    alfa2 = 90 - alfa1
    a2 = sin(radians(alfa1)) * b
    per = a1 + a2 + b
    plo = a1 * a2 / 2
    return a1, a2, b, alfa1, alfa2, per, plo

def t_pri_u_hip():
    alfa1 = get_angle(I_GET_PRI_U)
    b = get_side(I_GET_HIP)
    alfa2 = 90 - alfa1
    a2 = sin(radians(alfa1)) * b
    a1=cos(radians(alfa1))*b
    per = a1 + a2 + b
    plo = a1 * a2 / 2
    return a1, a2, b, alfa1, alfa2, per, plo

triangle_type = {
    0: sys.exit,
    1: t_two_sides,
    2:t_side_pri_u,
    3:t_side_pro_u,
    4:t_side_hip,
    5:t_pri_u_hip
}

def draw_triangle(triangle_params):
    a1, a2, b, alfa1, alfa2,per,plo = triangle_params
    for x in range(1, round(max(a1, a2)) + 1):
        print('L.' * int(round(x * tan(radians(min(alfa1, alfa2))))))


def main():
    while True:
        user_choice = get_number(MAIN_INTERFACE, int, -1, 6)
        triangle_params = list(triangle_type[user_choice]())
        print(RESULT.format(triangle_params))
        draw_triangle(triangle_params)
        if input(I_CONTINUE).lower() in NEG_ANSWERS:
            break

if __name__ == '__main__':
    main()
