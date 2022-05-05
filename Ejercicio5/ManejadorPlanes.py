import csv
from PlanAhorro import PlanAhorro


class manejador:
    __lista = []

    def __init__(self):                 # constructor de la lista
        self.__lista = []

    def agregarPlan(self, plan):        # agrega únicamente instancias de la clase PlanAhorro a la lista
        if type(plan) == PlanAhorro:
            self.__lista.append(plan)

    def leerarchivo(self):              # lee el archivo
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            unPlan = PlanAhorro(fila[0], fila[1], fila[2], fila[3])
            self.agregarPlan(unPlan)
        archivo.close()

    def buscar(self):                       # devuelve el índice del plan buscado por su código
        cod = input('Ingrese un código de plan: ')
        for cont, i in enumerate(self.__lista):
            if cod == i.getCodigo():
                return cont

    def listarPlanes(self, valorCuota):     # muestra los planes con valor de cuota menor a un valor dado
        for i in self.__lista:
            if valorCuota > i.calculoCuota(i.getCantidadCuotas()):
                print('Código: {:<4} Modelo: {:<8} Versión: {}'.format(i.getCodigo(), i.getModelo(), i.getVersion()))

    def comprobarValor(self, indice, valor):
        band = False
        if self.__lista[indice].getValor() == valor:
            band = True
        return band                     # si encontró el plan devuelve True, si no lo encontró devuelve False

    def cambiarValor(self, indice):     # actualiza el valor del plan
        valor = float(input('Ingrese el nuevo valor: '))
        self.__lista[indice].cambioValor(valor)
        input('Valor del plan actualizado. Presione enter para volver al menú.\n')

    def mostrar(self):                  # comprobación de la lista
        print('CODIGO   MODELO   VERSION         PRECIO       CUOTAS   CUOTAS P/ LICITAR')
        for i in self.__lista:
            print(i)

    def montoLicitacion(self, indice):
        return self.__lista[indice].getCuotasLicitacion() * self.__lista[indice].calculoCuota(self.__lista[indice].getCantidadCuotas())

    def obtenerCuotasLicitacion(self, indice):
        return self.__lista[indice].getCuotasLicitacion()
