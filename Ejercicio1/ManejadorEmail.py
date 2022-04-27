import csv
from Email import Email


class controlEmail:
    __lista = []

    def __init__(self):
        self.__lista = []

    def punto1(self):
        print('El email debe ser del tipo: idCuenta@dominio.tipoDominio.\nEjemplo: alumnopoo@gmail.com\n')
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
        return unEmail

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
                print('Contraseña cambiada con éxito.')

    def punto3(self, email, contra):
        str1 = email.split('@', 1)
        str2 = str1[1].split('.', 1)
        otroEmail = Email(str1[0], str2[0], str2[1], contra)
        self.__lista.append(otroEmail)

    def punto4(self, idCorreo):
        cont = 0
        for i in self.__lista:
            if idCorreo == i.getID():
                cont += 1
        if cont > 1:
            print('El ID del correo ingresado está repetido {} veces.'.format(cont))
        elif cont == 1:
            print('El ID del correo ingresado no está repetido.')
        elif cont < 1:
            print('El ID del correo ingresado no se encuentra en la lista.')

    def leerArchivo(self):
        primeraFila = True
        archivo = open('archivoEmails.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if primeraFila:
                primeraFila = False
            else:
                emailArchivo = Email(fila[0], fila[1], fila[2], fila[3])
                self.__lista.append(emailArchivo)
        band = False
        return band

    def getMail(self, email):
        for i in self.__lista:
            if i.retornaEmail() == email:
                return i

    def mostrarlista(self):
        if len(self.__lista) < 1:
            print('No hay ningún correo cargado en la lista.\n')
            input()
        else:
            for i in self.__lista:                              # Recorre la lista y muestra mail y contraseña
                print(i.retornaEmail())
                print('Contraseña: {}\n'.format(i.getContrasena()))
