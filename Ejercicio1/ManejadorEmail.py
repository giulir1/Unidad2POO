from Email import Email


class controlEmail:
    __lista = []

    def __init__(self):
        self.__lista = []

    def punto1(self):
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
        unEmail = Email(idCuent, dom, tipoDom, contra)
        print('Estimado {}, te enviaremos tus mensajes a la dirección {}'.format(nombre, unEmail.retornaEmail()))
        self.__lista.append(unEmail)

    def punto2(self, mail):
        pass

"""
    def leerlista(self):
        for i in self.__lista:
            print(i.retornaEmail())
"""
