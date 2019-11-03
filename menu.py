#!/usr/bin/python3
 
def elegirOpcion():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input())
            correcto = True
        except ValueError:
            print('Error, introduce una opcion')
     
    return num

salir = False
opcion = 0

while not salir:

    print ("**********************")
    print ("********FINTER********")
    print ("**********************")
    print ()
    print ("********MENU********");
    print ()
    print ("1. Ingresar Datos")
    print ("2. Mostrar pasos del calculo")
    print ("3. Especializar el polinomio en un valor K")
    print ("4. Alterar valores iniciales")
    print ("5. Finalizar")
     
    print ("Elige una opcion")
 
    opcion = elegirOpcion()
    
    if opcion == 1:
        salirSubmenu = False

        while not salirSubmenu:

            print ("Opcion 1")
            print ("Interpolar por medio de:")
            print ("1. Polinomio de Lagrange")
            print ("2. Newton Gregory Progresivo")
            print ("3. Newton Gregory Regresivo")
            print ("4. Finalizar")
            print ("Elige una opcion")
 
            opcionSubmenu = elegirOpcion()

            if opcionSubmenu == 1:
                print ("Lagrange");
                # metodo para calcular Lagrange
            elif opcionSubmenu == 2:
                print ("NGProgresivo");
                # metodo para calcular NGProgresivo
            elif opcionSubmenu == 3:
                print ("NGRegresivo");
                # metodo para calcular NGRegresivo
            elif opcionSubmenu == 4:
                salirSubmenu = True
            else:
                print ("Introduce un numero entre 1 y 3")


    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
