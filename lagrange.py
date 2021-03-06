from typing import Tuple
from sympy import simplify
from sympy.abc import x


def lagrange(*puntos: Tuple[int, int]):
    cantidad_puntos = len(puntos)
    sumatoria = 0
    pasos = "Primero me fijo cuantos puntos tengo, en este caso son {}:\n\t{}\n".format(cantidad_puntos, puntos)
    pasos += "\nPor cada punto vamos a calcular primero el Li(x) y multiplicarlo por f(xi).\n" \
             "Luego, la suma de estos resultados será el polinomio interpolante de Lagrange.\n\n"
    for i in range(cantidad_puntos):
        pasos += "Punto {} de {}:\n".format(i+1, cantidad_puntos)
        y = puntos[i][1]
        l_de_i = L(i, *puntos)
        pasos += "\tL{}(x) = {}\n\tf(x{}) = {}\n".format(i, l_de_i, i, y)
        sumatoria += l_de_i * y
    resultado = simplify(sumatoria)
    pasos += "\nSumando los {} términos anteriores obtenemos:\n\tP(x) = {}\n\n".format(cantidad_puntos, sumatoria)
    pasos += "Y operando finalmente obtenemos:\n\tP(x) = {}\n".format(resultado)
    indice = str(resultado).find("**")
    if (indice == -1):
        indice = str(resultado).find("*")
        if (indice==-1):
            pasos += " Grado del polinomio: 0 \n"
        else:
            pasos += " Grado del polinomio: 1 \n"
    else:
        pasos += " Grado del polinomio: {} \n".format(str(resultado)[indice+2])
    if (cantidad_puntos == 1):
        diferencia = 0
    else:
        diferencia = puntos[0][0] - puntos[1][0]
    equiespaciados = True
    for i in range((cantidad_puntos) - 1):
        if (puntos[i][0] - puntos[i + 1][0] != diferencia):
            equiespaciados = False
        diferencia = puntos[i][0] - puntos[i + 1][0]
    if (equiespaciados):
        pasos+= "Los puntos son equiespaciados"
    else:
        pasos+= "Los puntos no son equiespaciados"
    return resultado, pasos


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