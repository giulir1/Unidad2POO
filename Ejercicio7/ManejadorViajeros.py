import csv
from ViajeroFrecuente import ViajeroFrecuente


class manejador:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregarViajero(self, viajero):
        if type(viajero) == ViajeroFrecuente:
            self.__lista.append(viajero)

    def leerArchivo(self):
        primerFila = True
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if primerFila:
                primerFila = False
            else:
                numViajero = fila[0]
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millasAcumuladas = fila[4]
                unViajero = ViajeroFrecuente(numViajero, dni, nombre, apellido, millasAcumuladas)
                self.agregarViajero(unViajero)
        archivo.close()
        print('ARCHIVO LEIDO. Presione una tecla para continuar.')
        input()

    def comparar(self):
        try:
            cont = 0
            millas = int(input('Ingrese la cantidad de millas: '))
            for i in self.__lista:
                if i == millas:
                    print(i)
                    cont += 1
            if cont < 1:
                print('No hay viajeros con la cantidad de millas ingresadas.')
            print('\n')
        except ValueError:
            input('ERROR. Debe ingresar un número válido. Presione enter para volver al menú.\n')

    def buscar(self):                       # devuelve el índice del viajero según su número
        cod = input('Ingrese un número de viajero: ')
        for cont, i in enumerate(self.__lista):
            if cod == i.retornaNum():
                return cont

    def acumularMillas(self, indice):
        try:
            millas = int(input('Ingrese millas: '))
            millas + self.__lista[indice]
            print('Viajero:\n{}'.format(self.__lista[indice]))
        except ValueError:
            input('ERROR. Debe ingresar un número válido. Presione enter para volver al menú.\n')

    def canjearMillas(self, indice):
        try:
            millas = int(input('Ingrese millas a canjear: '))
            if millas < self.__lista[indice].totalMillas():
                millas - self.__lista[indice]
                print('Viajero:\n{}'.format(self.__lista[indice]))
            else:
                input('ERROR. La cantidad de millas a canjear debe ser menor que la cantidad de millas acumuladas.\nPresione enter para volver al menú.\n')
        except ValueError:
            input('ERROR. Debe ingresar un número válido. Presione enter para volver al menú.\n')
