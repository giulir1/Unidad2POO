class Ventana:
    __titulo = ''
    __vSupIzq = []
    __vInfDer = []

    def __init__(self, titulo='', vSupIzq=[0, 0], vInfDer=[500, 500]):
        self.__titulo = titulo
        if (vSupIzq[0] < vInfDer[0]) and (vSupIzq[1] < vInfDer[1]) and (vSupIzq >= [0, 0]) and (vInfDer <= [500, 500]):
            self.__vSupIzq = vSupIzq
            self.__vInfDer = vInfDer
        else:
            self.__vSupIzq = [0, 0]
            self.__vInfDer = [500, 500]

    def mostrar(self):
        print('Título: {}\nVértice superior izquierdo: ({},{}). Vértice inferior derecho: ({},{}).'.format(self.__titulo, self.__vSupIzq[0], self.__vSupIzq[1], self.__vInfDer[0], self.__vInfDer[1]))

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return self.__vInfDer[1] - self.__vSupIzq[1]

    def ancho(self):
        return self.__vInfDer[0] - self.__vSupIzq[0]

    def moverDerecha(self, desp=1):
        if (self.__vInfDer[0] + desp) <= 500:
            self.__vSupIzq[0] += desp
            self.__vInfDer[0] += desp

    def moverIzquierda(self, desp=1):
        if (self.__vSupIzq[0] - desp) >= 0:
            self.__vSupIzq[0] -= desp
            self.__vInfDer[0] -= desp

    def bajar(self, desp=1):
        if (self.__vInfDer[1] + desp) <= 500:
            self.__vSupIzq[1] += desp
            self.__vInfDer[1] += desp

    def subir(self, desp=1):
        if (self.__vSupIzq[1] - desp) >= 0:
            self.__vSupIzq[1] -= desp
            self.__vInfDer[1] -= desp
