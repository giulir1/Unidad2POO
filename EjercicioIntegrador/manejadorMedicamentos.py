import csv
from medicamento import medicamento


class manejadorMed:
    __listaMed = []

    def __init__(self):
        self.__listaMed = []

    def agregarMedicamento(self, med):
        if type(med) == medicamento:
            self.__listaMed.append(med)

    def leerArchivoMedicamentos(self):
        band = False
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if not band:
                band = True
            else:
                unMedicamento = medicamento(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila [6])
                self.agregarMedicamento(unMedicamento)

    def mostrarLista(self):
        for i in self.__listaMed:
            print(i)

    def mostrarMedicamentoPaciente(self, idCama):
        total = 0
        for i in self.__listaMed:
            if i.getId() == idCama:
                print(i)
                total += i.getPrecio() * i.getCantidad()
        return total
