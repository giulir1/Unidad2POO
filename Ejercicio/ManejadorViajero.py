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

    def getViajero(self, num):
        for i in self.__lista:
            if num == i.retornaNum():
                return i

    def datosViajero(self, viajero):
        opcion = input('Seleccione una opción:\n1 -- Consultar millas\n2 -- Acumular millas\n3 -- Canjear millas\nOpción: ')
        while (opcion != '1') and (opcion != '2') and (opcion != '3'):
            print('ERROR. Seleccione una opción correcta.\n')
            opcion = input('Seleccione una opción:\n1 -- Consultar millas\n2 -- Acumular millas\n3 -- Canjear millas\nOpción: ')
        if opcion == '1':
            print('Cantidad de millas: {}\n'.format(viajero.totalMillas()))
        elif opcion == '2':
            millas = int(input('Ingrese la cantidad de millas a acumular: '))
            print('Cantidad de millas: {}\n'.format(viajero.acumularMillas(millas)))
        elif opcion == '3':
            millas2 = int(input('Ingrese la cantidad de millas a canjear: '))
            print('Cantidad de millas: {}\n'.format(viajero.canjearMillas(millas2)))

    def getType(self):
        return ViajeroFrecuente

    def mostrar(self):
        for i in self.__lista:
            print(i)

    def test(self):
        viajero1 = ViajeroFrecuente(2000, '40123199', 'Nahuel', 'García', 10000)
        self.agregarViajero(viajero1)
        try:
            viajero2 = ViajeroFrecuente(2001, '40383199', 'Marcelo', 'Gómez', 'Seis mil')
            self.agregarViajero(viajero2)
        except:
            pass
        try:
            viajero3 = ViajeroFrecuente(2002, '29123479', 'Paulina', 'Toranzo')
            self.agregarViajero(viajero3)
        except:
            pass
        viajero4 = ViajeroFrecuente(2003, '24058410', 'Mauro', 'López', 8500)
        self.agregarViajero(viajero4)
        viajero5 = 4
        self.agregarViajero(viajero5)
        viajero6 = 'Prueba'
        self.agregarViajero(viajero6)
        viajero7 = ViajeroFrecuente(2004, 42853374, 'Nicolás', 'Ferreira', '4200')
        self.agregarViajero(viajero7)

        print('La lista ha quedado formada por los siguientes objetos:')
        for i in self.__lista:
            print (i)
        input('\nTesteo finalizado. Presione enter para vaciar la lista y comenzar con el programa.')
        self.__lista.clear()
