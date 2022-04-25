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
        unEmail = Email(idCuent, dom, tipoDom, contra)  # Crea la instancia de la clase Email
# Arma el email con los atributos ingresados
        print('Estimado {}, te enviaremos tus mensajes a la dirección {}'.format(nombre, unEmail.retornaEmail()))
        self.__lista.append(unEmail)                    # Agrega el objeto a la lista

    def punto2(self, mail):
        for i in self.__lista:
            if mail == i:
                print('Ingrese la contraseña actual: ')
                contraActual = input()
                while contraActual != i.getContrasena():
                    print('Contraseña incorrecta. Intente otra vez.')
                    contraActual = input()
                print('Ingrese la nueva contraseña: ')
                contraNueva = input()
                i.cambiarContrasena(contraNueva)           # Cambia la contraseña del email

    def getMail(self, email):
        for i in self.__lista:
            while i.retornaEmail() != email:
                print('ERROR. Email incorrecto. Intente nuevamente:')
                email = input()
            return i                                        # Devuelve el objeto de la clase

    def leerlista(self):
        for i in self.__lista:                              # Recorre la lista y muestra mail y contraseña
            print(i.retornaEmail())
            print('Contraseña: {}\n'.format(i.getContrasena()))
