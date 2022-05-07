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
        maximo = ViajeroFrecuente(0000, '', '', '', 0)
        for cont, i in enumerate(self.__lista):
            if self.__lista[cont] > maximo:
                maximo = self.__lista[cont]
        print('Viajero/s con mayor cantidad de millas')
        for i in self.__lista:
            if i == maximo:
                print(i)
        print('\n')

    def mostrar(self):
        for i in self.__lista:
            print(i)

    def acumularMillas(self, indice):
        try:
            millas = int(input('Ingrese millas: '))
            self.__lista[indice] + millas
            print('Viajero:\n{}'.format(self.__lista[indice]))
        except ValueError:
            input('ERROR. Debe ingresar un número válido. Presione enter para volver al menú.\n')

    def buscar(self):                       # devuelve el índice del plan buscado por su código
        cod = input('Ingrese un número de viajero: ')
        for cont, i in enumerate(self.__lista):
            if cod == i.retornaNum():
                return cont

    def canjearMillas(self, indice):
        try:
            millas = int(input('Ingrese millas a canjear: '))
            if millas < self.__lista[indice].totalMillas():
                self.__lista[indice] - millas
                print('Viajero:\n{}'.format(self.__lista[indice]))
            else:
                print('ERROR. La cantidad de millas a canjear debe ser menor que la cantidad de millas acumuladas.\nPresione enter para volver al menú.\n')
        except ValueError:
            input('ERROR. Debe ingresar un número válido. Presione enter para volver al menú.\n')
