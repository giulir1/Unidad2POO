from ManejadorViajeros import manejador


if __name__ == '__main__':
    control = manejador()
    control.leerArchivo()
    opcion = input('1 - Mostrar viajero/s con una cierta cantidad de millas\n2 - Acumular millas\n3 - Canjear millas\n0 - SALIR\nOpción: ')
    while opcion != '0':
        if opcion == '1':
            control.comparar()
        elif opcion == '2':
            idViajero = control.buscar()
            if type(idViajero) == int:
                control.acumularMillas(idViajero)
            else:
                input('No se encontró el viajero. Presione enter para volver al menú.\n')
        elif opcion == '3':
            idViajero = control.buscar()
            if type(idViajero) == int:
                control.canjearMillas(idViajero)
            else:
                input('No se encontró el viajero. Presione enter para volver al menú.\n')
        else:
            print('ERROR. Ingrese una opción válida.')
        opcion = input('1 - Mostrar viajero/s con mayor cantidad de millas\n2 - Acumular millas\n3 - Canjear millas\n0 - SALIR\nOpción: ')
