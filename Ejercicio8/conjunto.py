class conjunto:
    __conj = []

    def __init__(self, lista=[]):
        self.__conj = lista

    def __str__(self):
        return '{}'.format(self.__conj)

    def getLista(self):
        return self.__conj

    # SOBRECARGA

    def __add__(self, other):
        lista = self.__conj.copy()
        for i in other.getLista():
            if i not in lista:
                lista.append(i)
        return conjunto(lista)

    def __sub__(self, other):
        lista = self.__conj.copy()
        for i in other.getLista():
            if i in lista:
                lista.remove(i)
        return conjunto(lista)

    def __eq__(self, other):
        band = False
        if set(self.__conj) == set(other.getLista()):
            band = True
        return band
