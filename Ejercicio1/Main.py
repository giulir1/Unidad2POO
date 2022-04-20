from Email import Email
import ManejadorEmail

if __name__ == '__main__':
    print('Ingrese su nombre:')
    nombre = input()
    print('Ingrese el ID de la cuenta:')
    idCuent = input()
    print('Ingrese el dominio de la cuenta:')
    dom = input()
    print('Ingrese el tipo de dominio de la cuenta:')
    tipoDom = input()
    print('Ingrese la contraseña de la cuenta:')
    contra = input()

#   INCISO 1
    unEmail = Email(idCuent, dom, tipoDom, contra)
    print('Estimado {}, te enviaremos tus mensajes a la dirección {}'.format(nombre, unEmail.retornaEmail()))

#   INCISO 2
    print('\n\n¿Desea cambiar la contraseña?\n0--SI\n1--NO')
    op = input()
    if op == '0':
        print('Se cambiará la contraseña.')
    else:
        print('No se cambiará la contraseña.')
