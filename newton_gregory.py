from typing import Tuple
from sympy import simplify
from sympy.abc import x
from texttable import Texttable


def newton_gregory(*puntos: Tuple[int, int]):
    cantidad_puntos = len(puntos)

    pasos = "Primero me fijo cuandos puntos tengo, en este caso son {}:\n\t{}\n".format(cantidad_puntos, puntos)
    pasos += "\nPara realizar el método de Newton Gregory vamos a trabajar con la tabla de diferencias divididas progresivas.\n" \
             "Con los puntos que tenemos la tabla nos queda así:.\n\n"

    # Creo la tabla llena de 0s
    tabla = [[0 for i in range(cantidad_puntos)] for j in range(cantidad_puntos)]
    # Cargo los f(x) de la tabla
    for indice in range(cantidad_puntos):
        tabla[indice][0] = puntos[indice][1]
    # Genero la tabla de diferencias divididas
    tabla = tabla_diferencias_divididas(puntos, tabla, cantidad_puntos)

    pasos += tabla_diferencias_divididas_to_string(puntos, tabla)
    pasos += "\n\nAhora, planteamos el polinomio:\n" \
             "\tP(x)=a0+a1(x-x0)+a2(x-x0)(x-x1)+....+an(x-x0)(x-x1)....(x-xn-1)\n"
    pasos += "Donde cada \"an\" es un elemento de la primera fila en nuestra tabla de diferencias divididas progresivas.\n\n"


    # Armo el polinomio
    sumatoria = tabla[0][1]
    pasos += "Termino 1 de {}:\n".format(cantidad_puntos)
    pasos += "\ta0 = {}\n".format(sumatoria)

    for i in range(2, cantidad_puntos+1):
        a_n = tabla[0][i]
        p = proterm(i-1, x, puntos)
        pasos += "Termino {} de {}:\n".format(i, cantidad_puntos)
        pasos += "\ta{} = {}\n\t{} * {}\n".format(i-1, a_n, a_n, p)
        sumatoria += ( a_n * p )
    resultado = simplify(sumatoria)
    pasos +="\nSumando los terminos anteriores nuestro polinomio resulta:\n\tP(x) = {}\n\n".format(sumatoria)
    pasos += "Y operando finalmente obtenemos:\n\tP(x) = {}\n".format(resultado)
    indice = str(resultado).find("**")
    if (indice == -1):
        indice = str(resultado).find("*")
        if (indice == -1):
            pasos += " Grado del polinomio: 0 \n"
        else:
            pasos += " Grado del polinomio: 1 \n"
    else:
        pasos += " Grado del polinomio: {} \n".format(str(resultado)[indice + 2])
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


def newton_gregory_regresivo(*puntos: Tuple[int, int]):
    cantidad_puntos = len(puntos)
    pasos = "Primero me fijo cuandos puntos tengo, en este caso son {}:\n\t{}\n".format(cantidad_puntos, puntos)
    pasos += "\nPara realizar el método de Newton Gregory vamos a trabajar con la tabla de diferencias divididas regresivas.\n" \
             "Con los puntos que tenemos la tabla nos queda así:.\n\n"
    # Creo la tabla llena de 0s
    tabla = [[0 for i in range(cantidad_puntos)] for j in range(cantidad_puntos)]
    # Cargo los f(x) de la tabla
    for indice in range(cantidad_puntos):
        tabla[indice][0] = puntos[indice][1]
    # Genero la tabla de diferencias divididas
    tabla = tabla_diferencias_divididas_regresiva(puntos, tabla, cantidad_puntos)
    pasos += tabla_diferencias_divididas_to_string(puntos, tabla)
    pasos += "\n\nAhora, planteamos el polinomio:\n" \
             "\tP(x)=b0+b1(x-xn)+b2(x-xn)(x-xn-1)+....+bn(x-xn)(x-xn-1)....(x-x1)\n"
    pasos += "Donde cada \"bn\" es un elemento de la última fila en nuestra tabla de diferencias divididas regresivas.\n\n"

    # Armo el polinomio
    sumatoria = tabla[-1][1]
    pasos += "Termino 1 de {}:\n".format(cantidad_puntos)
    pasos += "\tb0 = {}\n".format(sumatoria)
    for i in range(2, cantidad_puntos+1):
        b_n = tabla[-1][i]
        p = proterm_regresivo(i, x, puntos)
        sumatoria += (b_n * p)
        pasos += "Termino {} de {}:\n".format(i, cantidad_puntos)
        pasos += "\tb{} = {}\n\t{} * {}\n".format(i-1, b_n, b_n, p)
    resultado = simplify(sumatoria)
    pasos += "\nSumando los terminos anteriores nuestro polinomio resulta:\n\tP(x) = {}\n\n".format(sumatoria)
    pasos += "Y operando finalmente obtenemos:\n\tP(x) = {}\n".format(resultado)
    indice = str(resultado).find("**")
    if (indice == -1):
        indice = str(resultado).find("*")
        if (indice == -1):
            pasos += " Grado del polinomio: 0 \n"
        else:
            pasos += " Grado del polinomio: 1 \n"
    else:
        pasos += " Grado del polinomio: {} \n".format(str(resultado)[indice + 2])
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


def tabla_diferencias_divididas_to_string(puntos, tabla):
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
    return resultado.draw()


# a, mensaje = newton_gregory((1, 1), (3, 3), (4, 13), (5, 37), (7, 151))
# print(a)
# print(mensaje)
# print(simplify(a))
#
# b = newton_gregory_regresivo((1, 1), (3, 3), (4, 13), (5, 37), (7, 151))
# print(b)
# print(simplify(b))
#
# if simplify(a) == simplify(b):
#     print ("\033[92m"+"Los 2 métodos dan lo mismo"+"\033[0m")
