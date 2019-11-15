from typing import Tuple
from sympy import simplify, cos, sin
from sympy.abc import x, y


def lagrange(*puntos: Tuple[int, int]):
    cantidad_puntos = len(puntos)
    sumatoria = 0
    pasos = "Primero me fijo cuandos puntos tengo, en este caso son {}:\n\t{}\n".format(cantidad_puntos, puntos)
    pasos += "\nPor cada punto vamos a calcular primero el Li(x) y multiplicarlo por f(xi).\n" \
             "Luego, la suma de estos resultados será el polinomio interpolante de Lagrange.\n\n"
    for i in range(cantidad_puntos):
        pasos += "Punto {} de {}:\n".format(i+1, cantidad_puntos)
        y = puntos[i][1]
        l_de_i = L(i, *puntos)
        pasos += "\tL{}(x) = {}\n\tf(x{}) = {}\n".format(i, l_de_i, i, y)
        sumatoria += l_de_i * y

    pasos += "\nSumando los {} terminos anteriores obtenemos:\n\tP(x) = {}\n\n".format(cantidad_puntos, sumatoria)
    pasos += "Y operando finalmente obtenemos:\n\tP(x) = {}\n".format(simplify(sumatoria))

    return simplify(sumatoria), pasos


def L(i, *puntos: Tuple[int, int]):
    cantidad_puntos = len(puntos)
    multiplicatoria = 1
    for j in range(cantidad_puntos):
        if j != i:
            x_i = puntos[i][0]
            x_j = puntos[j][0]
            multiplicatoria *= (x - x_j) / (x_i - x_j)
    return multiplicatoria


# a, mensaje = lagrange((1, 1), (3, 3), (4, 13), (5, 37), (7, 151))
# print(a)
# print(mensaje)
# Ejemplo de como se usa la funcion
# print(L(0, (1,2), (3,4)))
# print(L(0, (1,2), (6,7)))
# print(L(0, (1,2), (3,4), (6,7)))
#
# print("---------")
# a = lagrange((1,1), (2,8), (4,64))
# print(a)
# print(simplify(a))
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