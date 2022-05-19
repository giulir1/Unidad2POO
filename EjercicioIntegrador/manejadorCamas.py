import csv
import numpy as np
from cama import cama


class manejadorCamas:
    __arregloCamas = None
    __dimension = 0
    __i = 0

    def __init__(self):
        self.__arregloCamas = np.empty(self.__dimension, dtype=cama)

    def leerArchivoCamas(self):
        band = False
        archivo = open('camas.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if not band:
                band = True
            else:
                self.__dimension += 1
                self.__arregloCamas.resize(self.__dimension)
                unaCama = cama(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                self.__arregloCamas[self.__i] = unaCama
                self.__i += 1
        archivo.close()

    def buscar(self, paciente):
        indice = -1
        i = 0
        band = False
        while (not band) and (i < len(self.__arregloCamas)):
            if self.__arregloCamas[i].getPaciente() == paciente:
                indice = i
                band = True
            i += 1
        return indice

    def darAlta(self, indice):
        error = False
        print('- FECHA DE ALTA -')
        try:
            dia = int(input('Ingrese N° de día: '))
            mes = int(input('Ingrese N° de mes: '))
            anio = int(input('Ingrese N° de año: '))
            if (1 <= dia <= 31) and (1 <= mes <= 12) and (2020 <= anio):
                fecha = '{}/{}/{}'.format(dia, mes, anio)
                self.__arregloCamas[indice].cambiarAlta(fecha)
            else:
                input('ERROR - Debe ingresar números válidos.\nPresione enter para volver al menú.\n')
                error = True
        except ValueError:
            input('ERROR - Debe ingresar números válidos.\nPresione enter para volver al menú.\n')
            error = True
        finally:
            return error

    def obtenerIdCama(self, indice):
        return self.__arregloCamas[indice].getId()

    def mostrarPaciente(self, indice):
        return self.__arregloCamas[indice]

    def buscarPorDiagnostico(self, diagnostico):
        band = False
        for i in self.__arregloCamas:
            if i.getDiagnostico() == diagnostico:
                print(i)
                print('')
                band = True
        if not band:
            print('No hay pacientes con el diagnóstico ingresado.\n')
