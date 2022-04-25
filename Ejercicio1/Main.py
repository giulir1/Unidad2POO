from ManejadorEmail import controlEmail

if __name__ == '__main__':
    opcion1 = 5
    control = controlEmail()
    while opcion1 != 0:
        print('Elija una acción:\n1--Crear cuenta\n2--Modificar contraseña\n3--Crear instancia de la clase\n4--Verificar email\n0--SALIR')
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
#            control.leerlista()                                    VERIFICACION DEL CAMBIO DE CONTRASEÑA
