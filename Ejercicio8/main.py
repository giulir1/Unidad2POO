from ManejadorConjuntos import manejador

if __name__ == '__main__':
    control = manejador()
    control.muestraListas()
    print('------------------------------')
    opcion = input('1 - Sumar las listas\n2 - Restar las listas\n3 - Verificar si las listas son iguales\n0 - SALIR\nOpción: ')
    while opcion != '0':
        if opcion == '1':
            control.punto1()
            print('------------------------------')
        elif opcion == '2':
            control.punto2()
            print('------------------------------')
        elif opcion == '3':
            control.punto3()
            print('------------------------------')
        else:
            print('ERROR - Ingrese una opción válida.')
        opcion = input('1 - Sumar las listas\n2 - Restar las listas\n3 - Verificar si las listas son iguales\n0 - SALIR\nOpción: ')
