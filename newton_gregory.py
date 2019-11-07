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
    sumatoria = tabla[0][1]
    for i in range(2, cantidad_puntos+1):
        a_n = tabla[0][i]
        p = proterm(i-1, x, puntos)
        sumatoria += ( a_n * p )

    return sumatoria


def newton_gregory_regresivo(*puntos: Tuple[int, int]):
    cantidad_puntos = len(puntos)

    # Creo la tabla llena de 0s
    tabla = [[0 for i in range(cantidad_puntos)] for j in range(cantidad_puntos)]
    # Cargo los f(x) de la tabla
    for indice in range(cantidad_puntos):
        tabla[indice][0] = puntos[indice][1]
    # Genero la tabla de diferencias divididas
    tabla = tabla_diferencias_divididas_regresiva(puntos, tabla, cantidad_puntos);

    print_tabla_diferencias_divididas(puntos, tabla)

    # Armo el polinomio
    sumatoria = tabla[-1][1]
    for i in range(2, cantidad_puntos+1):
        sumatoria += (proterm_regresivo(i, x, puntos) * tabla[-1][i])

    return sumatoria


# Function to find the product term
def proterm(i, x, puntos):
    pro = 1
    for j in range(i):
        pro = pro * (x - puntos[j][0])
    return pro


def proterm_regresivo(i, x, puntos):
    cantidad_puntos = len(puntos)
    pro = 1
    for j in range(1, i):
        pro = pro * (x - puntos[cantidad_puntos-j][0])
    return pro


# Function for calculating
# divided difference table
def tabla_diferencias_divididas(puntos, tabla, cantidad_puntos):
    for i in range(1, cantidad_puntos):
        for j in range(cantidad_puntos - i):
            tabla[j][i] = ((tabla[j][i - 1] - tabla[j + 1][i - 1]) /
                           (puntos[j][0] - puntos[i + j][0]))
    return tabla


def tabla_diferencias_divididas_regresiva(puntos, tabla, cantidad_puntos):
    for i in range(1, cantidad_puntos):
        j = cantidad_puntos - 1
        while j >= i:
            tabla[j][i] = ((tabla[j][i - 1] - tabla[j - 1][i - 1]) /
                           (puntos[j][0] - puntos[j - i][0]))
            j = j-1
    return tabla


def print_tabla_diferencias_divididas(puntos, tabla):
    cantidad_puntos = len(tabla)
    for i, element in enumerate(tabla): # Con esto agrego la columna de x
        element.insert(0, puntos[i][0])
    encabezado = ["x", "f(x)"]
    for i in range(1, cantidad_puntos):
        encabezado.append("Orden {}".format(i))
    resultado = Texttable()
    resultado.add_row(encabezado)
    resultado.add_rows(tabla, header=False)
    resultado.set_cols_align(list("c" * (cantidad_puntos + 1)))
    print(resultado.draw(), '\n')


a = newton_gregory((1, 1), (3, 3), (4, 13), (5, 37), (7, 151))
print(a)
print(simplify(a))

b = newton_gregory_regresivo((1, 1), (3, 3), (4, 13), (5, 37), (7, 151))
print(b)
print(simplify(b))

if simplify(a) == simplify(b):
    print ("\033[92m"+"Los 2 métodos dan lo mismo"+"\033[0m")