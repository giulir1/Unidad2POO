from ManejadorEmail import controlEmail

if __name__ == '__main__':
    opcion1 = 5
    control = controlEmail()
    while opcion1 != 0:
        print('Elija una acción:\n1--Crear cuenta\n2--Modificar contraseña\n3--Crear instancia de la clase\n4--Verificar email\n0--SALIR')
        opcion1 = int(input())

        if opcion1 == 1:
            control.punto1()
            print('¿Desea cambiar la contraseña?\1--SI\n2--NO')
            opcion2 = int(input())
            if opcion2 == 1:
                control.punto2()
                print('\n')
                input('Presione cualquier tecla para continuar.')
            else:
                print('No se modificará la contraseña\n')
                input('Presione cualquier tecla para continuar.')
"""        if opcion1 == 2:


   INCISO 2
    print('\n\n¿Desea cambiar la contraseña?\n0--SI\n1--NO')
    op = input()
    if op == '0':
        print('Se cambiará la contraseña.')
    else:
        print('No se cambiará la contraseña.')
"""
