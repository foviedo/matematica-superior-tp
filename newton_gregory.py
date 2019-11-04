from typing import Tuple
from sympy import simplify
from sympy.abc import x, y
from texttable import Texttable


def newton_gregory(*puntos: Tuple[int, int]):
    cantidad_puntos = len(puntos)

    # Creo la tabla llena de 0s
    tabla = [[0 for i in range(cantidad_puntos)] for j in range(cantidad_puntos)]
    # Cargo los f(x) de la tabla
    for indice in range(cantidad_puntos):
        tabla[indice][0] = puntos[indice][1]
    # Genero la tabla de diferencias divididas
    tabla = tabla_diferencias_divididas(puntos, tabla, cantidad_puntos);

    print_tabla_diferencias_divididas(puntos, tabla)

    # Armo el polinomio
    sumatoria = tabla[0][0]
    for i in range(1, cantidad_puntos):
        sumatoria += (proterm(i, x, puntos) * tabla[0][i])

    return sumatoria


# Function to find the product term
def proterm(i, x, puntos):
    pro = 1
    for j in range(i):
        pro = pro * (x - puntos[j][0])
    return pro


# Function for calculating
# divided difference table
def tabla_diferencias_divididas(puntos, tabla, cantidad_puntos):
    for i in range(1, cantidad_puntos):
        for j in range(cantidad_puntos - i):
            tabla[j][i] = ((tabla[j][i - 1] - tabla[j + 1][i - 1]) /
                       (puntos[j][0] - puntos[i + j][0]))
    return tabla


def print_tabla_diferencias_divididas(puntos, tabla):
    cantidad_puntos = len(tabla)
    for i, element in enumerate(tabla):
        element.insert(0, puntos[i][0])
    encabezado = ["x", "f(x)"]
    for i in range(1, cantidad_puntos):
        encabezado.append("Orden {}".format(i))
    resultado = Texttable()
    resultado.add_row(encabezado)
    resultado.add_rows(tabla, header =False)
    resultado.set_cols_align(list("c"*(cantidad_puntos+1)))
    print(resultado.draw(), '\n')


a = newton_gregory((1,1), (3,3), (4,13), (5,37), (7,151))
print(a)
print(simplify(a))