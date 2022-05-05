from ManejadorPlanes import manejador


if __name__ == '__main__':
    control = manejador()
    control.leerarchivo()
    print('ARCHIVO LEIDO\n\n')
    opcion = input('1 - Cambiar valor de plan\n2 - Comparar valor de cuota\n3 - Mostrar precio de licitación\n4 - Modificar cuotas para licitación\n5 - Mostrar lista (prueba)\n0 - SALIR\nOpción: ')
    while opcion != '0':
        if opcion == '1':
            control.listarPlanes(9999999)    # lista los planes, 9999999 es para que muestre todos los planes
            indicePlan = control.buscar()    # solicita codigo para buscar el plan correspondiente
            if type(indicePlan) == int:      # el método buscar devuelve un int si encuentra el plan, devuelve None si no lo encuentra
                try:
                    valor = float(input('Ingrese el valor actual del plan: '))
                    while not control.comprobarValor(indicePlan, valor):    # el metodo devuelve False si el valor ingresado no es correcto
                        print('Valor incorrecto. Intente nuevamente.')      # a menos que se ingrese el valor correcto, el programa se mantiene en el loop y no continúa
                        valor = float(input('Ingrese el valor actual del plan: '))
                        control.comprobarValor(indicePlan, valor)
                    control.cambiarValor(indicePlan)                        # si el valor es correcto se ejecuta el método
                except ValueError:           # evita que el programa crashee al ingresar una cadena en lugar de un número
                    input('ERROR. Debe ingresar un número válido. Presione enter para volver al menú.\n')
            else:
                input('No se encontró el plan correspondiente al código ingresado. Presione enter para volver al menú.\n')
        elif opcion == '2':
            try:
                valor = float(input('Ingrese un valor de cuota: $'))
                print('Se muestran los planes con un valor de cuota inferior a ${:.2f}'.format(valor))
                control.listarPlanes(valor)
                print('\n')
            except ValueError:
                input('ERROR. Debe ingresar un número válido. Presione enter para volver al menú.\n')
        elif opcion == '3':
            indice = control.buscar()
            if type(indice) == int:
                print('Para licitar el vehículo se debe pagar una cantidad de ${:.2f}'.format(control.montoLicitacion(indice)))
            else:
                input('No se encontró el plan correspondiente al código ingresado. Presione enter para volver al menú.\n')

        elif opcion == '4':
            print('Modificar cantidad de cuotas para licitar un plan. NOTA: se modifica para todos los planes.')
            indice2 = control.buscar()
            if type(indice2) == int:
                control.cambiarCuotasLicitacion(indice2)
                input('Cantidad de cuotas necesarias para licitar actualizadas.\nPresione enter para volver al menú.\n')
            else:
                input('No se encontró el plan correspondiente al código ingresado. Presione enter para volver al menú.\n')
        elif opcion == '5':
            control.mostrar()
        else:
            print('ERROR. Ingrese una opción válida.\n')

        opcion = input('1 - Cambiar valor de plan\n2 - Comparar valor de cuota\n3 - Mostrar precio de licitación\n4 - Modificar cuotas para licitación\n5 - Mostrar lista (prueba)\n0 - SALIR\nOpción: ')
