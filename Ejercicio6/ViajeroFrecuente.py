class ViajeroFrecuente:
    __numViajero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millasAcumuladas = 0

    def __init__(self, numViajero, dni, nombre, apellido, millasAcumuladas):
        self.__numViajero = str(numViajero)
        self.__dni = str(dni)
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__millasAcumuladas = int(millasAcumuladas)

    def __str__(self):
        return 'NUMERO VIAJERO: {:4}  DNI: {:10} NOMBRE Y APELLIDO: {} {:10} MILLAS ACUMULADAS: {}.'.format(self.__numViajero, self.__dni, self.__nombre, self.__apellido, self.__millasAcumuladas)

    def totalMillas(self):
        return self.__millasAcumuladas

    def canjearMillas(self, millasCanjeadas):
        if self.__millasAcumuladas > millasCanjeadas:
            self.__millasAcumuladas -= millasCanjeadas
            return self.__millasAcumuladas
        else:
            print('La cantidad de millas a canjear debe ser menor a las millas totales.')
            return self.__millasAcumuladas

    def retornaNum(self):
        return self.__numViajero

#   SOBRECARGA DE OPERADORES
    def __gt__(self, other):
        return self.__millasAcumuladas > other.totalMillas()

    def __eq__(self, other):
        return self.__millasAcumuladas == other.totalMillas()

    def __add__(self, millas):
        self.__millasAcumuladas += millas

    def __sub__(self, millas):
        self.__millasAcumuladas -= millas
