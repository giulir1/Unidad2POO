from ManejadorViajero import manejador

if __name__ == '__main__':
    archivoLeido = False
    control = manejador()
    print('Presione enter para realizar el testeo, se agregarán a la lista únicamente los objetos pertenecientes a la clase ViajeroFrecuente.')
    input()
    control.test()
    opcion = input('1 -- Leer archivo\n2 -- Datos viajero\n3 -- Mostrar lista (prueba)\n0 -- SALIR\nIngrese opción: ')
    while (opcion != '0') and (opcion != '1') and (opcion != '2') and (opcion != '3'):
        print('ERROR. Ingrese una opción válida')
        opcion = input('1 -- Leer archivo\n2 -- Datos viajero\n3 -- Mostrar lista (prueba)\n0 -- SALIR\nIngrese opción: ')
    while opcion != '0':
        if opcion == '1':
            if not archivoLeido:
                control.leerArchivo()
                archivoLeido = True
            else:
                print('El archivo ya fue leído anteriormente.\n')
            opcion = input('1 -- Leer archivo\n2 -- Datos viajero\n3 -- Mostrar lista (prueba)\n0 -- SALIR\nIngrese opción: ')

        elif (opcion == '2') and archivoLeido:
            try:
                numero = int(input('\nIngrese número de viajero: '))
                unViajero = control.getViajero(numero)
                if type(unViajero) == control.getType():
                    control.datosViajero(unViajero)
                else:
                    input('No se encontró el viajero correspondiente. Presione enter para volver al menú.\n')
                opcion = input('1 -- Leer archivo\n2 -- Datos viajero\n3 -- Mostrar lista (prueba)\n0 -- SALIR\nIngrese opción: ')
            except:
                input('ERROR. Debe ingresar un número válido. Presione enter para volver al menú.\n')
                opcion = input('1 -- Leer archivo\n2 -- Datos viajero\n3 -- Mostrar lista (prueba)\n0 -- SALIR\nIngrese opción: ')

        elif (opcion == '3') and archivoLeido:
            print('LISTA DE VIAJEROS:')
            control.mostrar()
            opcion = input('\n1 -- Leer archivo\n2 -- Datos viajero\n3 -- Mostrar lista (prueba)\n0 -- SALIR\nIngrese opción: ')

        elif (opcion == '2') or (opcion == '3') and not archivoLeido:
            print('ERROR. El archivo debe ser leído antes de realizar alguna acción. Seleccione primero la opción N° 1.')
            opcion = input('1 -- Leer archivo\n2 -- Datos viajero\n3 -- Mostrar lista (prueba)\n0 -- SALIR\nIngrese opción: ')

        while (opcion != '0') and (opcion != '1') and (opcion != '2') and (opcion != '3'):
            print('ERROR. Ingrese una opción válida')
            opcion = input('1 -- Leer archivo\n2 -- Datos viajero\n3 -- Mostrar lista (prueba)\n0 -- SALIR\nIngrese opción: ')
    print('\nFINALIZANDO PROGRAMA...')
