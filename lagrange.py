from typing import Tuple
from sympy import simplify, cos, sin
from sympy.abc import x, y


def lagrange(*puntos: Tuple[int, int]):
    cantidad_puntos = len(puntos)
    sumatoria = 0
    for i in range(cantidad_puntos):
        y = puntos[i][1]
        sumatoria += L(i, *puntos) * y
    return sumatoria


def L(i, *puntos: Tuple[int, int]):
    cantidad_puntos = len(puntos)
    multiplicatoria = 1
    for j in range(cantidad_puntos):
        if j != i:
            x_i = puntos[i][0]
            x_j = puntos[j][0]
            multiplicatoria *= (x - x_j) / (x_i - x_j)
    return multiplicatoria



    # Ejemplo de como se usa la funcion
print(L(0, (1,2), (3,4)))
print(L(0, (1,2), (6,7)))
print(L(0, (1,2), (3,4), (6,7)))

print("---------")
a = lagrange((1,1), (2,8), (4,64))
print(a)
print(simplify(a))
#print(a)

#print(eval(str(lagrange((1,2), (3,4), (6,7)))))


# ecuacion = '1 '
# for xd in range(10):
#     ecuacion += "* (x+"+str(xd)+") "
# print(ecuacion)
# print(eval(ecuacion))
# x=2
# a = (x + x**2)
# a = a*x
# print(a)
# print(eval('5*(x+5)'))
# print("hola "+"hoas")