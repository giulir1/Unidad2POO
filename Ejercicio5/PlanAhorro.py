class PlanAhorro:
    cantidadCuotas = 60
    cuotasLicitacion = 10

    def __init__(self, codigo, modelo, version, valor):     # constructor
        self.__codigo = str(codigo)
        self.__modelo = str(modelo)
        self.__version = str(version)
        self.__valor = float(valor)

    def __str__(self):
        return '{:<8} {:<8} {:<15} {:<14.2f} {:<4} {:11}'.format(self.__codigo, self.__modelo, self.__version, self.__valor, self.getCantidadCuotas(), self.getCuotasLicitacion())

    def calculoCuota(self, cantidadCuotas):
        recargo = self.__valor + self.__valor * 0.1                # aumenta el 10% del valor al pagar en cuotas
        return float(recargo / cantidadCuotas)                     # calcula el valor de la cuota con el 10% de recargo

    def cambioValor(self, nuevoValor):
        self.__valor = nuevoValor

    def getCodigo(self):
        return self.__codigo

    def getModelo(self):
        return self.__modelo

    def getVersion(self):
        return self.__version

    def getValor(self):
        return self.__valor

    @classmethod
    def getCantidadCuotas(cls):
        return cls.cantidadCuotas

    @classmethod
    def getCuotasLicitacion(cls):
        return cls.cuotasLicitacion
