class medicamento:
    __idCama = 0
    __idMedicamento = 0
    __nombreComercial = ''
    __monodroga = ''
    __presentacion = ''
    __cantidad = 0
    __precio = 0

    def __init__(self, idCama, idMed, nombre, monodroga, presentacion, cant, precio):
        self.__idCama = idCama
        self.__idMedicamento = idMed
        self.__nombreComercial = nombre
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cantidad = int(cant)
        self.__precio = float(precio)

    def __str__(self):
        return '{:<12}/ {:<16} {:^16} {:>6} {:>12}'.format(self.__nombreComercial, self.__monodroga, self.__presentacion, self.__cantidad, self.__precio)

    def getId(self):
        return self.__idCama

    def getPrecio(self):
        return self.__precio

    def getCantidad(self):
        return self.__cantidad
