from ManejadorEmail import controlEmail

if __name__ == '__main__':
    band = True
    opcion1 = -1
    control = controlEmail()
    while opcion1 != 0:
        print('Elija una acción:\n1--Crear cuenta\n2--Modificar contraseña\n3--Crear instancia de la clase\n4--Verificar email\n5--Leer lista (PRUEBA)\n0--SALIR')
        opcion1 = int(input())

        if opcion1 == 1:
            unEmail = control.punto1()                              # Crea instancia de la clase Email
            print('¿Desea cambiar la contraseña?\n1--SI\n2--NO')
            opcion2 = int(input())
            if opcion2 == 1:
                control.punto2(unEmail)                             # Cambia contraseña de la instancia creada
                input('Presione cualquier tecla para continuar.\n')
            else:
                print('No se modificará la contraseña\n')
                input('Presione cualquier tecla para continuar.\n')

        if opcion1 == 2:
            print('Ingrese un email para modificar la contraseña:')
            correo = str(input())
            unEmail = control.getMail(correo)                       # Devuelve el objeto de la clase Email correspondiente
            control.punto2(unEmail)

        if opcion1 == 3:
            print('Ingrese una dirección de correo:')
            nuevomail = input()
            print('Ingrese la contraseña de la cuenta:')
            contra = input()
            control.punto3(nuevomail, contra)                      # Crea instancia de la clase Email

        if opcion1 == 4:
            if band:
                band = control.leerArchivo()                                    # Lee el archivo una sola vez para evitar repeticiones en la lista
                print('ARCHIVO LEIDO.\n')
            print('Ingrese un ID de correo para verificar si está repetido:')
            idCorreo = input()
            control.punto4(idCorreo)                                            # Verifica si el ID ingresado está repetido
            print('Presione cualquier tecla para continuar.\n')
            input()

        if opcion1 == 5:
            control.mostrarlista()                                              # Muestra la lista para verificar que se haya cargado correctamente
