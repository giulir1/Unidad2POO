class cama:
    __idCama = 0
    __habitacion = 0
    __estado = False
    __apellidoNombre = None
    __diagnostico = ''
    __fechaInternacion = ''
    __fechaAlta = ''

    def __init__(self, idCama, hab, estado, nom, diag, fechaInt):
        self.__idCama = idCama
        self.__habitacion = hab
        self.__estado = estado
        self.__apellidoNombre = nom
        self.__diagnostico = diag
        self.__fechaInternacion = fechaInt
        self.__fechaAlta = 'None'

    def __str__(self):
        return 'Paciente: {:<15} Cama: {:<4} Habitación: {:<4}\nDiagnóstico: {:<14} Fecha de internación: {:<10}\nFecha de alta: {:<10}'.format(self.__apellidoNombre, self.__idCama, self.__habitacion, self.__diagnostico, self.__fechaInternacion, self.__fechaAlta)

    def getId(self):                        # devuelve idCama
        return self.__idCama

    def getPaciente(self):                  # devuelve apellido y nombre
        return self.__apellidoNombre

    def getDiagnostico(self):               # devuelve diagnostico
        return self.__diagnostico

    def cambiarAlta(self, fecha):
        self.__fechaAlta = fecha
